# FAQ

- **How do I preview the site locally?** Run `npm run dev` and open http://localhost:3000.
- **How do I preview the wiki?** Install MkDocs + Material (`pip install mkdocs mkdocs-material`), then `mkdocs serve`.
- **Where do docs live?** MkDocs wiki files are in `docs/`; site content lives in `content/`.
- **How do I add a nav item to the site?** Set `showInNav: true` and `navOrder` in the page’s frontmatter.
- **How do I add a nav item to the wiki?** Add the page to `mkdocs.yml` under `nav`.
- **Why is my blog post hidden?** Future-dated posts (via `publishAt`) are suppressed until their date.
- **Where do images go?** Site assets in `public/`; wiki images in `docs/assets/`.
- **How do I link firmware or hardware docs?** Add the repo or file links in relevant pages (e.g., [Hardware Build](hardware-build.md)) and keep version/commit references.
- **How do I deploy the wiki?** Push to `main` or run the MkDocs workflow manually; it publishes `site/` to `gh-pages`.
