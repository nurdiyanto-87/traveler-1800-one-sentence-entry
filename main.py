"""One Sentence for a Traveler from 1800 — make.fun entry.

Writes a single sentence explaining the modern internet to a time
traveler from 1800, using only words and things a person from 1800
could know: a printing press, a page, a question asked and answered.
The chosen image — a printing press that answers back — was picked
over a library, a post road, a town crier, and a market of letters:
it is the only one that is a single picture, explains both asking and
instant answer, and stays literally true as a comparison. Pure Python
standard library only; no third-party packages.
"""

import os

SENTENCE = (
    "It is a printing press that answers back: ask it anything, and it "
    "sets the very page you need before you faster than a man can blink."
)


def validate_sentence(sentence: str) -> str:
    """Check the entry is exactly one non-blank sentence of 1-200 chars."""
    if not isinstance(sentence, str):
        raise ValueError("entry must be a string")
    text = sentence.strip()
    if not text:
        raise ValueError("entry must not be blank")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters long")
    terminators = sum(text.count(c) for c in ".!?")
    if terminators != 1 or not text.endswith((".", "!", "?")):
        raise ValueError("entry must be exactly one sentence")
    return text


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(validate_sentence(SENTENCE))


if __name__ == "__main__":
    main()
