contenu_ly = r"""\version "2.24.2"

#(define RHYTHMS '((1 8 8) (2 16 16 16 16) (2 8 16 16 8)))

\header {
  title = "Variante rythmique d'archet"
  composer = "Étude inspirée de Ševčík"
}

\score {
  \new Staff {
    \tempo "Modéré"
    \clef treble
    \key d \major
    \time 4/4

    \relative c'' {
      % Motif à varier rythmiquement :
      \repeat volta 3 {
        \once \override TextScript.self-alignment-X = #LEFT
        d8[^\"Détaché\" e fis g]
        d8[ e fis g]
        d8[ e fis g]
        d8[ e fis g]
      }
    }
  }
}
"""

# Écriture dans le fichier
with open("variante_archet.ly", "w", encoding="utf-8") as f:
    f.write(contenu_ly)

print("✅ Fichier LilyPond écrit avec succès : variante_archet.ly")

