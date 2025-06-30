ly_script = r"""
\version "2.24.1"


violin = \relative d' {
  \clef treble
  \key d \major
  \time 4/4

  % Explicitly show 4th finger and string indication (optional)
  \once \override Glissando.style = #'zigzag
  <d\4>4 \glissando <fis\4>
}

\score {
  \new Staff {
    \violin
  }
  \layout { }
}
"""

with open("glissando_major_third.ly", "w") as f:
    f.write(ly_script)

