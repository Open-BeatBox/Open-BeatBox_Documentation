# Contributing

## Code of conduct
Be respectful and constructive. Assume good intent, and surface concerns with empathy. Escalate harmful behavior to maintainers.

## Ways to contribute
- File issues with clear steps, expected vs. actual behavior, and screenshots/logs when helpful.
- Improve content structure and copy in `content/`.
- Extend components or styling to support new section types.
- Enhance documentation and runbooks in `docs/`.
- Contribute hardware build notes (BOM, wiring diagrams) and link to firmware/runtime repositories.

## Pull request checklist
- [ ] Branch created from `main`
- [ ] `npm run lint`, `npm run type-check`, `npm run test`, and `npm run build` pass
- [ ] For docs: `mkdocs build --strict` passes
- [ ] Links and assets verified; navigation updated if needed
- [ ] PR description explains what/why, testing performed, and screenshots for UI changes

## Reviews and approvals
- Seek at least one maintainer review for non-trivial changes.
- Address feedback with follow-up commits (avoid force-push when possible to keep context).
- Re-run validations after major updates.
- For hardware/firmware docs, include pin maps, configuration files, and version/commit references.

## Filing issues
- Use a descriptive title.
- Include environment info (OS, browser, Node.js version); for hardware issues, add device ID, firmware/runtime version, and wiring notes.
- Provide reproduction steps or sample content snippets/logs that trigger the issue.
