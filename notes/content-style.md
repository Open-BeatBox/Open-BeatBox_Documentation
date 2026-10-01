# Content style guide

## Voice and tone

- Clear, concise and confident; favour the active voice.
- **Write for a non-programmer first.** Assume the reader is a neuroscientist or technician who may never have used a terminal.
- Define domain terms on first use, add new ones to the glossary, and avoid unexplained acronyms.
- Say what to *do* and what the reader should *see* afterwards.

## Formatting

- One H1 per page; use a logical heading hierarchy.
- Prefer short paragraphs, numbered steps and tables.
- Use fenced code blocks with a language hint (```` ```bash ````, ```` ```python ````, ```` ```text ```` for diagrams).
- Always include alt text for images. Keep manual images small (about 1000 px wide, under 150 KB) in `source/_static/img/`; keep full-size media in `assets/`.

## Links and navigation

- Link between pages with `{doc}` roles, not by file name.
- Keep link text descriptive ("the flashing guide"), never "click here".
- Add each new page to a `toctree`, then build and check that there are no warnings.

## Facts

- Check statements against the repository files (Hardware, Software) and cite the version in the status page.
- Mark uncertain statements openly rather than guessing, and list them in `source/project/status.md`.
- Do not describe features that do not exist.

## Examples

- Good: "Hold **BOOT** and plug in the USB cable; a drive named RPI-RP2 appears."
- Avoid: "Just flash the board" (vague) or "obviously" (assumes knowledge).

## Hardware and safety

- When describing hardware, call out safety and calibration steps explicitly.
- State the hardware revision (V3) and the software version when it matters.
