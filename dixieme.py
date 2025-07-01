ly_code = r'''
\version "2.24.2"

\header {
  title = "Étude : Double arrêt à la dixième"
  composer = "Créé par Python"
}

doubleStopEtude = \relative c' {
  \clef treble
  \key d \major
  \time 4/4

  % Instruction: French coaching note
  \once \override Score.RehearsalMark.direction = #UP
  \mark \markup {
    \column {
      "+)"
      "Déplacez les deux doigts simultanément jusqu'à la dixième"
      "et placez-les pour le double arrêt."
      ""
      "First practise détaché."
    }
  }

  % Double stop example in 10th position (e.g., a' and d'')
  <a' d''>4 <a' d''> <a' d''> <a' d''>
  <a' d''> <a' d''> <a' d''> <a' d''>

  \bar "|."
}

\score {
  \new Staff \doubleStopEtude
  \layout { }
}
'''

# Write to LilyPond file
with open("double_arret_10e.ly", "w", encoding="utf-8") as file:
    file.write(ly_code)

print("Fichier LilyPond 'double_arret_10e.ly' généré avec succès.")

