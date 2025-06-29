def write_extent_fourth_finger_D(filename="extent_4th_D.ly"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(r'''\version "2.24.2"

\header {
  title = "Étude – Extent du 4e doigt sur la corde D"
  composer = "Généré par Python"
}

\score {
  \new Staff {
    \clef treble
    \key d \major
    \time 4/4
    \tempo "Lent et connecté"

    \absolute {
      % Glissando du ré ouvert vers le ré'' (4e doigt étendu au maximum)
      a'^4\glissando ais'
      \glissando b'\glissando c''\glissando e''^4 a'^0 e''^0

      \bar "||"
    }
  }
}
''')
    print(f"✅ Fichier LilyPond écrit dans : {filename}")

write_extent_fourth_finger_D()

