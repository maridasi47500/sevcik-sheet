def generate_sextioles_with_accentuation():
    lilypond_header = r'''\version "2.24.2"
\header {
  title = "Sextioles 3/4 accentuées comme en 6/8"
  composer = "Généré par Python"
}
\score {
  \new Staff {
    \clef treble
    \time 3/4
    \tempo 4 = 80
    \relative c'' {
'''
    notes = ["d16", "e", "fis", "g", "a", "b"]  # sextioles
    accents = ["->", "", "", "->", "", ""]  # 1er et 4e temps accentués

    # Construire la sextiole : \tuplet 6/4 { ... }
    tuplet = "      \\tuplet 6/4 { "
    for note, accent in zip(notes, accents):
        tuplet += note + accent + " "
    tuplet += "}"

    lilypond_footer = r'''
    }
  }
}
'''

    with open("sextioles_accent_6-8.ly", "w", encoding="utf-8") as f:
        f.write(lilypond_header)
        f.write(tuplet + "\n")
        f.write(lilypond_footer)

    print("✅ Fichier 'sextioles_accent_6-8.ly' généré avec succès.")

generate_sextioles_with_accentuation()

