# Getting Started (Dev)

For contributors working on the Open-BEATBox website and documentation.

## Prerequisites
- Node.js 18+ and npm.
- Git for version control.
- Optional: Python 3.10+ and `pip install mkdocs mkdocs-material` to preview this wiki locally.

## Install the project
```bash
git clone https://github.com/Open-BeatBox/Open-BeatBox.github.io.git
cd Open-BeatBox.github.io
npm install
```

## Run locally
```bash
npm run dev
# Open http://localhost:3000
```

## Validate before pushing
- Lint: `npm run lint`
- Type check: `npm run type-check`
- Tests: `npm run test`
- Build: `npm run build`
- Docs preview: `mkdocs serve` (from repo root)

## Adding site content
1. Duplicate an existing Markdown file in `content/` (or create one).
2. Set frontmatter: `title`, `layout` (e.g., `page` or `blog`), `slug`, `hero`, `sections`, and navigation fields (`showInNav`, `navOrder`).
3. For blog posts, place files in `content/blog/` with `layout: "blog"` and `publishAt`. Future-dated posts stay hidden until their date.
4. Run `npm run dev` to preview changes. Navigation derives from `showInNav` and `navOrder`.

## Working on the wiki
- Edit Markdown in `docs/` and update navigation in `mkdocs.yml` when adding pages.
- Preview the wiki with `mkdocs serve` and validate with `mkdocs build --strict`.
