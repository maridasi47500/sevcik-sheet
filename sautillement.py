exercise = r"""
\version "2.24.1"

\header {
  title = "Exercice de Sautillement Rapide"
  subtitle = "7 variantes en octaves alternées"
  composer = "Exercice pédagogique"
}

upperNotes = { a''8 a'' a'' a'' a'' a'' a'' a'' }
lowerNotes = { a8 a a a a a a a }

\score {
  <<
    \new Staff {
      \clef treble
      \key a \minor
      \time 4/4
      \repeat volta 2 {
        % Variante 1 : alternance par octaves
        <<
          \new Voice = "up"   { \voiceOne \upperNotes }
          \new Voice = "down" { \voiceTwo \lowerNotes }
        >>
        \break
        % Variante 2 à 7 : on pourrait varier les rythmes, les intervalles, etc.
        % À remplir selon les objectifs pédagogiques
      }
    }
      \relative a16 {
        a' a a' a a' a a' a a' a' a' a' a' a' a'
      }
\relative a'' {
  \repeat volta 2 {
    \time 6/8
    \tuplet 3/2 { a8\staccato c b } \tuplet 3/2 { a c b }
    \tuplet 3/2 { g b a } \tuplet 3/2 { g b a }
  }
}

\relative a' {
  \repeat volta 2 {
    \time 4/4
    <a f'>8-. <a f'>-. r <a f'>-. <a f'>-. r <a f'>-. <a f'>-.
  }
}


  >>
  \layout { }
}
"""

with open("sautillement.ly", "w") as f:
    f.write(exercise)

