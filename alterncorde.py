# Génère un script LilyPond pour styles d'archet souples

lilypond_script = r"""\version "2.24.2"

\header {
  title = "Styles d'archet pour la souplesse sur deux cordes"
  composer = "Script généré en Python"
}

#(define myStyle "alternance cordes")

\score {
  <<
    \new Staff \relative c' {
      \clef treble
      \time 4/4
      % Martelé / détaché
      c8\downbow e\upbow c\downbow e\upbow |
      % Spiccato / sautillé
      c\staccato e\staccato c\staccato e\staccato |
      % Louré / portato
      \slurDashed
      c( e) c( e) |
      % Ricochet / jeté
      \repeat tremolo 4 { c16\downbow e } |
    }
  >>
  \layout { }
}
"""

with open("styles_archet.ly", "w", encoding="utf-8") as file:
    file.write(lilypond_script)

print("Script LilyPond généré dans 'styles_archet.ly'")

