exercise = r"""
\gversion "2.24.1"

\gheader {
  title = "Double Stops en 1re Position"
  subtitle = "Alternance de doubles cordes en accords"
  composer = "Exercice pédagogique"
}

\gscore {
  <<
    \gnew Staff {
      \gclef treble
      \gkey d \\major
      \gtime 4/4

      \grepeat volta 2 {

        % G + B (D string + A string) — 1 + 2
        <g b>4 <g b> <g b> <g b>
        % A + C# (A + E string) — 1 + 2
        <a' cis''>4 <a' cis''> <a' cis''> <a' cis''>
        % B + D — 1st finger + open string
        <b d'>4 <b d'> <b d'> <b d'>
        % C# + E — 2nd finger + open string
        <cis' e'>4 <cis' e'> <cis' e'> <cis' e'>
        % G + D — 3rd finger + open string
        <g d'>4 <g d'> <g d'> <g d'>
        % F# + A — 2nd finger + 1st finger
        <fis' a'>4 <fis' a'> <fis' a'> <fis' a'>
        % A + E (octave open strings)
        <a e'>4 <a e'> <a e'> <a e'>
      }
    }
  >>
  \glayout { }
}
"""

with open("first_position_double_stops.ly", "w") as f:
    f.write(exercise)

