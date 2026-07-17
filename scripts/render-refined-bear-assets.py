from __future__ import annotations

import base64
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
AVATAR = ASSETS / "avatar-bear.png"


def avatar_data_uri() -> str:
    encoded = base64.b64encode(AVATAR.read_bytes()).decode("ascii")
    return f"data:image/png;base64,{encoded}"


def write(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8", newline="\n")
    print(f"rendered {path.relative_to(ROOT).as_posix()}")


def render_arcade_bear(avatar: str) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 220" role="img" aria-labelledby="title desc">
  <title id="title">Refined arcade coding bear banner</title>
  <desc id="desc">A polished cyber arcade banner using the real bear avatar as the main visual.</desc>
  <defs>
    <linearGradient id="panel" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#090f1a"/>
      <stop offset="0.5" stop-color="#101827"/>
      <stop offset="1" stop-color="#071b2c"/>
    </linearGradient>
    <radialGradient id="halo" cx="30%" cy="47%" r="42%">
      <stop offset="0" stop-color="#58a6ff" stop-opacity=".34"/>
      <stop offset="0.58" stop-color="#58a6ff" stop-opacity=".08"/>
      <stop offset="1" stop-color="#58a6ff" stop-opacity="0"/>
    </radialGradient>
    <filter id="glow" x="-25%" y="-25%" width="150%" height="150%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <clipPath id="avatarClip">
      <circle cx="154" cy="110" r="78"/>
    </clipPath>
    <style>
      .txt{{font-family:Consolas,Monaco,monospace;fill:#c9d1d9}}
      .muted{{fill:#8b949e}}
      .line{{stroke:#58a6ff;stroke-width:2;stroke-linecap:round;opacity:.72}}
      .grid{{stroke:#1f6feb;stroke-width:1;opacity:.16}}
      .spark{{animation:spark 1.8s steps(1,end) infinite}}
      .float{{animation:float 3.2s ease-in-out infinite}}
      .cursor{{animation:cursor 1s steps(1,end) infinite}}
      .scan{{animation:scan 4.5s linear infinite}}
      @keyframes spark{{0%,100%{{opacity:.25}}50%{{opacity:1}}}}
      @keyframes float{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-5px)}}}}
      @keyframes cursor{{0%,48%{{opacity:1}}49%,100%{{opacity:0}}}}
      @keyframes scan{{0%{{transform:translateX(-110px)}}100%{{transform:translateX(780px)}}}}
    </style>
  </defs>

  <rect x="8" y="8" width="744" height="204" rx="18" fill="url(#panel)" stroke="#30363d" stroke-width="2"/>
  <rect x="8" y="8" width="744" height="204" rx="18" fill="url(#halo)"/>
  <path class="grid" d="M34 42h692M34 78h692M34 114h692M34 150h692M34 186h692M70 26v188M122 26v188M174 26v188M226 26v188M278 26v188M330 26v188M382 26v188M434 26v188M486 26v188M538 26v188M590 26v188M642 26v188M694 26v188"/>
  <rect class="scan" x="0" y="10" width="95" height="200" fill="#58a6ff" opacity=".025"/>

  <g class="float">
    <circle cx="154" cy="110" r="88" fill="#0d1117" stroke="#58a6ff" stroke-width="2" filter="url(#glow)"/>
    <image href="{avatar}" x="76" y="32" width="156" height="156" clip-path="url(#avatarClip)" preserveAspectRatio="xMidYMid slice"/>
    <circle cx="154" cy="110" r="78" fill="none" stroke="#ffcc66" stroke-width="2" opacity=".72"/>
    <path d="M82 176c36 25 105 25 142 0" fill="none" stroke="#58a6ff" stroke-width="2" opacity=".42"/>
  </g>

  <g transform="translate(305 56)">
    <text class="txt" x="0" y="0" font-size="14" fill="#58a6ff">BEARCODER6 / RESEARCH LOG</text>
    <text class="txt" x="0" y="42" font-size="30" font-weight="700">YIXIANG YIN</text>
    <text class="txt muted" x="0" y="75" font-size="16">AI Agents / MLLMs / Machine Learning</text>
    <text class="txt" x="0" y="116" font-size="15">&gt; learn, build, iterate<tspan class="cursor">_</tspan></text>
    <path class="line" d="M0 138h150M166 138h26M210 138h128"/>
  </g>

  <path class="spark" d="M682 48h30M698 42v12" stroke="#58a6ff" stroke-width="2" stroke-linecap="round"/>
  <path d="M684 144h24" stroke="#58a6ff" stroke-width="2" stroke-linecap="round" opacity=".55"/>
</svg>
"""


def render_bear_terminal(avatar: str) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 620 170" role="img" aria-labelledby="title desc">
  <title id="title">Refined bear terminal companion</title>
  <desc id="desc">A cozy terminal card with the real bear avatar and blinking cyber UI details.</desc>
  <defs>
    <clipPath id="avatarClip"><circle cx="88" cy="84" r="52"/></clipPath>
    <filter id="glow" x="-25%" y="-25%" width="150%" height="150%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <style>
      .txt{{font-family:Consolas,Monaco,monospace;fill:#c9d1d9}}
      .muted{{fill:#8b949e}}
      .cursor{{animation:cursor 1s steps(1,end) infinite}}
      .pulse{{animation:pulse 1.8s ease-in-out infinite}}
      @keyframes cursor{{0%,48%{{opacity:1}}49%,100%{{opacity:0}}}}
      @keyframes pulse{{0%,100%{{opacity:.35}}50%{{opacity:1}}}}
    </style>
  </defs>
  <rect x="8" y="8" width="604" height="154" rx="18" fill="#0d1117" stroke="#30363d" stroke-width="2"/>
  <circle cx="88" cy="84" r="62" fill="#010409" stroke="#58a6ff" stroke-width="2" filter="url(#glow)"/>
  <image href="{avatar}" x="36" y="32" width="104" height="104" clip-path="url(#avatarClip)" preserveAspectRatio="xMidYMid slice"/>
  <circle cx="88" cy="84" r="52" fill="none" stroke="#ffcc66" stroke-width="2" opacity=".72"/>

  <rect x="170" y="32" width="410" height="104" rx="12" fill="#010409" stroke="#21262d"/>
  <text class="txt muted" x="190" y="58" font-size="13">bear@server-room ~</text>
  <text class="txt" x="190" y="84" font-size="14">$ ./study --topic agents</text>
  <text class="txt" x="190" y="109" font-size="14">&gt; reading papers</text>
  <text class="txt" x="190" y="132" font-size="14">&gt; building small demos<tspan class="cursor">_</tspan></text>
  <path class="pulse" d="M532 51h34M548 45v12" stroke="#58a6ff" stroke-width="2" stroke-linecap="round"/>
  <path d="M540 116h28" stroke="#58a6ff" stroke-width="2" stroke-linecap="round" opacity=".55"/>
</svg>
"""


def render_divider(avatar: str) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 86" role="img" aria-labelledby="title desc">
  <title id="title">Refined bear divider</title>
  <desc id="desc">A neon divider using the real bear avatar as a tiny centerpiece.</desc>
  <defs>
    <clipPath id="avatarClip"><circle cx="420" cy="43" r="28"/></clipPath>
    <style>
      .line{{stroke:#58a6ff;stroke-width:2;stroke-linecap:round;opacity:.55}}
      .spark{{animation:spark 1.6s steps(1,end) infinite}}
      @keyframes spark{{0%,100%{{opacity:.25}}50%{{opacity:1}}}}
    </style>
  </defs>
  <line x1="24" y1="43" x2="350" y2="43" class="line"/>
  <line x1="490" y1="43" x2="816" y2="43" class="line"/>
  <circle cx="420" cy="43" r="34" fill="#0d1117" stroke="#58a6ff" stroke-width="2"/>
  <image href="{avatar}" x="392" y="15" width="56" height="56" clip-path="url(#avatarClip)" preserveAspectRatio="xMidYMid slice"/>
  <circle cx="420" cy="43" r="28" fill="none" stroke="#ffcc66" stroke-width="1.5" opacity=".8"/>
  <text x="462" y="48" font-family="Consolas, Monaco, monospace" font-size="13" fill="#58a6ff">code / learn</text>
</svg>
"""


def main() -> None:
    avatar = avatar_data_uri()
    write(ASSETS / "arcade-bear.svg", render_arcade_bear(avatar))
    write(ASSETS / "bear-terminal.svg", render_bear_terminal(avatar))
    write(ASSETS / "tiny-bear-divider.svg", render_divider(avatar))


if __name__ == "__main__":
    main()
