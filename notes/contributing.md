# Contributing to the documentation

The contribution guide for the whole project is part of the manual: `source/contributing.md` (published at <https://open-beatbox.github.io/docs/manual/contributing.html>). It explains which repository takes which contribution, how to build the manual locally, and the writing style.

Quick checklist for a documentation pull request:

- [ ] The manual builds with **no warnings**: `python -m sphinx -b html source _build/html`
- [ ] New pages are in a `toctree`
- [ ] New terms are in the glossary
- [ ] Claims were checked against the code or design files; uncertain points are in `source/project/status.md`
- [ ] Images are small and have alt text
- [ ] The changelog (`notes/changelog.md`) has an entry
