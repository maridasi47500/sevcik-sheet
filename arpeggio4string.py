ly_code = r'''
\version "2.24.2"

\header {
  title = "Étude d’Arpège à Quatre Cordes"
  composer = "Généré par Python"
}

arpeggioStudy = \relative c' {
  \clef treble
  \key c \major
  \time 4/4

  % Instruction: French performance note
  \once \override Score.RehearsalMark.direction = #UP
  \mark \markup {
    \column {
      "**)" 
      "Abaissez et soulevez le coude, le poignet immobile."
      "Avec une légère inclinaison. L'archet reste sur la corde."
    }
  }

  % Arpeggio across four strings
  <c g e' a'>\arpeggio
  <c g e' a'>\arpeggio
  <c g e' a'>\arpeggio

  \bar "|."
}

\score {
  \new Staff \arpeggioStudy
  \layout { }
}
'''

# Write to LilyPond file
with open("arpege_4cordes.ly", "w", encoding="utf-8") as file:
    file.write(ly_code)

print("Fichier LilyPond 'arpege_4cordes.ly' créé avec succès.")

