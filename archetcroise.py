exercise = r"""
\version "2.24.1"

\header {
  title = "Exercice : Passage de l'archet entre cordes"
  subtitle = "Pendant les silences, l’archet change de position en douceur"
  composer = "Exercice pédagogique"
}

\score {
  <<
    \new Staff {
      \clef treble
      \key d \major
      \time 4/4

      \repeat volta 2 {

        % Position SOL
        g4 r r r
        % Passage vers RÉ
        d'4 r r r
        % Passage vers LA
        a'4 r r r
        % Passage vers MI
        e''4 r r r

        % Aller-retour sur 3 cordes pendant silences
        g4 r d' r
        a'4 r e'' r

        % Variante : changement rapide
        g8 r d'8 r a'8 r e''8 r
      }
    }
  >>
  \layout { }
}
"""

with open("archet_croise.ly", "w") as f:
    f.write(exercise)

