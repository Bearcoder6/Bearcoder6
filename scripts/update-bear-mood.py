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
# - Change "expression" to one of: happy, focused, sleepy, excited, love, debugging, tired.
# Keep text short so it fits inside the GitHub README image.
MOODS = [
    {
        "name": "Happy",
        "message": "All systems feel bright today.",
        "accent": "#39d353",
        "expression": "happy",
    },
    {
        "name": "Focused",
        "message": "Deep work mode is online.",
        "accent": "#58a6ff",
        "expression": "focused",
    },
    {
        "name": "Sleepy",
        "message": "Recharge first, then build.",
        "accent": "#a78bfa",
        "expression": "sleepy",
    },
    {
        "name": "Excited",
        "message": "A new idea just unlocked.",
        "accent": "#ffcc66",
        "expression": "excited",
    },
    {
        "name": "Love It",
        "message": "This build has extra heart.",
        "accent": "#ff7bba",
        "expression": "love",
    },
    {
        "name": "Debugging",
        "message": "Tracing the bug with patience.",
        "accent": "#f97316",
        "expression": "debugging",
    },
    {
        "name": "Tired",
        "message": "Low battery, still learning.",
        "accent": "#8b949e",
        "expression": "tired",
    },
]


def expression_svg(kind: str) -> str:
    if kind == "happy":
        return """
        <path d="M82 78h8v8h-8zM122 78h8v8h-8z" class="ink"/>
        <path d="M87 105h8v8h8v6h16v-6h8v-8h8v8h-8v8h-8v6h-16v-6h-8v-8h-8z" class="ink"/>
        <rect x="58" y="96" width="12" height="8" class="blush"/>
        <rect x="142" y="96" width="12" height="8" class="blush"/>
        """
    if kind == "focused":
        return """
        <path d="M72 72h34v6H72zM116 72h34v6h-34z" class="ink"/>
        <path d="M83 84h10v10H83zM127 84h10v10h-10z" class="ink"/>
        <path d="M92 111h38v7H92z" class="ink"/>
        <rect x="146" y="120" width="36" height="22" class="screen"/>
        <rect x="152" y="126" width="12" height="4" class="green"/>
        <rect x="152" y="134" width="22" height="4" class="cyan"/>
        """
    if kind == "sleepy":
        return """
        <path d="M76 84h30v6H76zM118 84h30v6h-30z" class="ink"/>
        <path d="M92 112h34v6H92z" class="ink"/>
        <text x="144" y="58" class="mini">Zzz</text>
        <rect x="56" y="105" width="10" height="8" class="blush"/>
        <rect x="146" y="105" width="10" height="8" class="blush"/>
        """
    if kind == "excited":
        return """
        <path d="M80 76h14v14H80zM122 76h14v14h-14z" class="ink"/>
        <path d="M91 106h36v8h8v8h-8v8H91v-8h-8v-8h8z" class="ink"/>
        <path d="M170 40l8 16 18 2-13 12 3 18-16-9-16 9 3-18-13-12 18-2z" class="gold"/>
        """
    if kind == "love":
        return """
        <path d="M70 72h8v-8h12v8h8v12h-8v8h-8v8h-4v-8h-8v-8h-8V72z" class="heart"/>
        <path d="M120 72h8v-8h12v8h8v12h-8v8h-8v8h-4v-8h-8v-8h-8V72z" class="heart"/>
        <path d="M88 112h8v8h8v6h16v-6h8v-8h8v8h-8v8h-8v6h-16v-6h-8v-8h-8z" class="ink"/>
        <rect x="152" y="96" width="9" height="9" class="heart"/>
        """
    if kind == "debugging":
        return """
        <path d="M72 78h34v6H72zM116 78h34v6h-34z" class="ink"/>
        <path d="M83 91h10v10H83zM127 91h10v10h-10z" class="ink"/>
        <path d="M94 118h34v6H94z" class="ink"/>
        <path d="M158 48h8v8h8v8h-8v8h-8v-8h-8v-8h8z" class="bug"/>
        <path d="M174 51h14v5h-14zM174 66h14v5h-14z" class="bug"/>
        """
    return """
      <path d="M76 86h30v6H76zM118 86h30v6h-30z" class="ink"/>
      <path d="M92 116h36v6H92z" class="ink"/>
      <rect x="58" y="104" width="11" height="8" class="blush"/>
      <rect x="143" y="104" width="11" height="8" class="blush"/>
      <rect x="166" y="52" width="10" height="34" class="battery"/>
      <rect x="176" y="62" width="5" height="14" class="battery"/>
    """


def pixel_bear_svg(expression: str) -> str:
    return f"""
    <g transform="translate(54 30)" shape-rendering="crispEdges">
      <rect x="42" y="20" width="46" height="28" class="bear"/>
      <rect x="118" y="20" width="46" height="28" class="bear"/>
      <rect x="50" y="28" width="28" height="20" class="ear"/>
      <rect x="128" y="28" width="28" height="20" class="ear"/>
      <rect x="38" y="42" width="132" height="96" class="bear"/>
      <rect x="30" y="62" width="20" height="60" class="bear-dark"/>
      <rect x="158" y="62" width="20" height="60" class="bear-dark"/>
      <rect x="58" y="130" width="92" height="24" class="bear-dark"/>
      <rect x="76" y="96" width="60" height="40" class="muzzle"/>
      <rect x="100" y="97" width="14" height="10" class="nose"/>
      {expression_svg(expression)}
      <rect x="38" y="42" width="132" height="6" class="fur-hi"/>
      <rect x="52" y="54" width="18" height="6" class="fur-hi"/>
      <rect x="136" y="54" width="18" height="6" class="fur-shadow"/>
    </g>
    """


def render_svg(mood: dict[str, str]) -> str:
    name = escape(mood["name"])
    message = escape(mood["message"])
    accent = mood["accent"]
    expression = mood["expression"]

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 210" role="img" aria-labelledby="title desc">
  <title id="title">Daily pixel bear mood widget: {name}</title>
  <desc id="desc">A GitHub profile pixel bear mood widget showing the current mood as {name}.</desc>
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
      .bear-dark{{fill:#7a4328}}
      .ear{{fill:#5b2f1d}}
      .muzzle{{fill:#e8c7a5}}
      .nose,.ink{{fill:#1f2328}}
      .fur-hi{{fill:#c88955;opacity:.7}}
      .fur-shadow{{fill:#5f331f;opacity:.62}}
      .blush{{fill:#ff9fc5;opacity:.72}}
      .heart{{fill:#ff7bba}}
      .gold{{fill:#ffcc66}}
      .green{{fill:#39d353}}
      .cyan{{fill:#58a6ff}}
      .bug{{fill:#f97316}}
      .battery{{fill:#8b949e}}
      .mini{{font-family:Consolas,Monaco,monospace;font-size:17px;fill:{accent}}}
      .stroke{{fill:none;stroke-linecap:round;stroke-linejoin:round;stroke-width:4}}
      .float{{animation:float 3s ease-in-out infinite}}
      .spark{{animation:spark 1.8s steps(1,end) infinite}}
      .cursor{{animation:cursor 1s steps(1,end) infinite}}
      @keyframes float{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-4px)}}}}
      @keyframes spark{{0%,100%{{opacity:.28}}50%{{opacity:1}}}}
      @keyframes cursor{{0%,48%{{opacity:1}}49%,100%{{opacity:0}}}}
    </style>
  </defs>

  <rect x="8" y="8" width="744" height="194" rx="16" class="panel"/>
  <rect x="26" y="28" width="708" height="154" rx="12" class="screen" filter="url(#glow)"/>

  <g class="float">
    <rect x="58" y="28" width="214" height="154" rx="12" fill="#0d1117" stroke="{accent}" stroke-width="2" filter="url(#glow)"/>
    {pixel_bear_svg(expression)}
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
