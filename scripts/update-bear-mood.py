from __future__ import annotations

from html import escape
from pathlib import Path
import random


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "xp-bear-mood.svg"


MOODS = [
    {"name": "Happy", "message": "A small win made the desktop brighter.", "expression": "happy"},
    {"name": "Focused", "message": "One task, a few notes, no extra tabs.", "expression": "focused"},
    {"name": "Sleepy", "message": "Saving progress before a proper recharge.", "expression": "sleepy"},
    {"name": "Excited", "message": "A new idea just appeared on the desktop.", "expression": "excited"},
    {"name": "Curious", "message": "Opening one more folder to see what is inside.", "expression": "curious"},
    {"name": "Debugging", "message": "Following the clue, one line at a time.", "expression": "debugging"},
]


def face(kind: str) -> str:
    if kind == "happy":
        return '<rect x="47" y="55" width="7" height="7" class="ink"/><rect x="79" y="55" width="7" height="7" class="ink"/><path d="M48 76h7v6h25v-6h7v7h-7v7H55v-7h-7z" class="ink"/>'
    if kind == "focused":
        return '<path d="M42 52h18v5H42zm31 0h18v5H73z" class="ink"/><rect x="48" y="60" width="7" height="8" class="ink"/><rect x="79" y="60" width="7" height="8" class="ink"/><rect x="57" y="79" width="22" height="5" class="ink"/>'
    if kind == "sleepy":
        return '<path d="M43 61h18v5H43zm30 0h18v5H73zM56 81h24v5H56z" class="ink"/><text x="91" y="31" class="mini">Zzz</text>'
    if kind == "excited":
        return '<rect x="47" y="55" width="8" height="10" class="ink"/><rect x="79" y="55" width="8" height="10" class="ink"/><rect x="55" y="76" width="27" height="17" class="ink"/><rect x="62" y="82" width="13" height="11" fill="#f8dcb7"/><path d="M104 17l5 10 12 2-9 8 3 12-11-6-10 6 2-12-8-8 11-2z" fill="#f5c542"/>'
    if kind == "curious":
        return '<rect x="47" y="55" width="7" height="7" class="ink"/><rect x="80" y="52" width="8" height="11" class="ink"/><circle cx="68" cy="82" r="7" class="ink"/><rect x="93" y="72" width="23" height="18" fill="#fff" stroke="#7f9db9"/><path d="M98 77h13m-13 5h9" stroke="#0b5bd3" stroke-width="2"/>'
    return '<path d="M42 53h18v5H42zm31 0h18v5H73z" class="ink"/><rect x="48" y="61" width="7" height="8" class="ink"/><rect x="79" y="61" width="7" height="8" class="ink"/><rect x="56" y="82" width="25" height="5" class="ink"/><path d="M104 24h8v8h8v8h-8v8h-8v-8h-8v-8h8z" fill="#e85a35"/>'


def pixel_bear(kind: str) -> str:
    return f"""
      <g transform="translate(73 54)" class="crisp bob">
        <rect x="25" y="13" width="30" height="25" class="fur-dark"/>
        <rect x="77" y="13" width="30" height="25" class="fur-dark"/>
        <rect x="18" y="28" width="96" height="77" class="fur"/>
        <rect x="10" y="47" width="17" height="46" class="fur-dark"/>
        <rect x="105" y="47" width="17" height="46" class="fur-dark"/>
        <rect x="34" y="91" width="65" height="25" class="fur-dark"/>
        <rect x="44" y="67" width="48" height="33" fill="#f8dcb7"/>
        <rect x="62" y="67" width="13" height="9" class="ink"/>
        {face(kind)}
      </g>
    """


def render_svg(mood: dict[str, str]) -> str:
    name = escape(mood["name"])
    message = escape(mood["message"])
    expression = mood["expression"]
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 225" role="img" aria-labelledby="title desc">
  <title id="title">Bear mood: {name}</title>
  <desc id="desc">A privacy-friendly Windows XP style pixel bear widget showing the current mood as {name}.</desc>
  <defs>
    <linearGradient id="titlebar" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#3f8cf3"/><stop offset=".5" stop-color="#0869e8"/><stop offset="1" stop-color="#0054c8"/></linearGradient>
    <filter id="shadow" x="-20%" y="-30%" width="140%" height="170%"><feDropShadow dx="0" dy="6" stdDeviation="5" flood-color="#123765" flood-opacity=".38"/></filter>
    <style>
      .ui{{font-family:Tahoma,"MS Sans Serif",Arial,sans-serif;fill:#1f1f1f}}.white{{fill:#fff}}.blue{{fill:#174ea6}}.muted{{fill:#66758c}}
      .crisp{{shape-rendering:crispEdges}}.fur{{fill:#a9683d}}.fur-dark{{fill:#754127}}.ink{{fill:#202020}}.mini{{font-family:"Courier New",monospace;font-size:12px;fill:#174ea6}}
      .bob{{animation:bob 3.5s ease-in-out infinite}}.blink{{animation:blink 1s steps(1,end) infinite}}
      @keyframes bob{{0%,100%{{transform:translate(73px,54px)}}50%{{transform:translate(73px,50px)}}}}@keyframes blink{{0%,48%{{opacity:1}}49%,100%{{opacity:0}}}}
      @media (prefers-reduced-motion:reduce){{.bob,.blink{{animation:none}}}}
    </style>
  </defs>
  <rect width="760" height="225" rx="11" fill="#d6e6ff"/>
  <g filter="url(#shadow)">
    <rect x="17" y="15" width="726" height="194" rx="8" fill="#0a5cd4"/>
    <rect x="21" y="19" width="718" height="28" rx="6" fill="url(#titlebar)"/>
    <rect x="31" y="25" width="14" height="14" fill="#fff"/><path d="M34 28h8v8h-8z" fill="#5bad3b"/>
    <text class="ui white" x="51" y="38" font-size="13" font-weight="700">Bear Mood - Windows Messenger</text>
    <rect x="667" y="24" width="19" height="18" rx="3" fill="#1f75e5" stroke="#fff"/><path d="M672 36h9" stroke="#fff" stroke-width="2"/>
    <rect x="690" y="24" width="19" height="18" rx="3" fill="#1f75e5" stroke="#fff"/><rect x="695" y="29" width="9" height="8" fill="none" stroke="#fff"/>
    <rect x="713" y="24" width="19" height="18" rx="3" fill="#e8563f" stroke="#fff"/><path d="M718 29l9 8m0-8l-9 8" stroke="#fff" stroke-width="2"/>
    <rect x="21" y="47" width="718" height="158" fill="#ece9d8"/>
    <rect x="37" y="61" width="213" height="126" rx="5" fill="#fff" stroke="#7f9db9"/>
    {pixel_bear(expression)}
    <text class="ui muted" x="283" y="85" font-size="12">TODAY'S STATUS</text>
    <text class="ui blue" x="283" y="124" font-size="31" font-weight="700">{name}</text>
    <text class="ui" x="283" y="153" font-size="14">{message}</text>
    <text class="ui muted" x="283" y="181" font-size="11">updated quietly by GitHub Actions<tspan class="blink">_</tspan></text>
    <rect x="651" y="167" width="69" height="25" fill="#ece9d8" stroke="#7f7a6e"/>
    <rect x="654" y="170" width="63" height="19" fill="none" stroke="#fff"/>
    <text class="ui" x="676" y="184" font-size="11">OK</text>
  </g>
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
    cleaned = "\n".join(line.rstrip() for line in svg.splitlines()) + "\n"
    OUTPUT.write_text(cleaned, encoding="utf-8", newline="\n")
    print(f"Bear mood updated: {mood['name']}")


if __name__ == "__main__":
    main()
