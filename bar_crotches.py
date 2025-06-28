# Save this as generate_violin.ly and compile with LilyPond

lilypond_code = r"""
\version "2.24.2"
\header {
  title = "Violin Study"
  composer = "AI-assisted Composition"
}

violinNotes = \relative c'' {
  \clef treble
  \key c \major
  \time 4/4

  % Example rhythm using crotchets, quavers, and semiquavers
  c4 d8 e8 f4 g16 a16 b16 c16 |
  c'4 b8 a8 g4 f16 e16 d16 c16 |
}



\score {
  <<
    \new Staff {
      \violinNotes
    }
    \markup { \column { \vspace #2 \violinText } }
  >>
  \layout { }
}
\markup {
    "Each bar on crotchets, quavers and semiquavers as before."
    "The bowing remains the same as on crotches."
}
"""
with open("violin_study.ly", "w") as f:
    f.write(lilypond_code)
print("✅ LilyPond file saved as 'violin_study.ly'. Compile it with LilyPond to produce sheet music.")

