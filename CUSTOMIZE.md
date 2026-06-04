# Cozy Bear Profile README Customization Guide

## Suggested Repo Structure

```text
Bearcoder6/
├─ README.md
├─ assets/
│  ├─ hero-banner.svg
│  ├─ bear-mood-widget.svg
│  ├─ bear-mood-cycle.svg
│  ├─ divider.svg
│  └─ footer-strip.svg
└─ .github/
   └─ workflows/
      └─ asset-check.yml
```

Use this inside the special GitHub profile repository named exactly like your username.
For your current profile, the repository should be named `Bearcoder6`.

## Asset Design Plan

- `hero-banner.svg`: main identity anchor. It sets the cozy cyber server-room mood and frames the coding bear as the mascot.
- `bear-mood-widget.svg`: static vertical widget for the five mood states requested: Happy, Focused, Sleepy, Excited, and Love It.
- `bear-mood-cycle.svg`: optional animated SVG mood badge. Use it if GitHub renders the animation well for your profile; otherwise keep the static widget.
- `divider.svg`: lightweight decorative separator for section rhythm.
- `footer-strip.svg`: final branded strip with a short quote.

## What To Edit Later

- Your name, GitHub username, no-website setting, interests, and language badges have already been filled in.
- Replace the three featured project cards when you have real repositories you want to show.
- Edit the quick status chips if you want a different personality.
- If you want the hero to include your real name, edit the text nodes inside `assets/hero-banner.svg`.

## Preview Notes

GitHub README rendering is stricter than a normal website. This package avoids JavaScript and uses Markdown,
GitHub-safe inline HTML, external stat images, and local SVG assets only.

To preview locally, open `README.md` in VS Code Markdown preview. For the most accurate result, push to your
profile repository and view it on GitHub.

## Practical Limitations

- GitHub does not run JavaScript in READMEs.
- Animated SVG support can vary by browser and GitHub's image proxy behavior. The static mood widget is the reliable default.
- External cards from services like Shields.io or GitHub Readme Stats can fail temporarily. The README still includes readable text content as a fallback.
