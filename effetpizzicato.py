# Génère un script LilyPond avec remarques pédagogiques sur pizzicato à l'archet

lilypond_pizz_archet = r"""\version "2.24.2"

\header {
  title = "Jeu à la pointe de l'archet — effet pizzicato"
  subtitle = "Exercice préparatoire avec remarques techniques"
  composer = "Généré par script Python"
}

\markup {
  \column {
    \line { "* L'archet frappe toujours la corde avec la pointe." }
    \line { "  Les notes jouées doivent ressembler à celles pincées et sonner comme ces dernières." }
    \line { "  Pour éviter les ampoules aux doigts, il faut appuyer légèrement en pinçant" }
    \line { "  et utiliser si possible toute la phalange du doigt." }
    \vspace #0.5
    \line { "* Frappez la corde avec l'archet à l'extrémité pour obtenir l'effet pizzicato." }
    \line { "  Si possible, pincez la corde avec tout le bout du doigt" }
    \line { "  et sans trop appuyer pour éviter les ampoules." }
  }
}

\score {
  \new Staff \relative c'' {
    \clef treble
    \time 4/4
    \tempo "Détaché sec — imitation pizzicato"

    % Simule un effet détaché sec à la pointe
    c8\staccato\downbow r8 e\staccato\downbow r8 g\staccato\downbow r8 b\staccato\downbow r8 |
    d8\staccato\downbow r8 f\staccato\downbow r8 e\staccato\downbow r8 c\staccato\downbow r8 |
  }

  \layout { }
}
"""

with open("pizzicato_archet.ly", "w", encoding="utf-8") as file:
    file.write(lilypond_pizz_archet)

print("Fichier LilyPond 'pizzicato_archet.ly' généré avec succès.")

