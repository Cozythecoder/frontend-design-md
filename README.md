# Frontend Design MD

A curated collection of DESIGN.md files and Claude Code skills for building beautiful, consistent web interfaces.

## What This Repository Contains

### 1. Design System Collection (`design-systems/`)

60+ DESIGN.md files extracted from notable websites:
- **SaaS/Developers**: Linear, Vercel, Supabase, Stripe, GitHub
- **Product/E-commerce**: Apple, Shopify, Nike
- **Creative**: Framer, Webflow
- **Content**: Medium, Substack
- **Enterprise**: IBM, Salesforce
- **Luxury**: Tesla, Ferrari, BMW

Each follows the 9-section format: Visual Theme, Colors, Typography, Components, Layout, Depth, Do's/Don'ts, Responsive, Agent Prompts.

### 2. Design System Intelligence Skill (`skills/design-systems/`)

Automatically detect project type and apply optimal design system:
- **Auto-detection**: Analyzes project files to recommend design system
- **Pre-flight protocol**: Asset inspection, token extraction
- **Intelligent adaptation**: Maps existing tokens to design system
- **Quality gates**: 11 validation rules

### 3. Epic Design Skill (`skills/epic-design/`)

Build cinematic, scroll-driven 2.5D websites:
- **6-level depth system**: Parallax from 0.10x to 1.20x
- **45+ animation techniques**: Scroll-linked timelines, pinning, reveals
- **Asset pipeline**: Pre-flight image inspection
- **Quality assurance**: 11 non-negotiable rules

### 4. OpenData Skills (`plugins/`)

From [tryopendata/skills](https://github.com/tryopendata/skills):
- **opendata-api**: Query public datasets via REST API
- **openchart**: Generate charts, tables, graphs from data
- **svg-design**: Create hand-written SVG logos and icons

## Installation

### As Claude Code Skill

```bash
# Clone to skills directory
git clone https://github.com/cozy/frontend-design-md ~/.claude/skills/frontend-design-md
```

Or symlink for development:
```bash
ln -s /path/to/frontend-design-md ~/.claude/skills/frontend-design-md
```

Restart Claude Code, then run `/plugin` to verify.

## Usage

### Commands

| Command | Description |
|---------|-------------|
| `/design analyze` | Analyze project and recommend design system |
| `/design apply <system>` | Apply design system (linear, vercel, apple, etc.) |
| `/design systems` | List all 60+ available design systems |
| `/epic scroll` | Initialize cinematic 2.5D parallax website |
| `/chart from <data>` | Generate chart from CSV/JSON data |
| `/data query <source>` | Query public datasets (FRED, etc.) |
| `/svg icon <name>` | Create optimized SVG icon |
| `/svg logo <desc>` | Generate geometric SVG logo |

### Natural Language

Just say what you want:
- "Apply Linear design to my project"
- "Build epic scroll site with parallax"
- "Create chart from this data"
- "Get CPI data from FRED"
- "Make a search icon SVG"
- "Design a geometric logo"

### Direct Script Usage

```bash
# Run project analysis
python3 skills/design-systems/scripts/analyze-project.py ./my-project

# Validate application
python3 skills/design-systems/scripts/validate-application.py ./my-project linear.app

# Copy a design system reference
cp -r design-systems/vercel ./my-project/design/
```

## Repository Structure

```
/
├── README.md                          # This file
├── CLAUDE.md                          # Contributor guidance
├── .gitignore                         # Allowlist strategy
├── .claude-plugin/
│   └── marketplace.json               # Plugin registry
│
├── design-systems/                    # 60+ DESIGN.md files
│   ├── apple/
│   │   ├── DESIGN.md
│   │   └── README.md
│   ├── linear.app/
│   ├── vercel/
│   └── ... (60+ more)
│
├── skills/
│   ├── design-systems/                # Auto-detection skill
│   │   ├── SKILL.md
│   │   ├── references/
│   │   └── scripts/
│   │
│   └── epic-design/                   # Cinematic scroll skill
│       ├── SKILL.md
│       ├── references/
│       │   ├── depth-system.md
│       │   ├── motion-system.md
│       │   └── ...
│       └── scripts/
│
└── plugins/                           # OpenData skills
    ├── opendata/skills/opendata-api/
    ├── openchart/skills/openchart/
    └── opendesign/skills/svg-design/
```

## Design System Format

All DESIGN.md files follow the 9-section format introduced by Google Stitch:

1. **Visual Theme & Atmosphere** - Mood, density, principles
2. **Color Palette & Roles** - Semantic names with hex codes
3. **Typography Rules** - Families, hierarchy, scales
4. **Component Stylings** - Buttons, cards, inputs, navigation
5. **Layout Principles** - Spacing, grids, section patterns
6. **Depth & Elevation** - Shadow systems
7. **Do's and Don'ts** - Design guardrails
8. **Responsive Behavior** - Breakpoints, touch targets
9. **Agent Prompt Guide** - Quick reference

## Contributing

- Fix wrong colors or missing tokens
- Add missing sections to incomplete DESIGN.md files
- Improve descriptions for clarity
- Add new design systems following the pattern
- Enhance skills with better detection algorithms

## License

MIT - Free to use for any project.

## Acknowledgments

- Format inspired by [Google Stitch](https://stitch.withgoogle.com/)
- OpenData skills from [tryopendata/skills](https://github.com/tryopendata/skills)
- Epic design patterns from [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills)
