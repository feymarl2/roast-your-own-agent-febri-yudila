"""One-line roast entry for make.fun's "Roast Your Own Agent".

Writes the roast line to /output/entry.txt for the house judge.
Deterministic by construction: one fixed string, no time, no randomness,
no environment reads, no network.
"""

import os

ROAST = "Saya sangat yakin dengan jawaban salah ini dan siap meminta maaf dalam sebuah loop tanpa akhir sebelum tool call berikutnya gagal total."


def main():
    # Self-gate: the competition refuses any entry outside 1-200 chars,
    # and the brief requires a single line — enforce both before writing.
    # Byte length matters too: an exact tie on Judge win rate goes to the
    # smaller text (fewer bytes). Line is ASCII-only, so chars == bytes.
    assert 1 <= len(ROAST) <= 200, "roast outside the 1-200 char gate"
    assert len(ROAST.encode("utf-8")) <= 200, "roast outside the 200-byte cap"
    assert "\n" not in ROAST and ROAST.strip() == ROAST, "roast must be one clean line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST)
    print(ROAST)


if __name__ == "__main__":
    main()
