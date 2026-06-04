from __future__ import annotations

from html import escape
from pathlib import Path
import random


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "bear-mood-cycle.svg"


# Edit moods here later:
# - Add a new dictionary to include another mood.
# - Change "message" to update the text shown in the widget.
# - Change "accent" to adjust the neon color for that mood.
# Keep text short so it fits inside the GitHub README image.
MOODS = [
    {
        "name": "Happy",
        "message": "All systems feel bright today.",
        "accent": "#39d353",
        "eyes": "happy",
        "mouth": "smile",
    },
    {
        "name": "Focused",
        "message": "Deep work mode is online.",
        "accent": "#58a6ff",
        "eyes": "focused",
        "mouth": "flat",
    },
    {
        "name": "Sleepy",
        "message": "Recharge first, then build.",
        "accent": "#a78bfa",
        "eyes": "sleepy",
        "mouth": "sleep",
    },
    {
        "name": "Excited",
        "message": "A new idea just unlocked.",
        "accent": "#ffcc66",
        "eyes": "wide",
        "mouth": "open",
    },
    {
        "name": "Love It",
        "message": "This build has extra heart.",
        "accent": "#ff7bba",
        "eyes": "heart",
        "mouth": "smile",
    },
    {
        "name": "Debugging",
        "message": "Tracing the bug with patience.",
        "accent": "#f97316",
        "eyes": "focused",
        "mouth": "flat",
    },
    {
        "name": "Tired",
        "message": "Low battery, still learning.",
        "accent": "#8b949e",
        "eyes": "sleepy",
        "mouth": "flat",
    },
]


def eyes_svg(kind: str) -> str:
    if kind == "happy":
        return """
        <path d="M118 72q8 8 16 0" class="stroke dark-line"/>
        <path d="M156 72q8 8 16 0" class="stroke dark-line"/>
        """
    if kind == "focused":
        return """
        <rect x="115" y="67" width="22" height="5" rx="2" class="dark"/>
        <rect x="154" y="67" width="22" height="5" rx="2" class="dark"/>
        """
    if kind == "sleepy":
        return """
        <path d="M116 70h22" class="stroke dark-line"/>
        <path d="M154 70h22" class="stroke dark-line"/>
        """
    if kind == "heart":
        return """
        <path d="M111 64c0-8 12-8 12 0 0-8 12-8 12 0 0 10-12 15-12 15s-12-5-12-15z" fill="#ff7bba"/>
        <path d="M153 64c0-8 12-8 12 0 0-8 12-8 12 0 0 10-12 15-12 15s-12-5-12-15z" fill="#ff7bba"/>
        """
    return """
    <rect x="120" y="65" width="8" height="8" rx="2" class="dark"/>
    <rect x="162" y="65" width="8" height="8" rx="2" class="dark"/>
    """


def mouth_svg(kind: str) -> str:
    if kind == "smile":
        return '<path d="M126 99q20 16 40 0" class="stroke dark-line"/>'
    if kind == "open":
        return '<rect x="139" y="96" width="14" height="10" rx="5" class="dark"/>'
    if kind == "sleep":
        return '<path d="M132 100q14 8 28 0" class="stroke dark-line"/>'
    return '<path d="M132 101h28" class="stroke dark-line"/>'


def render_svg(mood: dict[str, str]) -> str:
    name = escape(mood["name"])
    message = escape(mood["message"])
    accent = mood["accent"]

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 210" role="img" aria-labelledby="title desc">
  <title id="title">Daily bear mood widget: {name}</title>
  <desc id="desc">A GitHub profile bear mood widget showing the current mood as {name}.</desc>
  <defs>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <style>
      .panel{{fill:#0d1117;stroke:#30363d;stroke-width:2}}
      .screen{{fill:#010409;stroke:{accent};stroke-width:2}}
      .txt{{font-family:Consolas,Monaco,monospace;fill:#c9d1d9}}
      .muted{{fill:#8b949e}}
      .accent{{fill:{accent}}}
      .accent-stroke{{stroke:{accent}}}
      .bear{{fill:#a66a3f}}
      .ear{{fill:#7a4328}}
      .muzzle{{fill:#e6c7a5}}
      .dark{{fill:#1f2328}}
      .stroke{{fill:none;stroke-linecap:round;stroke-linejoin:round;stroke-width:4}}
      .dark-line{{stroke:#1f2328}}
      .blink{{animation:blink 3s steps(1,end) infinite}}
      .float{{animation:float 3s ease-in-out infinite}}
      .spark{{animation:spark 1.8s steps(1,end) infinite}}
      .cursor{{animation:cursor 1s steps(1,end) infinite}}
      @keyframes blink{{0%,88%,100%{{opacity:1}}89%,94%{{opacity:.08}}}}
      @keyframes float{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-4px)}}}}
      @keyframes spark{{0%,100%{{opacity:.28}}50%{{opacity:1}}}}
      @keyframes cursor{{0%,48%{{opacity:1}}49%,100%{{opacity:0}}}}
    </style>
  </defs>

  <rect x="8" y="8" width="744" height="194" rx="16" class="panel"/>
  <rect x="26" y="28" width="708" height="154" rx="12" class="screen" filter="url(#glow)"/>

  <g transform="translate(68 38)">
    <g class="float">
      <circle cx="145" cy="72" r="48" class="bear"/>
      <circle cx="108" cy="36" r="18" class="bear"/>
      <circle cx="182" cy="36" r="18" class="bear"/>
      <circle cx="108" cy="36" r="9" class="ear"/>
      <circle cx="182" cy="36" r="9" class="ear"/>
      <ellipse cx="145" cy="91" rx="28" ry="20" class="muzzle"/>
      <g class="blink">
        {eyes_svg(mood["eyes"])}
      </g>
      <rect x="141" y="85" width="9" height="7" rx="3" class="dark"/>
      {mouth_svg(mood["mouth"])}
      <rect x="105" y="119" width="90" height="38" rx="10" class="bear"/>
      <rect x="188" y="130" width="34" height="14" rx="7" class="bear"/>
    </g>
  </g>

  <g transform="translate(330 60)">
    <text class="txt muted" x="0" y="0" font-size="14">DAILY BEAR MOOD</text>
    <text class="txt" x="0" y="42" font-size="34" font-weight="700">{name}</text>
    <text class="txt muted" x="0" y="78" font-size="16">{message}</text>
    <text class="txt" x="0" y="118" font-size="15">&gt; generated by GitHub Actions<tspan class="cursor">_</tspan></text>
  </g>

  <rect class="accent spark" x="668" y="44" width="8" height="8"/>
  <rect class="accent spark" x="694" y="72" width="8" height="8"/>
  <rect class="accent spark" x="650" y="132" width="8" height="8"/>
  <path d="M54 170h150M216 170h24M574 170h88" class="stroke accent-stroke" opacity=".5"/>
</svg>
"""


def main() -> None:
    mood = random.SystemRandom().choice(MOODS)
    svg = render_svg(mood)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    previous = OUTPUT.read_text(encoding="utf-8") if OUTPUT.exists() else None
    if previous == svg:
        print(f"Bear mood unchanged: {mood['name']}")
        return

    OUTPUT.write_text(svg, encoding="utf-8", newline="\n")
    print(f"Bear mood updated: {mood['name']}")


if __name__ == "__main__":
    main()
