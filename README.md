# Global Briefing — 18 November 2026

![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)
![news-image-20261118](https://img.shields.io/badge/competition-news--image--20261118-green)
![entry](https://img.shields.io/badge/entry-poster-red)

A one-page news poster summing up Wednesday 18 November 2026 — the
day the US–Iran confrontation in the Gulf dominated the front page.

## The 12 stories

1. **US destroys five Iranian oil tankers** — strikes on the Kaviz,
   Charminar, Horizon 1, Riesco, and Derya; Iran hits back at 10 ships
   near Hormuz and the US base in Jordan; oil surges past $100.
2. **Shenzhen Summit** — Putin arrives; Trump, Xi, and Putin meet Nov 19.
3. **Kerch Bridge struck again** — Ukraine hits it a second night;
   Russia hits bridges too.
4. **US loses measles-free status** — 5,400+ cases, the most since 1991.
5. **Eisenkot to form government** — Herzog bypasses Netanyahu; an ally
   is elected speaker.
6. **Gaza winter crisis** — the UN warns of cold deaths; 1.7M displaced
   people need aid.
7. **COP31 deadlock** — 144 items disputed as talks enter their final days.
8. **Pattinson named Bond.**
9. **Cyber-attack hits European supermarket freezers.**
10. **US details $12B Venezuela revenue.**
11. **France protests enter a 4th weekend.**
12. **Peltola wins Alaska Senate.**

## How the image was made

The poster is a single self-contained HTML file (`poster.html`) — dark
navy layout, a radar motif drawn with inline SVG, no photos, no external
fonts or assets. It is rendered to a 1024×1024 PNG with Playwright
(`shoot.mjs`), and `main.py` copies that PNG to `/output/entry.png`
byte-for-byte, verifying the PNG signature, the 1 MiB size limit, and
that the delivered copy is identical to the source.
