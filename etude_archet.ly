
\version "2.24.2"
\header {
  title = "Étude d’archet"
  subtitle = "Trajectoire de l’archet par note"
}
\score {
  \new Staff {
    \clef treble
    \time 4/4
    \tempo 4 = 72
    \relative c' {
      c'2^\markup \italic "tout l'archet" d'4^\markup \italic "première moitié" e'4^\markup \italic "premoiere moitié" f'2^\markup \italic "tout l'archet" g'4^\markup \italic "seconde moitié" a'4^\markup \italic "seconde moitié"
    }
  }
}
