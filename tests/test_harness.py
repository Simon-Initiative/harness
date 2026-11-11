import copy
import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import yaml

ROOT = Path(__file__).resolve().parents[1]
def module(name, file):
    spec = importlib.util.spec_from_file_location(name, ROOT / file)
    obj = importlib.util.module_from_spec(spec); spec.loader.exec_module(obj); return obj
req = module('requirements_trace', 'skills/requirements/scripts/requirements_trace.py')
boot = module('seed', 'skills/bootstrap/seed_harness_contract.py')
contract = module('contract', 'skills/bootstrap/validate_harness_contract.py')

class HarnessTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.work = Path(self.tmp.name)
        self.doc = yaml.safe_load((ROOT / 'skills/requirements/assets/templates/requirements_template.yml').read_text())
    def write(self, doc=None):
        (self.work / 'requirements.yml').write_text(yaml.safe_dump(self.doc if doc is None else doc))
    def cli(self, *args, script='skills/validate/scripts/validate_work_item.py'):
        return subprocess.run([sys.executable, str(ROOT / script), str(self.work), *args], capture_output=True, text=True)
    def test_missing_empty_malformed_requirements(self):
        for content in (None, '', 'requirements: [', 'version: 1\nrequirements: []', '- wrong'):
            with self.subTest(content=content):
                if content is not None: (self.work/'requirements.yml').write_text(content)
                self.assertNotEqual(self.cli('--check', 'requirements').returncode, 0)
    def test_canonical_nested_and_duplicates(self):
        req.validate(self.doc, self.work)
        for mutation in ('empty', 'duplicate_fr', 'duplicate_ac', 'bad_id'):
            doc = copy.deepcopy(self.doc)
            if mutation == 'empty': doc['requirements'][0]['acceptance_criteria'] = []
            if mutation == 'duplicate_fr': doc['requirements'] *= 2
            if mutation == 'duplicate_ac': doc['requirements'][0]['acceptance_criteria'] *= 2
            if mutation == 'bad_id': doc['requirements'][0]['acceptance_criteria'][0]['id'] = 'bad'
            with self.assertRaises(ValueError): req.validate(doc, self.work)
    def test_evidence_and_no_source_scanning(self):
        (self.work/'unrelated.py').write_text('# AC-001')
        ac = self.doc['requirements'][0]['acceptance_criteria'][0]
        ac['evidence'] = [{'path': 'work:missing.txt', 'supports': 'manual observation'}]
        with self.assertRaises(ValueError): req.validate(self.doc, self.work)
        ac['evidence'][0]['path'] = 'work:unrelated.py'
        self.write(); result = self.cli('--check', 'requirements')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('no execution or semantic coverage claim', result.stdout)
        for path in ('work:../outside', 'https://example.org', 'repo:unrelated.py', 'work:/etc/passwd'):
            ac['evidence'][0]['path'] = path
            with self.assertRaises(ValueError): req.validate(self.doc, self.work)
    def test_capture_idempotent_and_atomic_on_error(self):
        payload = self.work/'payload.yml'; payload.write_text(yaml.safe_dump(self.doc))
        req.capture(self.work, payload); req.capture(self.work, payload)
        self.assertEqual(req.load(self.work/'requirements.yml'), self.doc)
        before = (self.work/'requirements.yml').read_bytes()
        payload.write_text('version: 1\nrequirements: []')
        with self.assertRaises(ValueError): req.capture(self.work, payload)
        self.assertEqual((self.work/'requirements.yml').read_bytes(), before)
    def test_capture_replaces_criteria_retains_omitted_requirements(self):
        self.doc['requirements'].append({'id':'FR-002','title':'Second','acceptance_criteria':[{'id':'AC-002','title':'Second criterion'}]})
        self.write()
        update = copy.deepcopy(self.doc); update['requirements'] = update['requirements'][:1]
        update['requirements'][0]['acceptance_criteria'][0]['title'] = 'Revised'
        payload = self.work/'update.yml'; payload.write_text(yaml.safe_dump(update))
        req.capture(self.work, payload)
        result = req.load(self.work/'requirements.yml')
        self.assertEqual(len(result['requirements']), 2)
        self.assertEqual(result['requirements'][0], update['requirements'][0])
    def test_duplicate_yaml_keys(self):
        (self.work/'requirements.yml').write_text('version: 1\nversion: 1\nrequirements: []')
        self.assertNotEqual(self.cli('--check','requirements').returncode, 0)
    def test_small_workflows_and_compact_feature(self):
        for workflow in ('work', 'bug', 'prototype'):
            self.assertEqual(self.cli('--workflow', workflow).returncode, 0)
        (self.work/'plan.md').write_text('Implement task; TODO follow-up outside scope.\n- [ ] Verify\n')
        self.assertEqual(self.cli('--workflow', 'epic').returncode, 0)
        self.write()
        self.assertEqual(self.cli('--workflow', 'feature').returncode, 0)
        for artifact in ('prd', 'fdd'):
            (self.work/f'{artifact}.md').write_text('Compact valid content without headings.')
            self.assertEqual(self.cli('--check', artifact).returncode, 0)
    def test_bootstrap_preserves_legacy(self):
        (self.work/'ARCHITECTURE.md').write_text('Substantive architecture')
        boot.seed(self.work); contract.validate_contract(self.work)
        self.assertEqual(sorted(p.name for p in self.work.iterdir()), ['AGENTS.md', 'ARCHITECTURE.md'])
        (self.work/'AGENTS.md').write_text('Existing rules')
        boot.seed(self.work)
        self.assertEqual((self.work/'AGENTS.md').read_text(), 'Existing rules')
        (self.work/'harness.yml').write_text('version: 1\ncapabilities:\n  code_review:\n    adoption: disabled\n    default: exclude\n')
        contract.validate_contract(self.work)
    def test_bootstrap_routes_existing_review_policy_without_overwriting(self):
        policy = self.work/'docs/CODEREVIEW.md'
        policy.parent.mkdir()
        original = 'Delegate security and performance to separate reviewer agents.'
        policy.write_text(original)
        boot.seed(self.work)
        self.assertIn('[docs/CODEREVIEW.md](docs/CODEREVIEW.md)', (self.work/'AGENTS.md').read_text())
        self.assertEqual(policy.read_text(), original)
        contract.validate_contract(self.work)
        (self.work/'harness.yml').write_text(yaml.safe_dump({
            'version': 1, 'capabilities': {'code_review': {
                'adoption': 'enabled', 'default': 'include',
                'details_file': 'docs/CODEREVIEW.md'}}}))
        contract.validate_contract(self.work)
        policy.unlink()
        with self.assertRaises(ValueError): contract.validate_contract(self.work)
    def test_installed_namespaced_paths(self):
        target = self.work/'installed skills'; target.mkdir()
        subprocess.run(['bash','-c','source "$1/bin/libharness.sh"; harness_install_target "$1" latest "$2" harness_1', 'smoke', str(ROOT), str(target)], check=True, capture_output=True)
        installed = target/'harness_1'
        self.assertTrue((installed/'harness-develop/SKILL.md').is_file())
        script = installed/'harness-validate/scripts/validate_work_item.py'
        result = subprocess.run([sys.executable,str(script),str(self.work),'--workflow','work'],cwd='/tmp',capture_output=True,text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        result = subprocess.run([sys.executable,str(installed/'harness-bootstrap/seed_harness_contract.py'),str(self.work/'repo')],cwd='/tmp',capture_output=True,text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        result = subprocess.run([sys.executable,str(installed/'harness-bootstrap/validate_harness_contract.py'),str(self.work/'repo')],cwd='/tmp',capture_output=True,text=True)
        self.assertEqual(result.returncode, 0, result.stderr)

if __name__ == '__main__': unittest.main()
