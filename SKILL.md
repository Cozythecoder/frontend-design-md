---
name: frontend-design-md
description: Design system intelligence, cinematic scroll animations, data visualization, and SVG creation - all in one unified skill.
trigger: [design, system, ui, chart, data, svg, icon, logo, parallax, scroll, animation, color, typography]
allowed-tools: [Read, Bash(python3:skills/*/scripts/*), Bash(curl), Glob, Grep, WebFetch]
---

# Frontend Design MD

A unified design skill combining 60+ design system references, cinematic animations, data visualization, and SVG creation.

## Available Commands

| Command | Description |
|---------|-------------|
| `/design analyze` | Analyze project and recommend design system |
| `/design apply <system>` | Apply specified design system (linear, vercel, etc.) |
| `/epic scroll` | Initialize cinematic 2.5D parallax site |
| `/chart from <data>` | Generate chart from data source |
| `/data query <source>` | Query public datasets (FRED, etc.) |
| `/svg icon <name>` | Create optimized SVG icon |
| `/svg logo <desc>` | Generate geometric SVG logo |
| `/design systems` | List available 60+ design systems |

## Natural Language Triggers

Also activates on phrases like:
- "Apply Linear design system"
- "Build epic scroll site"
- "Create chart from this data"
- "Get CPI data from FRED"
- "Make a search icon SVG"
- "Design a geometric logo"

## Auto-Detection

When opening any project, automatically:
1. Detect project category (saas, content, creative, enterprise)
2. Extract existing color/font tokens
3. Recommend best-matching design system
4. Offer to apply with `/design apply <system>`
