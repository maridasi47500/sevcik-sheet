exercise = r"""
\\version "2.24.1"

\\header {
  title = "Octave Alternée en Double Cordes"
  subtitle = "Travail d'alternance entre graves et aigus en double stop"
  composer = "Exercice pédagogique"
}

\\score {
  <<
    \\new Staff {
      \\clef treble
      \\key a \\minor
      \\time 4/4

      \\repeat volta 2 {
        % Double stop: lower octave (A3 + A4)
        <a a'>8 <a a'> <a a'> <a a'>
        % Double stop: upper octave (C4 + C5)
        <c' c''>8 <c' c''> <c' c''> <c' c''>
        % Alternating again
        <a a'> <c' c''> <a a'> <c' c''>
        <c' c''> <a a'> <c' c''> <a a'>
      }
    }
  >>
  \\layout { }
}
"""

with open("octave_double_stop.ly", "w") as f:
    f.write(exercise)

