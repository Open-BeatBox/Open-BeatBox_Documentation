# Architecture

## System overview
- Open-BEATBox is a modular home-cage behavioral platform combining hardware (sensors/actuators), firmware/runtime for task control, and data pipelines for acquisition and analysis.
- This repository hosts the public website and documentation; reference external firmware/runtime repos and hardware BOMs where applicable.
- Typical deployment: one controller per cage, networked to a collector or local storage, with a web presence for docs and community.

## System layers
1. **Hardware**: cage, sensors (IR beam, nose-poke, capacitive touch, environmental), actuators (pellet/liquid dispenser, lights), power, and connectivity.
2. **Firmware/runtime** (external repo): pin maps, task logic, device health metrics, logging, and networking (e.g., HTTP/MQTT).
3. **Data layer** (external or shared): log transport, storage (raw + processed), QC pipelines, and dashboards.
4. **Docs/site (this repo)**: Next.js site rendering content from Markdown in `site/content/` and this MkDocs wiki under `resources/docs/`.

## Repo structure (this site)
- `site/content/` - Markdown for pages and blog posts (`site/content/blog/`). `_site.md` stores global metadata (title, description, authors, default OG/Twitter assets).
- `site/src/app/` - Next.js App Router routes, layout, sitemap/robots, loading and not-found states.
- `site/src/components/` - Reusable UI blocks for hero sections, content sections, navigation, and layout.
- `site/src/lib/` - Content parsing (`content.ts`), icon registry, utilities (text truncation, formatting).
- `site/public/` - Static assets (images, icons).
- `site/styles/` - Tailwind layer config plus scoped component CSS.
- `resources/docs/` - MkDocs wiki pages; `resources/mkdocs.yml` controls navigation.

## Content pipeline (site)
1. Markdown is parsed with `gray-matter` for frontmatter and content body.
2. Slugs default to the relative path (with `/home` mapped to `/`) unless explicitly set.
3. Navigation is derived from pages with `showInNav` and ordered by `navOrder`; groups use `navGroup`.
4. Blog posts respect `publishAt`; future-dated posts stay hidden.
5. SEO metadata is built from page fields with fallbacks from `_site.md` (title, description, OG/Twitter defaults). Hero background images or the first Markdown image are used as OG images when available.

## Rendering and styling
- Markdown renders through `react-markdown` with `remark-gfm` and sanitized raw HTML via `rehype-raw` + `rehype-sanitize`.
- Tailwind CSS v4 (via `@tailwindcss/postcss`) provides utility layers; component-specific CSS refines the aesthetic.
- Fonts are loaded through `site/src/app/fonts.css`; global styles in `site/src/app/globals.css`.

## API and integrations
- The site is configured for static export and does not use server-side APIs.

## Build and output
- `npm run build` (run from `site/`) outputs a static export to `site/out/`.
- `mkdocs build -f resources/mkdocs.yml -d resources/docs-site` builds the docs locally.
