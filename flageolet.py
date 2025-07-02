# Génère un fichier LilyPond pour tierces majeures en doubles cordes de flageolet

lilypond_tierces_flageolet = r"""\version "2.24.2"

\header {
  title = "Tierces majeures en doubles cordes de flageolet"
  subtitle = "Exercice sur flageolets naturels"
  composer = "Généré en Python"
}

\score {
  <<
    \new Staff \relative c' {
      \clef treble
      \key c \major
      \time 4/4
      \tempo "Modéré et clair"

      % Tierce majeure : C + E (flageolet)
      <c\harmonic e\harmonic>1 |
      <d\harmonic fis\harmonic>1 |
      <e\harmonic gis\harmonic>1 |
      <f\harmonic a\harmonic>1 |
      <g\harmonic b\harmonic>1 |
    }
  >>
  \layout { }
}
"""

with open("tierces_flageolet.ly", "w", encoding="utf-8") as file:
    file.write(lilypond_tierces_flageolet)

print("Fichier LilyPond 'tierces_flageolet.ly' généré avec succès.")

