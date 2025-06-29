def write_glissando_etude(filename="glissando_etude.ly"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(r'''\version "2.24.2"

\header {
  title = "Étude d'Archet avec Glissando et Arpèges"
  composer = "Généré par Python"
}

\score {
  \new Staff {
    \clef treble
    \key d \major
    \time 4/4
    \relative c'' {

      % Arpège montant avec glissando vers le 4e doigt
      d8^"Talon" fis a d'\glissando fis''^"Pointe"

      % Retour par glissando en sens inverse
      fis''8\glissando d' a fis d^"Talon" r4

      % Variation rythmique avec divisions d'archet
      <d fis>4^"Milieu" r <e g>^"Milieu" r
      <fis a>4.^"Pointe" <d fis>8^"Talon"

      % Glissando chromatique sur une corde (D)
      d8\glissando dis\glissando e\glissando f\glissando fis
      fis\glissando d r2
    }
  }
}
''')
    print(f"✅ Étude écrite dans : {filename}")

write_glissando_etude()

