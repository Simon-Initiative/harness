# UI Boundaries

UI-layer code should stay focused on presentation, interaction flow, and view state.

- Keep product and domain rules in repository-defined lower layers.
- Avoid placing persistence logic or cross-system orchestration directly in UI handlers.
- Tests for UI code should focus on rendering, interaction flow, and state transitions.
- Use repository-local architecture docs to determine the exact layer names for the target stack.
