# NixOS Cyber-Rice

An original GitHub profile design for Alberto Davis. Source of professional information: [live portfolio](https://albdavis.zenreverse.space), reviewed October 12, 2026.

## Visual system

Black (`#000000`) is the canvas, outer gutter and section separator. Near-black (`#02091A`) is reserved for the hero surface. Deep blue (`#032999`) separates structural details; electric blue (`#0161EA`) and cyan (`#18DCF9`) provide accents. Neutral light text (`#F4F7FB`) and secondary text (`#C4D0DA`) improve readability. Pale cyan (`#9BEAF5`) distinguishes the role from brighter accent labels. System sans-serif typography carries the content; monospace is limited to small labels and numbers.

Headings use natural language. Information remains readable in native Markdown, independent of decorative images. SVGs have accessible descriptions, local resources and no scripts or remote fonts. SVG CSS provides a slow decorative halo pulse, a restrained hero light sweep and a one-time chart reveal. Text remains static. All motion is disabled under `prefers-reduced-motion: reduce`; the full chart and information remain visible without animation. The hero has a dedicated mobile composition. GitHub controls the surrounding page background; the profile cannot override visitors’ themes or apply global CSS.

The six-arm emblem is original and is not an official NixOS logo. NixOS, i3 and Polybar are visual references, not claims about installed systems or technical proficiency.

## Language chart

`assets/languages.svg` is a custom segmented horizontal bar chart. It reproduces the live portfolio’s published personal ratings, rather than inferring skills from repository sizes:

| Portfolio category | Personal rating / 100 |
| --- | ---: |
| HTML / CSS | 82 |
| SQL / MySQL / PostgreSQL | 77 |
| Python | 68 |
| PHP | 66 |
| JavaScript | 48 |
| TypeScript / Next.js | 48 — provisional |

The grouped categories are preserved in the accessible README explanation. TypeScript / Next.js is explicitly provisional in the source. These are self-assessments, not objective measurements, certifications, market benchmarks or shares of code. Do not assign values to languages that lack ratings.

## Content and privacy

The profile uses only the display name Alberto Davis. Personal education and location details are omitted from the current README, artwork, metadata and generator. Contact goes through the portfolio and publicly listed professional channels. The linked portfolio remains an external, independently maintained source. Earlier Git commits remain in normal history.

Project descriptions follow the portfolio; Lucy’s additional link follows its public repository. No private repository content is published. The public GitHub snapshot dated October 12, 2026 counts four original project repositories, one practice fork and this profile repository.

## Maintenance

Edit `scripts/generate.py` to update artwork and chart values, then run `python scripts/generate.py`. Python standard library only. Update the README alternative text and this note when changing values. Commit only README.md, assets/ and scripts/. No automatic updates or external statistics services are required.

## Inspiration

[Polybar Themes](https://github.com/adi1090x/polybar-themes), [NixOS Branding](https://github.com/NixOS/branding), [Profile Signal Kit](https://github.com/saroo98/profile-signal-kit) and [SVG README](https://github.com/Wenoxxxx/svg-readme). No reference code or artwork is incorporated.
