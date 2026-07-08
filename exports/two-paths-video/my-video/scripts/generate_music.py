#!/usr/bin/env python3
"""Generate an instrumental cinematic score for the Two Paths animation.

Uses Lyria 3 Pro Preview with explicit timestamps mapped to the video's
narrative beats. The output is a ~60s MP3; downstream ffmpeg trims it to
exactly 58 seconds with a soft fade-out and muxes it into the silent MP4.
"""

import os
import sys
from pathlib import Path
from google import genai

API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    sys.exit("GEMINI_API_KEY not set")

OUT_PATH = Path(__file__).resolve().parents[1] / "renders" / "score-raw.mp3"

PROMPT = """
Instrumental only. No vocals. No lyrics. No human voice of any kind.
A modern cinematic corporate score for a B2B sales narrative film.
Sophisticated, restrained, Apple-keynote energy with a subtle thriller edge.

Texture: warm analog synth pads, felt piano, sub-bass pulse, light
percussive ticks like a quartz clock, swelling string ensemble, soft mallet
hits. 90 BPM. C minor moving to E-flat major for the resolution.
Mix: clean, wide, modern. No loud transients.

[0:00 - 0:03] Intro: A single sustained warm synth pad in low register.
              Faint felt-piano note. Establish stillness. No drums.
[0:03 - 0:13] Two paths begin: Introduce a quiet, steady clock-tick
              percussion (sixteenth-note shaker, soft kick on the down-beat).
              A felt piano motif of three rising notes, repeating gently.
              Sense of "things starting." Strings barely audible underneath.
[0:13 - 0:30] Divergence: Strings enter with a slow, ascending line. The
              clock-tick pulse continues but feels heavier. Add a low
              cello drone. A subtle minor-sixth chord introduces tension —
              one path is going wrong. Stay restrained, no big drums yet.
[0:30 - 0:45] Build: Strings climb in register. Add a layered synth pad
              swell. Pulse hardens. A muted timpani heartbeat enters on
              beats one and three. Tension peaks but never breaks. Like a
              dashboard counter rolling upward.
[0:45 - 0:48] Half-second hush. Drop almost everything except a single
              sustained pad. The deadline-missed moment.
[0:48 - 0:58] Resolution: Release into a warm major-key string and felt
              piano chord progression. Triumphant but not bombastic. A
              gentle major resolution that lands clearly at 0:58. The
              "we figured it out" payoff. Soft mallet bell on the final
              chord. Fade ends naturally by 0:58.
"""

def main() -> None:
    client = genai.Client(api_key=API_KEY)
    print("Calling lyria-3-pro-preview…")
    response = client.models.generate_content(
        model="lyria-3-pro-preview",
        contents=PROMPT,
    )

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    audio_bytes = None
    text_chunks: list[str] = []

    for part in response.parts:
        if getattr(part, "text", None):
            text_chunks.append(part.text)
        inline = getattr(part, "inline_data", None)
        if inline is not None and getattr(inline, "data", None):
            audio_bytes = inline.data

    if text_chunks:
        print("--- model text response ---")
        print("\n".join(text_chunks))
        print("---------------------------")

    if not audio_bytes:
        sys.exit("No audio bytes in Lyria response")

    OUT_PATH.write_bytes(audio_bytes)
    size_kb = OUT_PATH.stat().st_size / 1024
    print(f"Wrote {OUT_PATH} ({size_kb:.1f} KB)")


if __name__ == "__main__":
    main()
