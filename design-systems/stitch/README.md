# Google Stitch Inspired Design System

[DESIGN.md](https://github.com/VoltAgent/awesome-design-md/blob/main/design-md/stitch/DESIGN.md) based on [Google Stitch](https://stitch.withgoogle.com/docs/design-md/overview) — Google's AI-native design system for content-forward, token-based interfaces. This is not the official design system. Colors, fonts, and spacing are approximated from the public documentation.

## Files

| File | Description |
|------|-------------|
| `DESIGN.md` | Complete design system documentation (9 sections) |

Use [DESIGN.md](https://github.com/VoltAgent/awesome-design-md/blob/main/design-md/stitch/DESIGN.md) as a reference for AI agents (Claude, Cursor, Stitch) to generate UI that follows Google's semantic token architecture.

## Key Characteristics

- **Semantic tokens**: Colors as roles (`--dt-background`, `--dt-surface-container`) not just values
- **Theme-aware**: Same token renders different values in light/dark modes
- **Google Sans**: Single variable font family for all text
- **Material Icons**: Consistent Google iconography
- **Surface elevation**: Depth via background layers, not shadows
- **Content-forward**: Picker components and content libraries as primary patterns

## When to Use

Use Stitch patterns when building:
- AI-generated or AI-assisted interfaces
- Content selection/picker UIs
- Natural language to UI translation systems
- Semantic, theme-aware design tokens

Don't use when:
- Heavy brand-first visual identity is primary
- Custom typography beyond Google Sans is required
- Photographic/immersive product showcases are needed
