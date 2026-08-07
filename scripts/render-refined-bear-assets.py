from __future__ import annotations

import base64
import hashlib
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
AVATAR = ASSETS / "avatar-bear.png"
README = ROOT / "README.md"


def avatar_data_uri() -> str:
    encoded = base64.b64encode(AVATAR.read_bytes()).decode("ascii")
    return f"data:image/png;base64,{encoded}"


def inline_svg_body(path: Path, prefix: str) -> str:
    content = path.read_text(encoding="utf-8")
    body = content[content.find(">") + 1 : content.rfind("</svg>")]
    ids = sorted(set(re.findall(r'\bid="([^"]+)"', body)), key=len, reverse=True)
    for original in ids:
        namespaced = f"{prefix}-{original}"
        body = body.replace(f'id="{original}"', f'id="{namespaced}"')
        body = body.replace(f"url(#{original})", f"url(#{namespaced})")
        body = body.replace(f'href="#{original}"', f'href="#{namespaced}"')
    return body


def sync_readme_cache_token(profile_path: Path) -> None:
    token = hashlib.sha256(profile_path.read_bytes()).hexdigest()[:12]
    content = README.read_text(encoding="utf-8")
    updated = re.sub(
        r"xp-profile\.svg(?:\?v=[0-9a-f]+)?",
        f"xp-profile.svg?v={token}",
        content,
    )
    if updated != content:
        README.write_text(updated, encoding="utf-8", newline="\n")
        print(f"updated README cache token: {token}")


def write(path: Path, content: str) -> None:
    cleaned = "\n".join(line.rstrip() for line in content.splitlines()) + "\n"
    path.write_text(cleaned, encoding="utf-8", newline="\n")
    print(f"rendered {path.relative_to(ROOT).as_posix()}")


def shared_defs() -> str:
    return """
    <linearGradient id="xp-title" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#3f8cf3"/>
      <stop offset=".48" stop-color="#0869e8"/>
      <stop offset="1" stop-color="#0054c8"/>
    </linearGradient>
    <linearGradient id="xp-taskbar" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#2f91f7"/>
      <stop offset=".35" stop-color="#1269dc"/>
      <stop offset="1" stop-color="#0751bd"/>
    </linearGradient>
    <linearGradient id="xp-start" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#62c34d"/>
      <stop offset="1" stop-color="#27831f"/>
    </linearGradient>
    <linearGradient id="xp-sidebar" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#7aa7ed"/>
      <stop offset="1" stop-color="#c4d6f5"/>
    </linearGradient>
    <filter id="window-shadow" x="-20%" y="-20%" width="140%" height="150%">
      <feDropShadow dx="0" dy="7" stdDeviation="6" flood-color="#123765" flood-opacity=".42"/>
    </filter>
    <style>
      .ui{font-family:Tahoma,"MS Sans Serif",Arial,sans-serif;fill:#1f1f1f}
      .mono{font-family:Consolas,"Courier New",monospace}
      .white{fill:#fff}.muted{fill:#5d6b82}.blue{fill:#174ea6}
      .crisp{shape-rendering:crispEdges}
      .blink{animation:blink 1.05s steps(1,end) infinite}
      .float{animation:float 4s ease-in-out infinite}
      .cloud{animation:cloud 18s linear infinite}
      @keyframes blink{0%,48%{opacity:1}49%,100%{opacity:0}}
      @keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-3px)}}
      @keyframes cloud{0%{transform:translateX(-24px)}100%{transform:translateX(34px)}}
      @media (prefers-reduced-motion:reduce){.blink,.float,.cloud{animation:none}}
    </style>
    """


def window_controls(x: int, y: int) -> str:
    return f"""
      <g class="crisp">
        <rect x="{x}" y="{y}" width="19" height="18" rx="3" fill="#1f75e5" stroke="#fff"/>
        <path d="M{x + 5} {y + 12}h9" stroke="#fff" stroke-width="2"/>
        <rect x="{x + 22}" y="{y}" width="19" height="18" rx="3" fill="#1f75e5" stroke="#fff"/>
        <rect x="{x + 27}" y="{y + 5}" width="9" height="8" fill="none" stroke="#fff" stroke-width="1.5"/>
        <rect x="{x + 44}" y="{y}" width="19" height="18" rx="3" fill="#e8563f" stroke="#fff"/>
        <path d="M{x + 49} {y + 5}l9 8m0-8l-9 8" stroke="#fff" stroke-width="2"/>
      </g>
    """


def xp_logo(x: int, y: int, scale: float = 1.0) -> str:
    return f"""
      <g transform="translate({x} {y}) scale({scale})" class="crisp">
        <path d="M0 0h9v8H0z" fill="#f35325"/><path d="M11 0h9v8h-9z" fill="#81bc06"/>
        <path d="M0 10h9v8H0z" fill="#05a6f0"/><path d="M11 10h9v8h-9z" fill="#ffba08"/>
      </g>
    """


def folder_icon(x: int, y: int, scale: float = 1.0) -> str:
    return f"""
      <g transform="translate({x} {y}) scale({scale})" class="crisp">
        <path d="M1 5h13l3 3h22v27H1z" fill="#d99618" stroke="#8a5b05"/>
        <path d="M2 10h38v24H2z" fill="#ffd45c" stroke="#ad7b12"/>
        <path d="M4 13h34" stroke="#fff1a6" stroke-width="2"/>
      </g>
    """


def render_arcade_bear(avatar: str) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 410" role="img" aria-labelledby="title desc">
  <title id="title">Bearcoder6 Windows XP inspired profile desktop</title>
  <desc id="desc">A nostalgic Windows XP desktop showing a compact Bearcoder6 profile window and research shortcuts.</desc>
  <defs>
    {shared_defs()}
    <clipPath id="hero-avatar"><rect x="491" y="137" width="122" height="122" rx="5"/></clipPath>
  </defs>

  <rect width="760" height="410" rx="11" fill="#69afea"/>
  <g class="cloud" fill="#fff" opacity=".92">
    <ellipse cx="110" cy="74" rx="68" ry="18"/><ellipse cx="74" cy="67" rx="28" ry="22"/><ellipse cx="128" cy="61" rx="39" ry="28"/>
    <ellipse cx="602" cy="67" rx="75" ry="18"/><ellipse cx="563" cy="59" rx="31" ry="23"/><ellipse cx="628" cy="51" rx="43" ry="30"/>
  </g>
  <path d="M0 229C128 160 226 177 347 239c117 60 248 63 413-7v178H0z" fill="#63ad36"/>
  <path d="M0 270c137-55 230-40 353 16 128 59 258 44 407-25v149H0z" fill="#3e982d" opacity=".72"/>

  <g class="ui white" font-size="11" text-anchor="middle">
    {folder_icon(25, 24, .88)}
    <text x="43" y="72">Research</text>
    {folder_icon(25, 93, .88)}
    <text x="43" y="141">Projects</text>
    <g transform="translate(29 166)" class="crisp"><rect width="30" height="35" fill="#d9ebf4" stroke="#fff"/><path d="M6 6h18v22H6z" fill="#8db6ca"/><path d="M2 0h26v5H2z" fill="#f5f7f8"/></g>
    <text x="43" y="218">Recycle Bin</text>
  </g>

  <g filter="url(#window-shadow)">
    <rect x="118" y="38" width="520" height="314" rx="8" fill="#0a5cd4" stroke="#174c9f" stroke-width="2"/>
    <rect x="122" y="42" width="512" height="28" rx="6" fill="url(#xp-title)"/>
    {xp_logo(132, 47, .72)}
    <text class="ui white" x="153" y="61" font-size="13" font-weight="700">bearcoder6 - My Computer</text>
    {window_controls(562, 47)}

    <rect x="122" y="70" width="512" height="278" fill="#ece9d8"/>
    <rect x="122" y="70" width="512" height="24" fill="#f5f3e8"/>
    <text class="ui" x="132" y="86" font-size="11">File</text><text class="ui" x="160" y="86" font-size="11">Edit</text>
    <text class="ui" x="188" y="86" font-size="11">View</text><text class="ui" x="221" y="86" font-size="11">Favorites</text>
    <text class="ui" x="276" y="86" font-size="11">Tools</text><text class="ui" x="312" y="86" font-size="11">Help</text>
    <rect x="122" y="94" width="512" height="32" fill="#ece9d8" stroke="#c6c3b5"/>
    <text class="ui muted" x="131" y="114" font-size="11">Address</text>
    <rect x="177" y="99" width="408" height="22" fill="#fff" stroke="#7f9db9"/>
    {folder_icon(183, 102, .43)}
    <text class="ui" x="205" y="114" font-size="11">C:\\Documents and Settings\\bearcoder6</text>
    <rect x="589" y="99" width="39" height="22" fill="#ece9d8" stroke="#9f9b8c"/>
    <text class="ui" x="600" y="114" font-size="11">Go</text>

    <rect x="130" y="134" width="147" height="199" rx="4" fill="url(#xp-sidebar)"/>
    <rect x="139" y="143" width="129" height="76" rx="4" fill="#fff" opacity=".91"/>
    <rect x="139" y="143" width="129" height="23" rx="4" fill="#d8e4f7"/>
    <text class="ui blue" x="149" y="159" font-size="12" font-weight="700">Profile Tasks</text>
    <text class="ui blue" x="151" y="184" font-size="11">View research</text>
    <text class="ui blue" x="151" y="202" font-size="11">Open projects</text>
    <rect x="139" y="229" width="129" height="91" rx="4" fill="#fff" opacity=".91"/>
    <rect x="139" y="229" width="129" height="23" rx="4" fill="#d8e4f7"/>
    <text class="ui blue" x="149" y="245" font-size="12" font-weight="700">Details</text>
    <text class="ui muted" x="150" y="271" font-size="10">Type: curious builder</text>
    <text class="ui muted" x="150" y="290" font-size="10">Status: learning</text>
    <text class="ui muted" x="150" y="309" font-size="10">Handle: Bearcoder6</text>

    <rect x="285" y="134" width="341" height="199" fill="#fff"/>
    <text class="ui blue" x="302" y="157" font-size="13" font-weight="700">Welcome.</text>
    <line x1="302" y1="166" x2="608" y2="166" stroke="#d8d2bc"/>
    <g class="float">
      <rect x="486" y="132" width="132" height="132" rx="7" fill="#fff" stroke="#7f9db9" stroke-width="3"/>
      <image href="{avatar}" x="491" y="137" width="122" height="122" clip-path="url(#hero-avatar)" preserveAspectRatio="xMidYMid slice" style="image-rendering:auto"/>
    </g>
    <text class="ui" x="302" y="195" font-size="24" font-weight="700">BEARCODER6</text>
    <text class="ui muted" x="302" y="219" font-size="12">AI agents / MLLMs</text>
    <text class="ui muted" x="302" y="237" font-size="12">machine learning / notes</text>
    <text class="ui" x="302" y="282" font-size="12">I read, build, test, and keep notes.</text>
    <text class="ui" x="302" y="303" font-size="12">That is pretty much the whole program.</text>
    <rect x="302" y="313" width="306" height="9" fill="#f5f3e8" stroke="#d8d2bc"/>
    <text class="ui muted" x="307" y="322" font-size="8">ready</text>
  </g>

  <rect x="0" y="370" width="760" height="40" fill="url(#xp-taskbar)"/>
  <path d="M0 370h760" stroke="#6ab6ff" stroke-width="2"/>
  <rect x="0" y="371" width="103" height="39" rx="0 16 16 0" fill="url(#xp-start)"/>
  {xp_logo(12, 381, .85)}
  <text class="ui white" x="39" y="397" font-size="17" font-style="italic" font-weight="700">start</text>
  <rect x="111" y="376" width="223" height="29" rx="3" fill="#3b8fe9" stroke="#0c4dad"/>
  {xp_logo(120, 382, .62)}
  <text class="ui white" x="140" y="395" font-size="11">bearcoder6 - My Computer</text>
  <rect x="657" y="371" width="103" height="39" fill="#0b78d4"/>
  <text class="ui white" x="679" y="395" font-size="11">always learning</text>
</svg>
"""


def render_research_explorer() -> str:
    folders = [
        ("AI Agents", "Workflows and tool use", 66, 160),
        ("Multimodal Models", "Vision and language", 268, 160),
        ("Machine Learning", "Foundations and practice", 470, 160),
        ("Notes", "Things worth remembering", 66, 230),
        ("Experiments", "Small ideas in motion", 268, 230),
        ("Open Source", "Useful pieces to share", 470, 230),
    ]
    folder_markup = "".join(
        f"""<g>{folder_icon(x, y, .9)}<text class="ui blue" x="{x + 48}" y="{y + 16}" font-size="12" font-weight="700">{name}</text><text class="ui muted" x="{x + 48}" y="{y + 34}" font-size="10">{desc}</text></g>"""
        for name, desc, x, y in folders
    )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 310" role="img" aria-labelledby="title desc">
  <title id="title">Bearcoder6 research explorer</title>
  <desc id="desc">A Windows XP Explorer window with six concise folders for current technical interests.</desc>
  <defs>{shared_defs()}</defs>
  <rect width="760" height="310" rx="11" fill="#d6e6ff"/>
  <g filter="url(#window-shadow)">
    <rect x="22" y="17" width="716" height="276" rx="8" fill="#0a5cd4"/>
    <rect x="26" y="21" width="708" height="28" rx="6" fill="url(#xp-title)"/>
    {folder_icon(34, 25, .5)}
    <text class="ui white" x="58" y="40" font-size="13" font-weight="700">Research Explorer</text>
    {window_controls(662, 25)}
    <rect x="26" y="49" width="708" height="240" fill="#ece9d8"/>
    <rect x="26" y="49" width="708" height="24" fill="#f5f3e8"/>
    <text class="ui" x="37" y="65" font-size="11">File</text><text class="ui" x="66" y="65" font-size="11">Edit</text><text class="ui" x="94" y="65" font-size="11">View</text>
    <text class="ui" x="128" y="65" font-size="11">Favorites</text><text class="ui" x="184" y="65" font-size="11">Tools</text><text class="ui" x="220" y="65" font-size="11">Help</text>
    <rect x="26" y="73" width="708" height="36" fill="#ece9d8" stroke="#c6c3b5"/>
    <rect x="38" y="80" width="46" height="22" fill="#ece9d8" stroke="#9f9b8c"/>
    <path d="M66 85l-8 6 8 6" fill="none" stroke="#237025" stroke-width="3"/>
    <text class="ui muted" x="99" y="95" font-size="11">Address</text>
    <rect x="145" y="80" width="566" height="22" fill="#fff" stroke="#7f9db9"/>
    {folder_icon(151, 83, .42)}
    <text class="ui" x="173" y="95" font-size="11">My Computer &gt; Research</text>
    <rect x="38" y="119" width="684" height="158" fill="#fff" stroke="#c7c7c7"/>
    <text class="ui blue" x="52" y="142" font-size="13" font-weight="700">6 folders</text>
    {folder_markup}
  </g>
</svg>
"""


def render_bear_terminal(avatar: str) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 620 255" role="img" aria-labelledby="title desc">
  <title id="title">Bearcoder6 command prompt</title>
  <desc id="desc">A compact Windows XP command prompt listing a minimal current workflow and toolkit.</desc>
  <defs>
    {shared_defs()}
    <clipPath id="terminal-avatar"><rect x="478" y="55" width="102" height="102" rx="5"/></clipPath>
  </defs>
  <rect width="620" height="255" fill="#d6e6ff"/>
  <g filter="url(#window-shadow)">
    <rect x="15" y="14" width="590" height="225" rx="7" fill="#0a5cd4"/>
    <rect x="19" y="18" width="582" height="27" rx="5" fill="url(#xp-title)"/>
    <rect x="27" y="24" width="15" height="14" fill="#151515" stroke="#fff"/>
    <text class="mono white" x="47" y="36" font-size="12">C:\\WINDOWS\\system32\\cmd.exe</text>
    {window_controls(529, 23)}
    <rect x="19" y="45" width="582" height="190" fill="#111"/>
    <text class="mono white" x="32" y="70" font-size="13">Microsoft Windows XP [Bear Edition]</text>
    <text class="mono white" x="32" y="92" font-size="13">C:\\bearcoder6&gt; current_focus</text>
    <text class="mono" x="32" y="116" font-size="13" fill="#9fe870">  reading papers</text>
    <text class="mono" x="32" y="138" font-size="13" fill="#9fe870">  building small prototypes</text>
    <text class="mono" x="32" y="160" font-size="13" fill="#9fe870">  documenting what works</text>
    <text class="mono white" x="32" y="188" font-size="13">C:\\bearcoder6&gt; toolkit</text>
    <text class="mono" x="32" y="211" font-size="13" fill="#9fe870">  Python / C / C++ / Java</text>
    <text class="mono white" x="32" y="232" font-size="13">C:\\bearcoder6&gt;<tspan class="blink">_</tspan></text>
    <rect x="473" y="50" width="112" height="112" rx="7" fill="#fff" stroke="#7f9db9" stroke-width="3"/>
    <image href="{avatar}" x="478" y="55" width="102" height="102" clip-path="url(#terminal-avatar)" preserveAspectRatio="xMidYMid slice"/>
  </g>
</svg>
"""


def render_profile_composite() -> str:
    desktop = inline_svg_body(ASSETS / "xp-desktop.svg", "desktop")
    research = inline_svg_body(ASSETS / "xp-research-explorer.svg", "research")
    terminal = inline_svg_body(ASSETS / "xp-command-prompt.svg", "terminal")
    mood = inline_svg_body(ASSETS / "xp-bear-mood.svg", "mood")
    footer = inline_svg_body(ASSETS / "xp-taskbar-footer.svg", "footer")
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 1153" role="img" aria-labelledby="title desc">
  <title id="title">Continuous Windows XP inspired Bearcoder6 profile</title>
  <desc id="desc">A single seamless profile artwork containing a desktop, research explorer, command prompt, pixel bear mood, and taskbar footer.</desc>
  <rect width="760" height="1153" fill="#d6e6ff"/>
  <svg x="0" y="0" width="760" height="410" viewBox="0 0 760 410">
    {desktop}
  </svg>
  <svg x="0" y="410" width="760" height="276" viewBox="0 17 760 276" overflow="hidden">
    {research}
  </svg>
  <svg x="70" y="686" width="620" height="225" viewBox="0 14 620 225" overflow="hidden">
    {terminal}
  </svg>
  <svg x="0" y="911" width="760" height="194" viewBox="0 15 760 194" overflow="hidden">
    {mood}
  </svg>
  <svg x="0" y="1105" width="760" height="48" viewBox="0 8 760 48" overflow="hidden">
    {footer}
  </svg>
</svg>
"""


def render_divider() -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 64" role="img" aria-labelledby="title desc">
  <title id="title">Windows XP style footer bar</title>
  <desc id="desc">A small blue taskbar footer thanking visitors without personal details.</desc>
  <defs>{shared_defs()}</defs>
  <rect x="0" y="8" width="760" height="48" rx="8" fill="url(#xp-taskbar)"/>
  <rect x="0" y="8" width="112" height="48" rx="8 19 19 8" fill="url(#xp-start)"/>
  {xp_logo(15, 22, .9)}
  <text class="ui white" x="43" y="39" font-size="17" font-style="italic" font-weight="700">start</text>
  <rect x="126" y="16" width="238" height="32" rx="4" fill="#3b8fe9" stroke="#0c4dad"/>
  <text class="ui white" x="145" y="36" font-size="12">Thanks for stopping by.</text>
  <rect x="636" y="9" width="124" height="46" rx="0 8 8 0" fill="#0b78d4"/>
  <text class="ui white" x="660" y="37" font-size="12">keep building</text>
</svg>
"""


def main() -> None:
    avatar = avatar_data_uri()
    write(ASSETS / "xp-desktop.svg", render_arcade_bear(avatar))
    write(ASSETS / "xp-research-explorer.svg", render_research_explorer())
    write(ASSETS / "xp-command-prompt.svg", render_bear_terminal(avatar))
    write(ASSETS / "xp-taskbar-footer.svg", render_divider())
    profile_path = ASSETS / "xp-profile.svg"
    write(profile_path, render_profile_composite())
    sync_readme_cache_token(profile_path)


if __name__ == "__main__":
    main()
