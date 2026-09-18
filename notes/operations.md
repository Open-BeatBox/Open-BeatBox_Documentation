# Operations

## Local checks (site + wiki)
- Lint: `npm run lint` (run from `site/`)
- Types: `npm run type-check` (run from `site/`)
- Tests: `npm run test` (run from `site/`)
- Build: `npm run build` (run from `site/`)
- Docs (wiki): `mkdocs build --strict -f resources/mkdocs.yml -d resources/docs-site`

## Environment variables
Create `site/.env.local` from `site/.env.example`:
- `NEXT_PUBLIC_SITE_URL` - canonical URLs, sitemap, and robots.
- `NEXT_PUBLIC_GA_ID` - optional Google Analytics measurement ID.

## Deployment (site)
- GitHub Actions/Pages (static export): `.github/workflows/deploy-site.yml` builds the site from `site/` and publishes `site/out` to `gh-pages`.
- Manual: run `npm run build` from `site/`, then publish `site/out` to a static host.

## Deployment (MkDocs wiki)
- CI workflow: `.github/workflows/mkdocs.yml` builds `resources/docs/` with `mkdocs build --strict -f resources/mkdocs.yml -d resources/docs-site` and publishes to the `gh-pages-docs` branch.

## Runbook: common issues
- **Broken links or missing assets**: run `npm run build` and fix reported paths; ensure images exist in `public/` or correct relative paths in Markdown.
- **Future-dated blog post not visible**: verify `publishAt` is in the past or remove it.
- **Navigation missing a page**: ensure `showInNav: true` and `navOrder` are set, and frontmatter `slug` is correct.
- **Stale caches**: remove `.next/` and restart the dev server; for MkDocs, remove `.cache/` and rerun `mkdocs serve`.

## Maintaining the wiki
- Edit Markdown in `resources/docs/` and update `resources/mkdocs.yml` navigation.
- Preview locally with `mkdocs serve -f resources/mkdocs.yml`.
- Keep screenshots and diagrams in `resources/docs/assets/` with descriptive filenames.

## Field operations reminders
- Back up configurations before firmware/runtime updates.
- Keep a device inventory with firmware versions and configuration hashes.
- For multi-cage deployments, monitor clock sync and storage health; schedule periodic validation runs.
