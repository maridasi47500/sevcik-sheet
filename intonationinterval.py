interval_above = "do''"  # Note cible située plus d'une octave au-dessus

lilypond_code = r"""
\version "2.24.2"
\language "français"

#(define repeatCount 4)

\score {
  \new Staff {
    \clef treble
    \key do \major
    \time 4/4

    \repeat unfold 4 { mi'8 fa'8 }  % 4 croches sur le mi'

    ( mi'4. mi''8 sol''4 )  % Intervalle lié, noire vers note plus haute
  }
}
"""

with open("intonation_interval.ly", "w", encoding="utf-8") as f:
    f.write(lilypond_code)

print("✅ Fichier 'intonation_interval.ly' généré.")

