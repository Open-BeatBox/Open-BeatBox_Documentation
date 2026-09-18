# Content Style Guide

## Voice and tone
- Clear, concise, and confident; favor active voice.
- Assume readers are technically capable but may be new to behavioral hardware.
- Define domain terms on first use; avoid unexplained acronyms.

## Formatting
- One H1 per page; use logical heading hierarchy.
- Prefer short paragraphs and bullet lists.
- Use fenced code blocks with language hints (` ```bash `, ` ```ts `).
- Always include alt text for images; store assets in `docs/assets/` or `public/` as appropriate.

## Links and navigation
- Use relative links between wiki pages (e.g., `[Development](development.md)`).
- Keep link text descriptive (`Preview locally` instead of `click here`).
- Update `mkdocs.yml` when adding new pages so navigation stays current.

## Examples
- Good: “Run `npm run build` before merging to catch integration issues.”
- Avoid: “Just run the build” (vague) or “obviously” (assumes knowledge).

## Writing for the site content
- Keep hero titles punchy; subtitles should clarify value.
- Section titles should summarize the takeaway (“Why Open-BEATBox for home-cage tasks?”).
- For FAQs, answer directly in the first sentence, then add detail if needed.
- When describing hardware, call out safety and calibration steps explicitly.
