motif = ["d", "e", "fis", "g"]

rhythms = [
    [8, 8],
    [16, 16, 16, 16],
    [8, 16, 16, 8]
]

archet_divisions = ["T", "M", "P", "T"]  # T = talon, M = milieu, P = pointe
archet_divisions = ["1er tiers", "2e tiers", "3e tiers", "1er tiers"]
archet_divisions = ["1/3", "2/3", "3/3", "1/3"]


def lilypond_note(note, duration, bow):
    return f'{note}{duration}^"{bow}"'

def generate_lilypond_variant(notes, rhythm, bows):
    output = []
    for i, dur in enumerate(rhythm):
        note = notes[i % len(notes)]
        bow = bows[i % len(bows)]
        output.append(lilypond_note(note, dur, bow))
    return " ".join(output)
with open("variantes_avec_archet.ly", "w", encoding="utf-8") as f:
    f.write(r"""\version "2.24.2"
\header {
  title = "Variantes rythmiques avec division d'archet"
  composer = "Généré par Python"
}
\score {
  \new Staff {
    \clef treble
    \key d \major
    \time 4/4
    \relative c'' {
""")

    for i, rhythm in enumerate(rhythms, start=1):
        f.write(f"      % Variante {i} – Rythme : {rhythm}\n")
        line = generate_lilypond_variant(motif, rhythm, archet_divisions)
        f.write("      " + line + "\n\n")

    f.write("    }\n  }\n}")

