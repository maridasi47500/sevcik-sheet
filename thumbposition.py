def generate_thumb_shift_etude(filename="thumb_shift_etude.ly"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(r"""\version "2.24.2"

\header {
  title = "Étude : Coordination du pouce lors du passage à la demi-position"
  composer = "Généré par Python"
}

\score {
  \new Staff {
    \clef treble
    \key d \major
    \time 4/4

    \relative c'' {
      \tempo "Modéré"
      % Début en 1ère position
      <d-1 a'-4>4^\markup { \italic "1ère position" } ^\markup { "Archet entier" }
      <d a'>4^\markup { "Pouce suit" }

      % Passage à la demi-position
      <cis-1 gis'-4>4^\markup { \italic "Demi-position" } ^\markup { "1/2 archet" }
      <cis gis'>4^\markup { "Pouce avance" }

      % Retour en 1ère position
      <d-1 a'-4>2^\markup { \italic "Retour 1ère position" } ^\markup { "Pouce recule" }

      % Variante syncopée
      r8 <e-2 b'-4>8-> r <f-3 c'-4>8-> r <e b'>4
    }
  }
}
""")
    print(f"✅ Étude LilyPond générée : {filename}")

generate_thumb_shift_etude()

