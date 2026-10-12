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

## Project screenshots and navigation

The five original project screenshots are copied from the portfolio’s public `imgs/` directory into `assets/screenshots/`. The generator embeds each PNG in a self-contained SVG with its name, description and stack on a black canvas. Project cards are linked from the README. No third-party image service is used.

The four workspace buttons are separate SVG images wrapped in native HTML anchors. Links inside a standalone SVG image would not provide reliable README navigation. Section anchors target About, Skills & Tools, Work and Connect. Decorative graphic backgrounds are black throughout; GitHub controls page margins and spacing around README elements.

The chart’s two footnotes have been removed from its visible artwork at the owner’s request. Source and provisional-rating details remain here and in accessible metadata. Core content also has a collapsible plain-text alternative.

## Tools and capability chart

The capability chart reproduces existing portfolio personal ratings: applied AI 68, UI/UX 65, networking 60, cybersecurity 60, Scrum 56, Linux 43 and Node.js 37. These are personal assessments rather than objective measurements. The source’s cybersecurity rating is provisional. Tools without published scores appear in grouped text, without inferred numerical ratings.

Additional tool and capability labels are grounded in the portfolio’s public descriptions: Figma, Claude, Claude Code, TCP/IP, routing, switching, network automation, technical presentations and data analysis. No education, institution, location or credential details appear in the presentation.

Selected work is restricted to the five projects in the portfolio: Themis, Sentinel, Rochy Spa Center, Sabores del Mar and Vozelia. The first three link to their public sites. Vozelia links to its repository. Sabores del Mar also retains its repository link at the owner’s explicit request. Lucy and the repository-directory shortcut are removed from the profile’s project list and text alternative.

Section 02 uses one heading and one anchor (`#skills`) for languages, capabilities and tools. No continuation heading or separately numbered subsection is used.

## Persistent motion

Skills & Tools uses a one-time bar reveal plus recurring light traces, so visible motion remains after scrolling to later content. Tool categories have staggered light pulses and a short initial entrance; text stays fully legible. Headings, project separators, statistics, contact buttons and the footer include slow recurring traces. Contact arrows move by five pixels. Decorative motion never changes a score, resizes a screenshot or hides essential text.

All recurring motion is disabled with `prefers-reduced-motion: reduce`. Decorative traces disappear in that mode, while static borders, text, scores and full bars remain. Capability scores are independent self-assessments; a pie chart is deliberately avoided because they are not parts of a shared whole.
