lilypond_code = r"""

\version "2.24.2"
\language "français"

\score {
  \new Staff {
    \clef treble
    \key do \major
    \time 4/4
    <<
      {
        \voiceOne
        \slurDown
        \downbow
        \once \stemUp
        \once \override Slur.direction = #DOWN
        sol'8( la' sol' la')
      }
      \\
      {
        \voiceTwo
        \slurNeutral
        fa'2
      }
    >>

    <<
      {
        \voiceOne
        \upbow
        \slurDown
        \once \stemUp
        \once \override Slur.direction = #DOWN
        sol'8( la' sol' la')
      }
      \\
      {
        \voiceTwo
        \slurNeutral
        mi'2
      }
    >>
  }
}

"""

with open("double_stop_slur.ly", "w", encoding="utf-8") as f:
    f.write(lilypond_code)

print("✅ Fichier LilyPond 'double_stop_slur.ly' créé.")

