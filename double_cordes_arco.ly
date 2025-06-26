
\version "2.24.2"
\header {
  title = "Double Cordes – Pizzicato main gauche et Arco"
}
\score {
  \new Staff {
    \clef treble
    \time 4/4
    \relative c' {
      <a d'>4_\markup "+"
<bes ees'>4^"arco"
<b f'>4
<c g'>4
    }
  }
}
