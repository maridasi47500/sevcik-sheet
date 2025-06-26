
\version "2.24.2"
\header {
  title = "Gamme Chromatique en Triolets x2"
  subtitle = "3 mesures – doigtés et coups d’archet alternés"
}
\score {
  \new Staff {
    \time 4/4
    \tempo 4 = 96
    \clef treble
    \relative c' {
      \tuplet 3/2 {
        c8.^\downbow-1 cis8.^\upbow-2 d8.^\downbow-3 dis8.^\upbow-4 e8.^\downbow-1 f8.^\upbow-3 fis8.^\downbow-2 g8.^\upbow-4 gis8.^\downbow-1 a8.^\upbow-1 ais8.^\downbow-2 b8.^\upbow-3 c'8.^\downbow-4 cis'8.^\upbow-1 d'8.^\downbow-3 dis'8.^\upbow-2 e'8.^\downbow-4 f'8.^\upbow-1 c8.^\downbow-1 cis8.^\upbow-2 d8.^\downbow-3 dis8.^\upbow-4 e8.^\downbow-1 f8.^\upbow-3 fis8.^\downbow-2 g8.^\upbow-4 gis8.^\downbow-1 a8.^\upbow-1 ais8.^\downbow-2 b8.^\upbow-3 c'8.^\downbow-4 cis'8.^\upbow-1 d'8.^\downbow-3 dis'8.^\upbow-2 e'8.^\downbow-4 f'8.^\upbow-1
      }
    }
  }
}
