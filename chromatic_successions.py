# chromatic_succession_8_starts.py

filename = "chromatic_successions_d_major.ly"

lilypond_code = r'''
\version "2.24.2"
\header {
  title = "Chromatic Successions from 8 Different Tones"
  subtitle = "For Violin – 1st to 3rd Position – D Major Context"
  composer = "Generated by Python"
}

violin = \relative d' {
  \clef treble
  \key d \major
  \time 4/4
  \tempo 8 = 168

  \repeat volta 2 {
    % Line 1: D to A
    d8 dis e f fis g gis a
    ^\markup { "Start on D – climb to 3rd pos A" }

    % Line 2: E♭ to B♭
    ees8 e f fis g gis a bes
    ^\markup { "Start on E♭ – reach B♭" }

    % Line 3: E to B
    e8 f fis g gis a bes b
    ^\markup { "Start on E – up to B" }

    % Line 4: F to C
    f8 fis g gis a bes b c
    ^\markup { "Start on F – end on C" }

    % Line 5: F♯ to C♯
    fis8 g gis a bes b c cis
    ^\markup { "Start on F♯ – reach C♯" }

    % Line 6: G to D
    g8 gis a bes b c cis d
    ^\markup { "Start on G – ending on D" }

    % Line 7: G♯ to D♯
    gis8 a bes b c cis d dis
    ^\markup { "Start on G♯ – reach D♯" }

    % Line 8: A to E
    a8 bes b c cis d dis e
    ^\markup { "Start on A – up to E" }
  }
}

\score {
  \new Staff \violin
  \layout { }
  \midi { \tempo 8 = 168 }
}
'''

with open(filename, 'w') as file:
    file.write(lilypond_code)

print(f"LilyPond file '{filename}' generated successfully.")

