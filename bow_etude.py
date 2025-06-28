# bow_control_etude.py

filename = "bow_control_etude.ly"

lilypond_code = r'''
\version "2.24.2"
\header {
  title = "Exercice d’Archet : Contrôle et Double Cordes"
  composer = "Généré par Python"
}

violin = \relative c' {
  \clef treble
  \key d \major
  \time 4/4

  % Répétition avec barres de reprise
  \repeat volta 3 {
    <a' d'>4 r4 <b d'> r4
    ^\markup { "Traversée G → D pendant les silences" }

    <b e'>4 r4 <c e'> r4
    ^\markup { "Traversée D → A, inclinaison 15°" }

    <c fis'>4 r4 <d fis'> r4
    ^\markup { "Traversée A → E" }
  }

  % Mouvement progressif de l’archet
  r4^\markup { "Début G position - bras élevé" }
  <g d'> r <a d'> r
  ^\markup { "Progression douce vers D position" }

  r4^\markup { "Progression vers A position" }
  <a e'> r <b e'> r

  r4^\markup { "Final vers E position - bras plus bas" }
  <b fis'> r <c fis'> r
}

\score {
  \new Staff \violin
  \layout { }
  \midi { \tempo 4 = 80 }
}
\markup {
"Bars between two double bar lines are to be reреаted several times. The bow crosses two and three strings during the rests. There are 4 positions of bowing: the G, D, A and E position. In the G position (holding the violin correctly) the bow is parallel to the bottom of the violin, the right arm and elbow being adequately raised. At the D, A and E position the bow is more inclinedby 15°. Crossing from one string to the other this angle of 15° should not be made abruptly, but bow and elbow aproach gradu - ally the desired position."
}
'''

with open(filename, 'w') as file:
    file.write(lilypond_code)

print(f"Fichier LilyPond '{filename}' généré avec succès.")

