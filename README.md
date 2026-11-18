[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/lukekwan/world-news-18-nov-2026/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/lukekwan/world-news-18-nov-2026/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

# The World, 18 November 2026

A breaking-news poster that sums up the world news of Wednesday 18 November 2026, made for the [make.fun news-image-20261118](https://make.fun/bounty/news-image-20261118) competition. One image, the whole day: the US–Iran oil war in the Gulf, the Trump–Xi–Putin summit in Shenzhen, a second night of strikes on the Kerch Bridge, and the measles outbreak that cost the United States its elimination status — plus the smaller stories that filled out the day, from a new James Bond to supermarket freezers going dark across Europe.

## The stories

1. **US destroys five Iranian oil tankers** — Iran hits back at 10 ships and the US base in Jordan, oil pushes past $100.
2. **Trump–Xi–Putin summit** — Putin arrives in Shenzhen, talks on 19 November.
3. **Ukraine hits the Kerch Bridge a second night** — Russia hits bridges in return.
4. **US loses measles-free status** — 5,400+ cases, the most since 1991.
5. **Israel: Herzog asks Eisenkot to form a government**, bypassing Netanyahu.
6. **Gaza winter crisis** — UN warns of cold deaths, 1.7M displaced.
7. **COP31 deadlock in Antalya** — 144 items disputed.
8. **Robert Pattinson named the new James Bond.**
9. **Cyber-attack disables supermarket freezers** across seven European countries.
10. **US details $12bn Venezuelan oil revenue.**
11. **France's fourth weekend of cost-of-living protests.**
12. **Mary Peltola wins the Alaska Senate seat.**

## How it is made

The poster is drawn as a single self-contained HTML page (`poster.html`), rendered to `entry.png` (1024×1024) with a Playwright script (`shoot.mjs`). `main.py` copies `entry.png` to `/output/entry.png`.

To reproduce:

```bash
node shoot.mjs
python3 main.py
```
