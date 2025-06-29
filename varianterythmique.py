motif = ["d", "e", "fis", "g"]

# Liste des variantes rythmiques
rhythms = [
    [8, 8],
    [16, 16, 16, 16],
    [8, 16, 16, 8]
]
def lilypond_note(note, duration):
    return f"{note}{duration}"

def generate_lilypond_variant(notes, rhythm):
    """
    Applique un rythme donné à un groupe de notes. Si le rythme est plus court, il boucle les notes.
    """
    output = []
    i = 0
    for dur in rhythm:
        output.append(lilypond_note(notes[i % len(notes)], dur))
        i += 1
    return " ".join(output)
with open("variantes_rythmiques.ly", "w", encoding="utf-8") as f:
    f.write(r"""\version "2.24.2"
\header {
  title = "Variantes rythmiques appliquées à un motif"
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
        f.write(f"      % Variante {i}\n")
        f.write("      " + generate_lilypond_variant(motif, rhythm) + "\n\n")

    f.write("    }\n  }\n}")

