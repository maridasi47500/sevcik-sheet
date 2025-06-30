exercise = r"""
\version "2.24.1"

\header {
  title = "Alternance Détaché / Sautillé"
  subtitle = "L’archet reste sur la corde en sautillé"
  composer = "Exercice technique"
}

\score {
  <<
    \new Staff {
      \clef treble
      \key d \major
      \time 4/4

      \repeat volta 2 {
        % Mesure 1 : Détaché sur une corde
        d'8-\markup { \italic "détaché" } d d d d d d d
        % Mesure 2 : Sautillé sur corde (même note pour rebond)
        d'16-\staccato d-\staccato d-\staccato d-\staccato d-\staccato d-\staccato d-\staccato d-\staccato
        % Mesure 3 : Détaché avec passage de corde
        a8 a d d a a d d
        % Mesure 4 : Sautillé sur notes alternées, rebond contrôlé
        d'16-\staccato e-\staccato d-\staccato e-\staccato d-\staccato e-\staccato d-\staccato e-\staccato
      }
    }
  >>
  \layout { }
}
"""

with open("alternating_bow_strokes.ly", "w") as f:
    f.write(exercise)

