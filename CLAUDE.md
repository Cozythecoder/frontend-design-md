# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

## Project Overview

This is a comprehensive design system collection and skill library for Claude Code, organized into three layers:

1. **Static References**: 60+ DESIGN.md files (design-systems/)
2. **Active Skills**: Intelligence + Epic design (skills/)
3. **Data/Visualization**: OpenData skills (plugins/)

## Repository Architecture

### Layer 1: Design System Collection (`design-systems/`)

Plain-text design specifications following the 9-section Stitch format:
- Extracted from real websites
- Semantic naming + hex values
- No code, just specifications
- For reference and copying

### Layer 2: Claude Code Skills (`skills/`)

Executable skills that integrate with Claude Code:

**design-systems skill:**
- Auto-detects project category
- Recommends optimal design system
- Extracts existing tokens
- Validates application

**epic-design skill:**
- Trigger phrases for activation
- Pre-flight asset inspection
- 6-level parallax depth system
- Quality gates

### Layer 3: OpenData Plugins (`plugins/`)

Specialized skills for data and graphics:
- opendata-api: REST API queries
- openchart: Data visualization specs
- svg-design: Hand-written SVGs

## File Organization Standards

### DESIGN.md Files

All design system entries must include:
1. 9 sections (Visual Theme through Agent Prompts)
2. Semantic color names with hex values
3. Complete typography hierarchy table
4. Component specifications
5. Spacing system

### SKILL.md Files

Must include YAML frontmatter:
```yaml
---
name: skill-name
description: Imperative description under 1024 chars
---
```

Body should be under 500 lines; lengthy content goes in `references/`.

### Skill Directory Structure

```
skill-name/
├── SKILL.md              # Main skill definition
├── evals/                # Evaluation tests
│   └── evals.json
├── scripts/              # Executable tools
│   └── *.py, *.js
├── references/           # Extended documentation
│   └── *.md
└── assets/               # Static assets
    └── *
```

## Key Principles

### Design Systems (Static)
- **Factual extraction**: Document what sites actually do
- **Semantic naming**: "Pure Black" not just "#000"
- **Complete specs**: All 9 sections mandatory
- **No opinions**: Describe, don't prescribe

### Skills (Active)
- **Auto-detection**: Minimize user input required
- **Pre-flight**: Check before acting (stolen from Epic)
- **Validation**: Quality gates after application
- **Executable**: Scripts, not just descriptions

### Consistency
- 4px or 8px spacing base units
- Semantic color tokens
- Systematic typography scales
- WCAG AA contrast minimum

## Contributing Guidelines

### Adding a Design System

1. Create directory: `design-systems/<site-name>/`
2. Add DESIGN.md with all 9 sections
3. Add README.md with source attribution
4. Test color contrast ratios
5. Verify all hex codes are accurate

### Adding a Skill

1. Follow `plugins/<name>/skills/<skill-name>/` structure
2. Include YAML frontmatter in SKILL.md
3. Add evals/evals.json with test cases
4. Make scripts self-contained and documented
5. Keep references focused and linkable

### Modifying Existing Files

- Preserve semantic naming conventions
- Maintain 9-section DESIGN.md structure
- Update references if moving content
- Test scripts still execute

## Common Tasks

### Analyze a New Website

```bash
# 1. Download website
wget --mirror --convert-links --adjust-extension --page-requisites --no-parent https://example.com -P design-systems/example/

# 2. Extract design tokens
python3 skills/design-systems/scripts/analyze-project.py design-systems/example/

# 3. Create DESIGN.md from extraction
# 4. Verify against actual website
```

### Test Skill Detection

```bash
python3 skills/design-systems/scripts/analyze-project.py ./test-project
```

### Validate Design System Application

```bash
python3 skills/design-systems/scripts/validate-application.py ./my-project linear.app
```

## Integration Points

### Claude Code Plugin Registry

`.claude-plugin/marketplace.json` defines:
- Plugin name and description
- Available skills
- Repository URL
- License

### GitHub Actions

`.github/workflows/` should include:
- Validation on PR (check DESIGN.md structure)
- Script testing
- Marketplace version bump on merge

## Reference Documentation

For detailed specification:
- [Stitch DESIGN.md format](https://stitch.withgoogle.com/docs/design-md/overview)
- [Agent Skills spec](https://github.com/tryopendata/skills/blob/main/CLAUDE.md)

---

**Remember**: This repository bridges static design documentation with active implementation skills. Design systems describe; skills execute.
