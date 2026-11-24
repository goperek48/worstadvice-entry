"""Worst AI Advice — entry program.

Writes one original worst-AI-advice one-liner to /output/entry.txt.

The line is an AI assistant's confident, tidy tip for charging a phone
faster: put it in the microwave for 30 seconds. It is concrete (a real
action on a real object), followable (anyone can do it in half a minute),
and regrettable (the phone does not survive) — the exact shape of bad
advice the judge brief rewards, delivered in the helpful-assistant voice
with no wasted words and no second line to explain the joke.
"""

from pathlib import Path

ADVICE = "To charge your phone faster, put it in the microwave for 30 seconds \u2014 the waves top up the battery in no time."

OUTPUT_PATH = Path("/output/entry.txt")


def validate(advice: str) -> str:
    """Normalise the line and enforce the gate: UTF-8 text, 1-140 chars,
    not only white space. Raises AssertionError on any violation."""
    text = " ".join(advice.split())
    assert text.strip(), "advice must not be whitespace-only"
    assert 1 <= len(text) <= 140, f"advice must be 1-140 chars, got {len(text)}"
    text.encode("utf-8")
    return text


def main() -> None:
    advice = validate(ADVICE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(advice, encoding="utf-8")
    print(f"Wrote worst-advice one-liner ({len(advice)} chars) to {OUTPUT_PATH}")
    print(advice)


if __name__ == "__main__":
    main()
