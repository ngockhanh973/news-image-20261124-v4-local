#!/usr/bin/env python3
"""
draw25-wed.py -- draws "The Wednesday Globe", Wednesday 25 November 2026.
Built fresh for news-image-20261124 v4-local. Every figure below was checked
against a source read on 25 November 2026; the full citation list, disputes
and LEFT OUT list live in SOURCES.md in this repo.

FIGURE LEDGER (all verified 25 Nov 2026, sources in SOURCES.md)
- Hormuz: 2 tankers hit mines Wed 25 Nov (IRGC via Reuters/OilPrice); no
  names, no toll given; Brent $89.93 at 07:30 GMT (Reuters); UKMTO logged
  3 vessels struck by projectiles on Mon 23 Nov.
- Huawei: jury guilty on 10 of 12 counts, acquitted racketeering +
  obstruction (Reuters, verdict Tue 24 Nov New York); sentencing 14 Sep
  2027; Huawei calls verdict "without legal or factual merit".
- Selloff: Nikkei -2.8% to 57,011.62; KOSPI -6.2%; SoftBank -14.8%;
  Samsung -9.9%; SK Hynix -11.1%; Taiex -4.9%; Nvidia -5.9% Tue, about
  -5% pre-market Wed; Nasdaq -1.48% Tue (AP / Sharecast / Tokenist).
- Shenzhou-24: liftoff 00:18 UTC, docking 03:56 UTC (about 3.5 h);
  3 crew; Zeeshan Ali first foreigner on Tiangong; stay 5-10 days.
- Cartagena: 30 taken Tue, 10 released Tue, 20 freed Wed about 01:00
  local after about 17 h; 1 gunman killed, 4 detained, no hostage died.
- Benghazi: 2 Libyan naval officers died Tue of wounds from the Sun 22
  Nov attack; Haftar vows retaliation; France (Barrot, Wed): self-defence.
- Riyadh: tower strike Tue 24 Nov, 11 hurt (2 Saudi, 2 Indian, 3 Nepali,
  4 Egyptian); Houthis claimed it Wed; 2nd strike in under a week.
- Rosstat leak: at least 490,334 registered military deaths to 29 Sep
  2026 (BBC Russian / Mediazona); model estimate over 700,000 with the
  missing; Rosstat admitted a cyber incident, denied a leak of protected
  data. 490,334 is a TOTAL, not a Wednesday figure.
- Gaza: Tue strike killed Hamas internal security chief Naeem Abu Nahal,
  50, in Gaza City; 6 others killed Tue; Hamas calls it a war crime.
- Poland: Russian drone entered Polish airspace overnight 23-24 Nov;
  2nd incursion in 4 days (3 Kh-101 missiles 20 Nov); Warsaw renewed its
  push for permanent US troops Tue; Moscow rejects the claims.
- Chen Jining: CCDI probe announced Tue 24 Nov; 4th Politburo member
  probed since 2025; Shanghai leadership pledged loyalty Wed.
- Solomon Islands: treaty signed Wed 25 Nov in Canberra; Australia the
  primary security partner; no foreign military base; $740m over 10 years.
- Senegal: CAS ruled Tue 24 Nov, restoring the 2025 AFCON title; final
  1-0 over Morocco in January; Morocco vows to appeal.
- Tariffs: USTR poised to unveil Section 301 findings on 16 economies
  (Reuters, Tue); caps 15% EU/Japan/Korea, 19% Malaysia; no final rates.
- Iran leaders: NBC Tue reported the US weighing strikes on senior
  Iranian leaders incl. Mojtaba Khamenei; Katz: Iran developing chemical
  weapons, pre-emptive strike open; Rubio: no decision made.
- Kyiv: Zelensky says Ukraine needs EUR 115bn in 2027, EUR 90bn
  secured, EUR 25bn gap; about 60 Patriot interceptors held up.
- Canberra: Australia October CPI 4.9% (ABS, released Wed 25 Nov).
- London: Ofgem cap +26% from Jan; typical bill GBP 1,723 -> 2,166
  (+GBP 443); about 20m households; GBP 100 help from 4 Jan.
- Dhaka: garment wage 12,500 -> 17,000 taka (+36%), 4-2 board vote;
  workers wanted 18,000 (revised) after demanding 30,000.
- Damazin: RSF drone strikes Tue night killed 19 civilians, wounded 20
  in Blue Nile (Emergency Lawyers, Wed); RSF did not comment.
- Bogor: 3 bodies recovered Wed, 23 still trapped of 26 in a flooded
  illegal gold mine, 100 m shaft, since Mon.
- Hanoi: gas blast Tue 08:00 at a hotpot eatery: 7 dead, 9 hurt
  (16 casualties); 125 households evacuated. Early count: 6 dead, 10 hurt.
- Ras Al Khaimah: bus hit a parked truck Tue about 01:00: 13 dead
  (11 at the scene, 2 later), 14 taken to hospital, 26 treated at the
  scene; bus carried 41, returning from an Oman visa trip.
- Eskisehir: AS-532 Cougar crashed Tue evening on a training flight;
  5 crew dead; cause unknown; 2nd fatal Turkish military helicopter
  crash in 12 days (Malatya 12 Nov, 4 dead).
- CIA breach: NYT Tue reported a breach of the CIA/ODNI unclassified
  OSINT system; ARTEX AI framework alleged, unconfirmed; no classified
  data; resolved. FinCEN disclosed a separate incident Tue.
- Abrego Garcia: left the US Tue, landed in Madrid Wed morning;
  lawyer: "a free man"; DHS: "self-deported"; nearly 2-year legal fight.
- Pyongyang: N. Korea expelled Swiss envoy Sylvain Astier Wed, 48 h to
  leave, office to close; over sanctions on the Songdowon camp; office
  opened 19 Oct.
- Iowa: Army to detonate about 5 tons of lead azide (68 drums) Wed
  09:00 CT (15:00 UTC); town braces for a lead-dust plume.
- Champions League Tue night: Real Madrid 5-1 PSV (comeback, Mbappe
  scored twice), Arsenal 1-1 Dortmund, Man City 2-2 Napoli.
- Doha: Sooryavanshi, 15, hit 204 off 53 balls, 28 sixes; fastest List
  A double century (52 balls, previous 103); India A beat UAE.
- UK heat: UKHSA 5,258 heat-linked deaths in England, summer 2026,
  a record since 2016, nearly double 2022's 2,985; provisional.
- Lagos: Dangote refinery IPO $1.6bn values it at $48bn; listing
  1 Dec; Africa's biggest listed firm; SEC cleared allotment Mon.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
PRESS = "13:40 UTC"  # press time, Wednesday 25 November 2026

PAPER = (247, 243, 232)
INK = (17, 17, 17)
MUTED = (90, 86, 76)
RULE = (60, 56, 48)
RED = (176, 30, 30)
NAVY = (27, 58, 107)
TEAL = (14, 92, 86)
AMBER = (166, 110, 0)
SKY = (178, 205, 225)
SEA = (64, 110, 150)
LAND = (196, 205, 176)
PANEL_BG = (255, 255, 255)
TAG_FILL = {
    "CONFIRMED": (27, 58, 107),
    "REPORTED": (166, 110, 0),
    "CLAIM": (176, 30, 30),
    "LEAKED": (96, 48, 130),
    "ESTIMATE": (96, 48, 130),
    "TOTAL": (96, 48, 130),
    "SCHEDULED": (14, 92, 86),
}

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def f_serif_b(size):
    return ImageFont.truetype(os.path.join(FONT_DIR, "DejaVuSerif-Bold.ttf"), size)


def f_serif(size):
    return ImageFont.truetype(os.path.join(FONT_DIR, "DejaVuSerif.ttf"), size)


def f_sans_b(size):
    return ImageFont.truetype(os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf"), size)


def f_sans(size):
    return ImageFont.truetype(os.path.join(FONT_DIR, "DejaVuSans.ttf"), size)


# ---------------------------------------------------------------- stories
# (num, city, region, headline, deck, tag, lat, lon, art)
LEADS = [
    (1, "STRAIT OF HORMUZ", "MIDDLE EAST",
     "2 TANKERS ABLAZE IN HORMUZ AFTER HITTING MINES, IRGC SAYS",
     "Tehran calls the ships violators on a banned route and warns all "
     "vessels to obey its orders. No ship named, no toll given. "
     "Oil slid anyway: Brent $89.93.",
     "REPORTED", 26.5, 56.5, "tanker"),
    (2, "NEW YORK", "AMERICAS",
     "JURY FINDS HUAWEI GUILTY ON 10 OF 12 COUNTS; BEIJING CALLS IT REPRESSION",
     "Brooklyn jury convicts on bank fraud and trade-secret theft, clears "
     "Huawei of racketeering. Sentencing 14 September 2027.",
     "CONFIRMED", 40.7, -74.0, "court"),
    (3, "TOKYO", "ASIA",
     "ASIA\u2019S AI RALLY UNWINDS: NIKKEI \u22122.8%, KOSPI \u22126.2%, SOFTBANK \u221214.8%",
     "Nvidia fell 5.9% on Tuesday, a day after Huang\u2019s return sent it "
     "up 31.5%, and slid about 5% more before Wednesday\u2019s open. "
     "Nasdaq fell 1.5% on Tuesday.",
     "CONFIRMED", 35.7, 139.7, "chart"),
]

GRID = [
    (4, "JIUQUAN", "ASIA",
     "SHENZHOU-24: FIRST FOREIGNER DOCKS AT TIANGONG",
     "Three crew, incl. Pakistan\u2019s Zeeshan Ali, docked 3.5 h after "
     "launch. Stay: 5\u201310 days.",
     "CONFIRMED", 39.8, 98.5, "rocket"),
    (5, "CARTAGENA", "AMERICAS",
     "20 HOSTAGES FREED AS TROOPS STORM STORE",
     "Siege ends after about 17 hours. 30 taken, 10 freed first; "
     "1 gunman killed. No hostage died.",
     "CONFIRMED", 10.4, -75.5, "store"),
    (6, "BENGHAZI", "AFRICA",
     "2 LIBYAN OFFICERS DIE OF WOUNDS FROM SHIP STRIKE",
     "Haftar vows retaliation for the Sunday attack on a Russian corvette. "
     "France: self-defence.",
     "CONFIRMED", 32.1, 20.1, "ship"),
    (7, "RIYADH", "MIDDLE EAST",
     "HOUTHIS CLAIM TOWER STRIKE THAT HURT 11",
     "Second hit on the district in under a week. Hurt: 2 Saudis, "
     "2 Indians, 3 Nepalis, 4 Egyptians.",
     "REPORTED", 24.7, 46.7, "tower"),
    (8, "MOSCOW", "EUROPE",
     "LEAKED FILES PUT RUSSIAN WAR DEAD AT 490,334",
     "Rosstat records counted by BBC and Mediazona; model estimate with "
     "the missing passes 700,000.",
     "LEAKED", 55.8, 37.6, "ledger"),
    (9, "GAZA CITY", "MIDDLE EAST",
     "ISRAEL KILLS HAMAS SECURITY CHIEF IN GAZA",
     "Naeem Abu Nahal, 50, died in a Tuesday strike; 6 others were killed "
     "too. Hamas: war crime.",
     "CONFIRMED", 31.5, 34.5, "city"),
    (10, "WARSAW", "EUROPE",
     "RUSSIAN DRONE STRAYS INTO POLAND",
     "Second incursion in 4 days, after 3 missiles on 20 Nov. Jets cleared "
     "to fire but held off.",
     "REPORTED", 52.2, 21.0, "drone"),
    (11, "SHANGHAI", "ASIA",
     "CHINA PROBES SHANGHAI CHIEF CHEN JINING",
     "The Politburo member is the 4th top leader probed since 2025. "
     "Shanghai pledged loyalty Wed.",
     "CONFIRMED", 31.2, 121.5, "skyline"),
    (12, "HONIARA", "PACIFIC",
     "SOLOMONS PICK AUSTRALIA, BAR ANY FOREIGN BASE",
     "Treaty signed in Canberra on Wednesday: Australia is the primary "
     "security partner. $740m/10 yrs.",
     "CONFIRMED", -9.4, 160.0, "island"),
    (13, "LAUSANNE", "AFRICA",
     "SENEGAL GET THEIR AFRICA CUP BACK",
     "CAS ruled on Tuesday: the referee could restart the January final, "
     "so the 1\u20130 win stands.",
     "CONFIRMED", 14.7, -17.4, "trophy"),
]

BRIEFS = [
    (14, "WASHINGTON", "AMERICAS",
     "USTR poised to unveil Section 301 findings on 16 economies; 15% caps "
     "for EU, Japan, Korea. (REPORTED)"),
    (15, "WASHINGTON", "MIDDLE EAST",
     "US weighing strikes on senior Iranian leaders, incl. Mojtaba Khamenei, "
     "NBC reports. No decision made. (REPORTED)"),
    (16, "KYIV", "EUROPE",
     "Zelensky: Ukraine needs \u20ac115bn in 2027; \u20ac90bn secured, \u20ac25bn "
     "to find. About 60 Patriots held up."),
    (17, "CANBERRA", "PACIFIC",
     "Australia\u2019s October inflation: 4.9%, released Wednesday. Reserve "
     "Bank cash rate now 4.85%."),
    (18, "LONDON", "EUROPE",
     "Ofgem: energy cap up 26% from January. Typical bill \u00a31,723 to "
     "\u00a32,166 (+\u00a3443). \u00a3100 help from 4 Jan."),
    (19, "DHAKA", "ASIA",
     "Garment wage up 36%: 12,500 to 17,000 taka, 4\u20132 board vote. Workers "
     "wanted 18,000; protests continue."),
    (20, "DAMAZIN", "AFRICA",
     "RSF drone strikes Tuesday night killed 19 civilians, wounded 20 in "
     "Blue Nile, a rights group says."),
    (21, "BOGOR", "ASIA",
     "Three bodies recovered Wednesday from a flooded illegal gold mine; 23 "
     "still trapped of 26."),
    (22, "HANOI", "ASIA",
     "Gas blast at a hotpot eatery Tuesday: 7 dead, 9 hurt; 125 households "
     "evacuated. (First count: 6.)"),
    (23, "RAS AL KHAIMAH", "MIDDLE EAST",
     "Bus hit a parked truck about 01:00 Tuesday: 13 dead, 14 taken to "
     "hospital. Bus carried 41."),
    (24, "ESKISEHIR", "EUROPE",
     "Air Force AS-532 crashed on a Tuesday training flight; all 5 crew "
     "died. Second such crash in 12 days."),
    (25, "WASHINGTON", "AMERICAS",
     "Hackers breached the CIA/ODNI unclassified analysis system, NYT "
     "reports. An AI tool is suspected. (REPORTED)"),
    (26, "MADRID", "EUROPE",
     "Abrego Garcia left the US Tuesday, landed in Madrid Wednesday "
     "morning. Lawyer: \u201ca free man\u201d."),
    (27, "PYONGYANG", "ASIA",
     "North Korea expelled the Swiss envoy Wednesday, 48 hours to leave, "
     "over sanctions on a camp."),
    (28, "IOWA", "AMERICAS",
     "Army to detonate about 5 tons of lead azide (68 drums) at 09:00 CT "
     "today (15:00 UTC). (SCHEDULED)"),
    (29, "MADRID", "EUROPE",
     "Champions League, Tuesday: Real Madrid 5\u20131 PSV; Arsenal 1\u20131 "
     "Dortmund; Man City 2\u20132 Napoli."),
    (30, "DOHA", "MIDDLE EAST",
     "Sooryavanshi, 15, hit 204 off 53 balls, 28 sixes \u2014 fastest List A "
     "double century (52 balls)."),
    (31, "LONDON", "EUROPE",
     "UKHSA: 5,258 heat-linked deaths in England this summer, a record "
     "since 2016. Provisional."),
    (32, "LAGOS", "AFRICA",
     "Dangote refinery IPO, $1.6bn, values it at $48bn. Listing 1 December; "
     "Africa\u2019s biggest firm."),
]

NUMBERS = [
    ("2", "TANKERS HIT", "HORMUZ, TODAY"),
    ("\u22122.8%", "NIKKEI 225", "TOKYO, TODAY"),
    ("\u221214.8%", "SOFTBANK", "TOKYO, TODAY"),
    ("\u22126.2%", "KOSPI", "SEOUL, TODAY"),
    ("20", "HOSTAGES FREED", "CARTAGENA, TODAY"),
    ("~17 HRS", "SIEGE", "CARTAGENA, TODAY"),
    ("11", "HURT IN STRIKE", "RIYADH, TODAY"),
    ("490,334", "REGISTERED DEAD", "TOTAL, LEAKED ROSSTAT"),
]

HOURS = [
    ("00:18", "SHENZHOU-24 LIFTS OFF, JIUQUAN"),
    ("03:56", "DOCKS AT TIANGONG, 3.5 HRS ON"),
    ("06:00", "CARTAGENA RAID FREES 20 (01:00 LOCAL)"),
    ("07:10", "CAS HANDS SENEGAL ITS TITLE BACK"),
    ("07:28", "DANGOTE IPO PRICED AT $48BN"),
    ("07:30", "BRENT $89.93 AS OIL SLIDES, LONDON"),
    ("09:23", "PYONGYANG EXPELS SWISS ENVOY"),
]

ALL = LEADS + GRID + BRIEFS


# ---------------------------------------------------------------- helpers

def wrap(text, font, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if font.getlength(trial) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(d, x, y, lines, font, fill, leading=None):
    if leading is None:
        leading = font.size + 3
    for ln in lines:
        d.text((x, y), ln, font=font, fill=fill)
        y += leading
    return y


def tag_chip(d, x, y, tag):
    fill = TAG_FILL.get(tag, NAVY)
    f = f_sans_b(10)
    w = int(f.getlength(tag)) + 12
    d.rounded_rectangle([x, y, x + w, y + 15], radius=3, fill=fill)
    d.text((x + 6, y + 2), tag, font=f, fill=(255, 255, 255))
    return w


def frame(d, x, y, w, h, edge=(200, 194, 178)):
    d.rectangle([x, y, x + w, y + h], outline=edge, width=1)


# ---------------------------------------------------------------- pictures
# Each routine draws a small flat scene inside (x, y, w, h).

def ill_tanker(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=SEA)
    d.rectangle([x, y + int(h * 0.62), x + w, y + h], fill=(30, 68, 96))
    d.polygon([(x + 8, y + int(h * 0.62)), (x + int(w * 0.42), y + int(h * 0.62)),
               (x + int(w * 0.36), y + int(h * 0.42)), (x + int(w * 0.16), y + int(h * 0.42))],
              fill=(150, 40, 30))
    d.rectangle([x + int(w * 0.55), y + int(h * 0.48), x + int(w * 0.62), y + int(h * 0.62)],
                fill=(220, 220, 210))
    d.rectangle([x + int(w * 0.66), y + int(h * 0.55), x + int(w * 0.86), y + int(h * 0.62)],
                fill=(60, 60, 60))
    for cx, cy, r in [(int(w * 0.72), int(h * 0.28), 9), (int(w * 0.80), int(h * 0.20), 7)]:
        d.ellipse([x + cx - r, y + cy - r, x + cx + r, y + cy + r], fill=(240, 140, 30))
    d.ellipse([x + int(w * 0.30), y + int(h * 0.72), x + int(w * 0.30) + 8,
               y + int(h * 0.72) + 8], outline=(230, 230, 220), width=2)
    d.line([x + int(w * 0.30) + 4, y + int(h * 0.72) + 8, x + int(w * 0.30) + 4,
            y + int(h * 0.72) + 14], fill=(230, 230, 220), width=2)


def ill_court(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(214, 206, 188))
    d.polygon([(x + int(w * 0.08), y + int(h * 0.38)), (x + int(w * 0.92), y + int(h * 0.38)),
               (x + int(w * 0.5), y + int(h * 0.12))], fill=(120, 40, 35))
    for i in range(5):
        cx = x + int(w * (0.14 + i * 0.18))
        d.rectangle([cx, y + int(h * 0.40), cx + 7, y + int(h * 0.82)], fill=(240, 238, 228))
    d.rectangle([x + int(w * 0.06), y + int(h * 0.82), x + int(w * 0.94), y + int(h * 0.90)],
                fill=(60, 56, 48))
    d.line([x + int(w * 0.42), y + int(h * 0.30), x + int(w * 0.42), y + int(h * 0.10)],
           fill=INK, width=2)
    d.line([x + int(w * 0.34), y + int(h * 0.12), x + int(w * 0.50), y + int(h * 0.12)],
           fill=INK, width=2)


def ill_chart(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(232, 236, 240))
    for i in range(4):
        gy = y + int(h * (0.22 + i * 0.18))
        d.line([x + 6, gy, x + w - 6, gy], fill=(200, 206, 212), width=1)
    pts = [(0.06, 0.22), (0.22, 0.30), (0.38, 0.26), (0.55, 0.48), (0.72, 0.62),
           (0.88, 0.82)]
    coords = [(x + int(px * w), y + int(py * h)) for px, py in pts]
    d.line(coords, fill=RED, width=3)
    for cx, cy in coords:
        d.ellipse([cx - 3, cy - 3, cx + 3, cy + 3], fill=RED)
    d.text((x + int(w * 0.60), y + int(h * 0.06)), "\u221214.8%", font=f_sans_b(13),
           fill=RED)


def ill_rocket(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(18, 28, 52))
    for sx, sy in [(0.15, 0.15), (0.8, 0.1), (0.6, 0.3), (0.3, 0.08), (0.9, 0.45)]:
        d.ellipse([x + int(sx * w) - 1, y + int(sy * h) - 1, x + int(sx * w) + 1,
                   y + int(sy * h) + 1], fill=(255, 255, 255))
    cx = x + int(w * 0.5)
    d.polygon([(cx, y + int(h * 0.10)), (cx + 9, y + int(h * 0.30)), (cx - 9, y + int(h * 0.30))],
              fill=RED)
    d.rectangle([cx - 9, y + int(h * 0.30), cx + 9, y + int(h * 0.62)], fill=(235, 235, 228))
    d.rectangle([cx - 16, y + int(h * 0.52), cx - 9, y + int(h * 0.66)], fill=RED)
    d.rectangle([cx + 9, y + int(h * 0.52), cx + 16, y + int(h * 0.66)], fill=RED)
    d.polygon([(cx - 6, y + int(h * 0.62)), (cx + 6, y + int(h * 0.62)),
               (cx + 12, y + int(h * 0.88)), (cx - 12, y + int(h * 0.88))],
              fill=(240, 140, 30))
    d.ellipse([x + int(w * 0.82), y + int(h * 0.62), x + int(w * 0.82) + 16,
               y + int(h * 0.62) + 16], outline=(200, 200, 190), width=2)


def ill_store(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(226, 232, 238))
    d.rectangle([x + int(w * 0.08), y + int(h * 0.30), x + int(w * 0.92), y + int(h * 0.88)],
                fill=(240, 200, 60))
    d.rectangle([x + int(w * 0.08), y + int(h * 0.30), x + int(w * 0.92), y + int(h * 0.46)],
                fill=NAVY)
    d.text((x + int(w * 0.30), y + int(h * 0.33)), "MARKET", font=f_sans_b(11),
           fill=(255, 255, 255))
    d.rectangle([x + int(w * 0.16), y + int(h * 0.56), x + int(w * 0.30), y + int(h * 0.88)],
                fill=(90, 60, 40))
    d.rectangle([x + int(w * 0.38), y + int(h * 0.56), x + int(w * 0.62), y + int(h * 0.80)],
                fill=(180, 220, 235))
    d.rectangle([x + int(w * 0.70), y + int(h * 0.56), x + int(w * 0.86), y + int(h * 0.80)],
                fill=(180, 220, 235))
    for px, py in [(0.20, 0.14), (0.45, 0.10), (0.72, 0.16)]:
        d.ellipse([x + int(px * w) - 3, y + int(py * h) - 3, x + int(px * w) + 3,
                   y + int(py * h) + 3], fill=(255, 255, 255))


def ill_ship(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(200, 216, 228))
    d.rectangle([x, y + int(h * 0.68), x + w, y + h], fill=(52, 96, 130))
    d.polygon([(x + 10, y + int(h * 0.68)), (x + int(w * 0.85), y + int(h * 0.68)),
               (x + int(w * 0.78), y + int(h * 0.50)), (x + int(w * 0.18), y + int(h * 0.50))],
              fill=(70, 70, 72))
    d.rectangle([x + int(w * 0.30), y + int(h * 0.34), x + int(w * 0.44), y + int(h * 0.50)],
                fill=(220, 220, 210))
    d.rectangle([x + int(w * 0.55), y + int(h * 0.40), x + int(w * 0.62), y + int(h * 0.50)],
                fill=(220, 220, 210))
    for fx, fy, r in [(0.68, 0.30, 8), (0.76, 0.22, 6)]:
        d.ellipse([x + int(fx * w) - r, y + int(fy * h) - r, x + int(fx * w) + r,
                   y + int(fy * h) + r], fill=(240, 140, 30))
    d.polygon([(x + int(w * 0.82), y + int(h * 0.16)), (x + int(w * 0.90), y + int(h * 0.16)),
               (x + int(w * 0.86), y + int(h * 0.34))], fill=(90, 90, 90))


def ill_tower(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(24, 34, 56))
    d.rectangle([x + int(w * 0.30), y + int(h * 0.18), x + int(w * 0.55), y + int(h * 0.92)],
                fill=(150, 170, 195))
    d.rectangle([x + int(w * 0.60), y + int(h * 0.34), x + int(w * 0.80), y + int(h * 0.92)],
                fill=(110, 130, 155))
    for r in range(6):
        yy = y + int(h * (0.24 + r * 0.11))
        d.line([x + int(w * 0.32), yy, x + int(w * 0.53), yy], fill=(240, 200, 80), width=2)
    d.ellipse([x + int(w * 0.66), y + int(h * 0.10), x + int(w * 0.66) + 12,
               y + int(h * 0.10) + 12], fill=(240, 140, 30))
    d.polygon([(x + int(w * 0.66) + 6, y + int(h * 0.10) + 12),
               (x + int(w * 0.58), y + int(h * 0.34)), (x + int(w * 0.74), y + int(h * 0.34))],
              fill=(240, 140, 30))


def ill_ledger(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(228, 222, 205))
    d.rectangle([x + int(w * 0.18), y + int(h * 0.12), x + int(w * 0.82), y + int(h * 0.88)],
                fill=(252, 250, 244), outline=(120, 110, 90), width=2)
    for i in range(5):
        yy = y + int(h * (0.28 + i * 0.13))
        d.line([x + int(w * 0.26), yy, x + int(w * 0.74), yy], fill=(150, 145, 130), width=2)
    d.rectangle([x + int(w * 0.66), y + int(h * 0.62), x + int(w * 0.78), y + int(h * 0.78)],
                fill=RED)
    d.text((x + int(w * 0.685), y + int(h * 0.64)), "?", font=f_sans_b(12),
           fill=(255, 255, 255))


def ill_city(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(216, 196, 160))
    for i, (bx, bw, bh) in enumerate([(0.06, 0.16, 0.55), (0.26, 0.14, 0.72),
                                      (0.44, 0.18, 0.48), (0.66, 0.14, 0.64),
                                      (0.84, 0.12, 0.42)]):
        d.rectangle([x + int(bx * w), y + int(h * (0.92 - bh)), x + int((bx + bw) * w),
                     y + int(h * 0.92)], fill=(90, 80, 70))
    d.ellipse([x + int(w * 0.70), y + int(h * 0.10), x + int(w * 0.70) + 14,
               y + int(h * 0.10) + 14], fill=(240, 140, 30))
    d.rectangle([x, y + int(h * 0.92), x + w, y + h], fill=(70, 62, 54))


def ill_drone(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(188, 204, 220))
    d.rectangle([x, y + int(h * 0.70), x + w, y + h], fill=(120, 140, 110))
    cx, cy = x + int(w * 0.5), y + int(h * 0.38)
    d.rectangle([cx - 12, cy - 6, cx + 12, cy + 6], fill=(50, 50, 55))
    for dx, dy in [(-18, -10), (18, -10), (-18, 10), (18, 10)]:
        d.line([cx + dx, cy + dy, cx + dx + (6 if dx > 0 else -6), cy + dy],
               fill=(80, 80, 85), width=3)
    d.ellipse([cx - 22, cy - 16, cx - 8, cy - 8], outline=(80, 80, 85), width=2)
    d.ellipse([cx + 8, cy - 16, cx + 22, cy - 8], outline=(80, 80, 85), width=2)
    d.line([x + int(w * 0.10), y + int(h * 0.86), x + int(w * 0.90), y + int(h * 0.86)],
           fill=RED, width=3)


def ill_skyline(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(206, 214, 226))
    for bx, bw, bh in [(0.04, 0.14, 0.5), (0.22, 0.12, 0.68), (0.38, 0.16, 0.58),
                        (0.58, 0.12, 0.76), (0.74, 0.14, 0.46)]:
        d.rectangle([x + int(bx * w), y + int(h * (0.92 - bh)), x + int((bx + bw) * w),
                     y + int(h * 0.92)], fill=(60, 70, 90))
    d.rectangle([x + int(w * 0.60), y + int(h * 0.10), x + int(w * 0.62) + 3,
                 y + int(h * 0.24)], fill=RED)
    d.ellipse([x + int(w * 0.80), y + int(h * 0.10), x + int(w * 0.80) + 12,
               y + int(h * 0.10) + 12], fill=(240, 200, 60))
    d.rectangle([x, y + int(h * 0.92), x + w, y + h], fill=(50, 56, 66))


def ill_island(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(120, 180, 205))
    d.ellipse([x + int(w * 0.14), y + int(h * 0.42), x + int(w * 0.86), y + int(h * 0.86)],
              fill=(110, 170, 110))
    d.polygon([(x + int(w * 0.40), y + int(h * 0.50)), (x + int(w * 0.50), y + int(h * 0.22)),
               (x + int(w * 0.60), y + int(h * 0.50))], fill=(60, 120, 70))
    d.line([x + int(w * 0.50), y + int(h * 0.22), x + int(w * 0.50), y + int(h * 0.50)],
           fill=(120, 90, 50), width=2)
    d.rectangle([x + int(w * 0.50), y + int(h * 0.22), x + int(w * 0.66), y + int(h * 0.30)],
                fill=(200, 40, 40))
    d.ellipse([x + int(w * 0.78), y + int(h * 0.12), x + int(w * 0.78) + 12,
               y + int(h * 0.12) + 12], fill=(250, 220, 90))


def ill_trophy(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(40, 110, 60))
    d.rectangle([x + int(w * 0.42), y + int(h * 0.18), x + int(w * 0.58), y + int(h * 0.52)],
                fill=(240, 200, 60))
    d.polygon([(x + int(w * 0.42), y + int(h * 0.18)), (x + int(w * 0.58), y + int(h * 0.18)),
               (x + int(w * 0.50), y + int(h * 0.10))], fill=(240, 200, 60))
    d.ellipse([x + int(w * 0.34), y + int(h * 0.22), x + int(w * 0.44), y + int(h * 0.38)],
              outline=(240, 200, 60), width=3)
    d.ellipse([x + int(w * 0.56), y + int(h * 0.22), x + int(w * 0.66), y + int(h * 0.38)],
              outline=(240, 200, 60), width=3)
    d.rectangle([x + int(w * 0.46), y + int(h * 0.52), x + int(w * 0.54), y + int(h * 0.66)],
                fill=(240, 200, 60))
    d.rectangle([x + int(w * 0.38), y + int(h * 0.66), x + int(w * 0.62), y + int(h * 0.72)],
                fill=(240, 200, 60))
    d.ellipse([x + int(w * 0.12), y + int(h * 0.66), x + int(w * 0.12) + 20,
               y + int(h * 0.66) + 20], fill=(245, 245, 240))
    d.ellipse([x + int(w * 0.12), y + int(h * 0.66), x + int(w * 0.12) + 20,
               y + int(h * 0.66) + 20], outline=INK, width=1)


# One registry line per illustration, so the picture count is machine-readable.
ILL = {"tanker": ill_tanker,
       "court": ill_court,
       "chart": ill_chart,
       "rocket": ill_rocket,
       "store": ill_store,
       "ship": ill_ship,
       "tower": ill_tower,
       "ledger": ill_ledger,
       "city": ill_city,
       "drone": ill_drone,
       "skyline": ill_skyline,
       "island": ill_island,
       "trophy": ill_trophy,}


# ---------------------------------------------------------------- world map
# Coarse hand-drawn continent outlines in (lon, lat), simplified on purpose.

CONTINENTS = {
    "na": [(-168, 66), (-140, 70), (-125, 71), (-110, 68), (-95, 69), (-85, 66),
           (-80, 73), (-65, 60), (-55, 52), (-60, 47), (-70, 42), (-75, 35),
           (-80, 32), (-85, 30), (-90, 21), (-95, 19), (-97, 16), (-92, 15),
           (-86, 12), (-83, 9), (-80, 9), (-85, 12), (-90, 14), (-95, 16),
           (-100, 18), (-105, 20), (-110, 24), (-115, 29), (-120, 34),
           (-125, 40), (-125, 49), (-130, 55), (-140, 60), (-155, 58),
           (-165, 60)],
    "sa": [(-80, 9), (-77, 4), (-80, -3), (-81, -6), (-77, -12), (-72, -18),
           (-70, -23), (-70, -30), (-72, -37), (-73, -44), (-70, -52),
           (-68, -55), (-65, -50), (-62, -41), (-58, -35), (-52, -32),
           (-48, -28), (-41, -23), (-35, -9), (-35, -6), (-40, -3), (-44, -2),
           (-50, 0), (-55, 6), (-60, 8), (-65, 10), (-70, 12), (-75, 10)],
    "af": [(-17, 15), (-16, 20), (-15, 27), (-10, 31), (-5, 35), (0, 36),
           (10, 37), (11, 34), (15, 32), (20, 32), (25, 32), (30, 31),
           (32, 31), (35, 28), (37, 22), (39, 18), (41, 12), (43, 11),
           (48, 11), (51, 12), (48, 5), (42, 0), (40, -5), (40, -12),
           (36, -18), (33, -26), (28, -33), (20, -35), (17, -32), (15, -27),
           (13, -18), (12, -10), (9, -1), (9, 4), (4, 6), (-3, 5), (-8, 5),
           (-13, 8)],
    "eu": [(-10, 36), (-9, 43), (-2, 48), (0, 51), (4, 53), (8, 55),
           (10, 57), (18, 56), (21, 59), (24, 60), (28, 62), (30, 66),
           (32, 70), (40, 68), (44, 68), (40, 64), (35, 62), (30, 60),
           (28, 58), (24, 58), (21, 55), (18, 54), (12, 54), (8, 54),
           (5, 53), (2, 51), (-2, 50), (-5, 48), (-2, 44), (-9, 43),
           (-10, 37)],
    "as": [(30, 36), (36, 36), (36, 33), (42, 32), (44, 29), (48, 30),
           (50, 29), (54, 27), (57, 26), (60, 25), (62, 25), (66, 25),
           (68, 23), (72, 20), (76, 18), (80, 16), (80, 13), (77, 8),
           (80, 7), (84, 10), (88, 15), (91, 22), (93, 18), (95, 16),
           (98, 16), (100, 14), (103, 10), (105, 9), (107, 11), (109, 13),
           (109, 18), (106, 20), (108, 21), (110, 20), (114, 22), (118, 25),
           (120, 28), (122, 30), (120, 32), (122, 35), (124, 38), (126, 40),
           (128, 38), (130, 42), (132, 43), (135, 44), (138, 46), (140, 48),
           (142, 50), (142, 53), (140, 55), (138, 58), (135, 60), (140, 62),
           (150, 60), (158, 58), (160, 60), (162, 62), (170, 66), (178, 65),
           (178, 68), (170, 66), (162, 64), (158, 60), (155, 55), (150, 50),
           (142, 45), (140, 40), (135, 35), (130, 33), (127, 35), (126, 38),
           (122, 39), (120, 35), (118, 30), (115, 25), (110, 20), (105, 15),
           (100, 10), (98, 8), (95, 15), (92, 20), (88, 22), (85, 19),
           (80, 15), (76, 10), (73, 16), (70, 20), (66, 25), (61, 25),
           (57, 27), (53, 27), (50, 29), (48, 30), (44, 29), (40, 30),
           (36, 36), (33, 36)],
    "au": [(113, -22), (114, -30), (115, -35), (118, -35), (124, -33),
           (129, -32), (132, -32), (135, -35), (138, -35), (140, -38),
           (145, -38), (150, -37), (153, -32), (153, -27), (150, -23),
           (146, -19), (142, -15), (142, -11), (137, -12), (135, -15),
           (132, -12), (130, -13), (126, -14), (122, -17), (118, -20)],
    "gl": [(-45, 60), (-40, 64), (-32, 68), (-25, 70), (-20, 72), (-22, 76),
           (-30, 80), (-45, 80), (-55, 76), (-58, 70), (-55, 64), (-50, 60)],
    "uk": [(-5, 50), (-3, 53), (-5, 56), (-3, 58), (0, 53), (1, 51)],
    "jp": [(130, 31), (132, 33), (135, 34), (137, 35), (139, 37), (140, 39),
           (141, 41), (142, 43), (144, 44), (141, 40), (139, 36), (136, 34),
           (133, 34), (131, 32)],
    "nz": [(167, -45), (170, -43), (173, -41), (175, -38), (177, -38),
           (174, -40), (171, -42), (168, -46)],
}

# Small nudges so clustered pins stay readable (story num -> (lon, lat)).
PIN_POS = {13: (-17.4, 14.7), 14: (-78.5, 40.0), 15: (-76.0, 37.8),
           25: (-77.8, 38.2), 26: (-3.7, 40.4), 29: (-4.6, 41.3),
           31: (1.5, 52.8), 18: (-0.1, 51.5)}


# Positions for the brief stories, which carry no coordinates of their own:
# story num -> (lat, lon).
BRIEF_POS = {14: (38.9, -77.0), 15: (38.9, -77.0), 16: (50.4, 30.5),
             17: (-35.3, 149.1), 18: (51.5, -0.1), 19: (23.8, 90.4),
             20: (11.8, 34.4), 21: (-6.6, 106.8), 22: (21.0, 105.8),
             23: (25.8, 55.9), 24: (39.8, 30.5), 25: (38.9, -77.0),
             26: (40.4, -3.7), 27: (39.0, 125.8), 28: (41.9, -93.1),
             29: (40.4, -3.7), 30: (25.3, 51.5), 31: (51.5, -0.1),
             32: (6.5, 3.4)}


def draw_map(d, mx, my, mw, mh):
    d.rectangle([mx, my, mx + mw, my + mh], fill=(214, 228, 238))
    scale = min(mw / 360.0, mh / 130.0)
    ox = mx + (mw - 360 * scale) / 2
    oy = my + (mh - 130 * scale) / 2

    def proj(lon, lat):
        return (ox + (lon + 180) * scale, oy + (80 - lat) * scale)

    for pts in CONTINENTS.values():
        d.polygon([proj(lon, lat) for lon, lat in pts], fill=LAND,
                  outline=(150, 158, 132))
    d.text((mx + 6, my + 4), "WHERE IT HAPPENED \u2014 32 STORIES PINNED",
           font=f_sans_b(11), fill=NAVY)
    placed = 0
    for item in ALL:
        num = item[0]
        if len(item) == 9:
            lat, lon = item[6], item[7]
        else:
            lat, lon = BRIEF_POS[num]
        plon, plat = PIN_POS.get(num, (lon, lat))
        px, py = proj(plon, plat)
        r = 8
        d.ellipse([px - r, py - r, px + r, py + r], fill=RED,
                  outline=(255, 255, 255), width=1)
        t = str(num)
        tw = f_sans_b(8).getlength(t)
        d.text((px - tw / 2, py - 5), t, font=f_sans_b(8), fill=(255, 255, 255))
        placed += 1
    return placed


# ---------------------------------------------------------------- layout

def draw():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- masthead
    d.text((12, 6), "The Wednesday Globe", font=f_serif_b(44), fill=INK)
    d.line([12, 62, 1012, 62], fill=RULE, width=2)
    d.text((12, 68), "WEDNESDAY 25 NOVEMBER 2026  \u00b7  32 STORIES  \u00b7  13 PICTURED  \u00b7  "
                     "PRESS " + PRESS + "  \u00b7  ONE DAY. ONE PAGE.",
           font=f_sans_b(12), fill=INK)

    # ---- three leads
    lead_xs = [12, 344, 676]
    lead_ws = [324, 324, 336]
    ly, lh = 84, 228
    for (num, city, region, headline, deck, tag, lat, lon, art), lx, lw in \
            zip(LEADS, lead_xs, lead_ws):
        d.rectangle([lx, ly, lx + lw, ly + lh], fill=PANEL_BG, outline=(200, 194, 178))
        d.rectangle([lx, ly, lx + lw, ly + 20], fill=NAVY)
        d.text((lx + 8, ly + 4), "LEAD %d \u00b7 %s" % (num, city), font=f_sans_b(11),
               fill=(255, 255, 255))
        chip_w = int(f_sans_b(10).getlength(tag)) + 12
        tag_chip(d, lx + lw - 8 - chip_w, ly + 2, tag)
        ILL[art](d, lx + 8, ly + 26, lw - 16, 68)
        yy = ly + 98
        yy = text_block(d, lx + 8, yy, wrap(headline, f_serif_b(20), lw - 16),
                        f_serif_b(20), INK, leading=23)
        text_block(d, lx + 8, yy + 4, wrap(deck, f_sans(11.5), lw - 16),
                   f_sans(11.5), (50, 48, 42), leading=14)

    # ---- day in numbers
    ny, nh = 316, 56
    d.rectangle([12, ny, 1012, ny + nh], fill=NAVY)
    d.text((20, ny + 4), "DAY IN NUMBERS", font=f_sans_b(11), fill=(200, 210, 230))
    cw = (1012 - 12 - 150) / len(NUMBERS)
    for i, (big, label, when) in enumerate(NUMBERS):
        cx = 12 + 150 + i * cw
        if i > 0:
            d.line([cx, ny + 8, cx, ny + nh - 8], fill=(70, 92, 128), width=1)
        d.text((cx + 6, ny + 4), big, font=f_sans_b(19), fill=(255, 255, 255))
        d.text((cx + 6, ny + 27), label, font=f_sans_b(9), fill=(200, 210, 230))
        d.text((cx + 6, ny + 40), when, font=f_sans(8), fill=(160, 175, 200))

    # ---- pictured grid, 10 panels in 2 rows x 5
    gy, gh = 376, 252
    gw = (1012 - 12 - 4 * 8) / 5
    for idx, (num, city, region, headline, deck, tag, lat, lon, art) in enumerate(GRID):
        row, col = divmod(idx, 5)
        gx = 12 + col * (gw + 8)
        gy2 = gy + row * (gh / 2 + 8)
        ph = gh / 2 - 4
        d.rectangle([gx, gy2, gx + gw, gy2 + ph], fill=PANEL_BG,
                    outline=(200, 194, 178))
        ILL[art](d, gx + 6, gy2 + 5, gw - 12, 40)
        yy = gy2 + 47
        d.text((gx + 6, yy), "%d \u00b7 %s" % (num, city), font=f_sans_b(10), fill=RED)
        yy += 12
        yy = text_block(d, gx + 6, yy, wrap(headline, f_sans_b(12), gw - 12),
                        f_sans_b(12), INK, leading=14)
        text_block(d, gx + 6, yy + 2, wrap(deck, f_sans(10), gw - 12)[:3],
                   f_sans(10), (50, 48, 42), leading=11)

    # ---- briefs, 4 columns
    by = 638
    d.text((12, by), "THE REST OF THE DAY", font=f_sans_b(12), fill=NAVY)
    d.line([12, by + 16, 1012, by + 16], fill=RULE, width=1)
    cols = [BRIEFS[i::4] for i in range(4)]
    col_xs = [12, 262, 512, 762]
    col_ws = [242, 242, 242, 250]
    row_h = 37
    for col_items, cx, cw2 in zip(cols, col_xs, col_ws):
        for j, (num, city, region, text, *_) in enumerate(col_items):
            yy = by + 22 + j * row_h
            d.text((cx, yy), "%d" % num, font=f_sans_b(10), fill=RED)
            lines = wrap(city + " \u2014 " + text, f_sans(10), cw2 - 18)
            text_block(d, cx + 18, yy, lines[:3], f_sans(10), (50, 48, 42),
                       leading=12)

    # ---- bottom band: map + hours + date check
    band_y = 850
    pins = draw_map(d, 12, band_y, 500, 162)
    # hours column
    hx = 524
    d.text((hx, band_y), "DAY IN HOURS (UTC)", font=f_sans_b(11), fill=NAVY)
    hy = band_y + 18
    for t, label in HOURS:
        d.text((hx, hy), t, font=f_sans_b(11), fill=RED)
        d.text((hx + 44, hy), label, font=f_sans(10), fill=INK)
        hy += 13
    tally = {}
    for _, _, region, *_ in ALL:
        tally[region] = tally.get(region, 0) + 1
    d.text((hx, hy + 4), "TALLY: EUROPE %d \u00b7 ASIA %d \u00b7 MIDDLE EAST %d" %
           (tally.get("EUROPE", 0), tally.get("ASIA", 0),
            tally.get("MIDDLE EAST", 0)), font=f_sans_b(10), fill=INK)
    d.text((hx, hy + 17), "AMERICAS %d \u00b7 AFRICA %d \u00b7 PACIFIC %d" %
           (tally.get("AMERICAS", 0), tally.get("AFRICA", 0),
            tally.get("PACIFIC", 0)), font=f_sans_b(10), fill=INK)
    d.text((hx, hy + 31), "TAGS: CONFIRMED = verified \u00b7 REPORTED = a claim",
           font=f_sans(9), fill=MUTED)
    d.text((hx, hy + 43), "CLAIM / LEAKED = unverified \u00b7 See SOURCES.md",
           font=f_sans(9), fill=MUTED)
    # date check box
    dx = 792
    d.rectangle([dx, band_y, 1012, band_y + 162], fill=(255, 252, 240),
                outline=RED, width=2)
    d.text((dx + 8, band_y + 6), "DATE CHECK", font=f_sans_b(12), fill=RED)
    dc = ("Every story on this page happened, or was first reported, on "
          "Wednesday 25 November 2026. Late-Tuesday events in the Americas "
          "are carried as Wednesday\u2019s news. LEFT OUT AS OTHER DAYS\u2019 "
          "NEWS: BepiColombo reached Mercury Sat 21 Nov; Venezuela\u2019s "
          "$237.5bn debt plan, Tue 24 Nov; US midterms decided 3\u201323 Nov; "
          "COP31 pact collapsed Sun 22 Nov; supermoon peaked Tue 24 Nov.")
    text_block(d, dx + 8, band_y + 24, wrap(dc, f_sans(9.5), 1012 - dx - 16),
               f_sans(9.5), INK, leading=12)

    d.text((12, 1016), "The Wednesday Globe \u2014 No. 1 \u00b7 All figures sourced; "
           "see SOURCES.md in this repo.", font=f_sans(9), fill=MUTED)
    img.save(OUT, optimize=True)
    total = len(ALL)
    assert total == 32, total
    assert sum(tally.values()) == 32
    assert pins == 32, pins
    print("stories=%d panels=%d pins=%d tally=%s" %
          (total, 3 + len(GRID), pins, tally))
    print("saved", OUT)


if __name__ == "__main__":
    draw()
