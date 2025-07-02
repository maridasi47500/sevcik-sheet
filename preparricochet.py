# Script Python pour créer un exercice LilyPond sur le ricochet

lilypond_ricochet = r"""\version "2.24.2"

\header {
  title = "Exercice préparatoire au ricochet"
  subtitle = "Sautillé et ricochet progressif"
  composer = "généré par script Python"
}
\markup {
"
Exercice préparatoire au ricochet. Après avoir frappé la corde avec la pointe de l'archet (fig. a), l'archet rebondit et, par un léger tour de main, est ramené en position verticale (fig. b) pour frapper à nouveau la corde. L'archet doit être tenu facilement entre les doigts pour faciliter le rebond. Les coups doivent se succéder régulièrement :


With sautillé and ricochet.

Les coups s'accélèrent et la distance de rebond diminue.

Deux, trois et quatre notes rebondissant d'un seul coup."
}

\score {
  <<
    \new Staff \relative c'' {
      \clef treble
      \time 4/4
      \tempo "Lent et rebondissant"

      % Fig. a : première frappe pour initier le ricochet
      c8\downbow r8 r4 r2 |

      % Fig. b : retour de l’archet avec rebond léger
      c8\upbow r8 c8\downbow r8 r4 |

      % Sautillé régulier
      \repeat volta 2 {
        c16\staccato e\staccato c\staccato e\staccato c\staccato e\staccato c\staccato e\staccato |
      }

      % Ricochet sur 2 notes
      \repeat tremolo 2 { c16\downbow e } r8 r4 |

      % Ricochet sur 3 notes
      \repeat tremolo 3 { c16\downbow e } r8 |

      % Ricochet sur 4 notes
      \repeat tremolo 4 { c16\downbow e } |
    }
  >>
  \layout { }
}
"""

with open("exercice_ricochet.ly", "w", encoding="utf-8") as file:
    file.write(lilypond_ricochet)

print("Fichier LilyPond 'exercice_ricochet.ly' généré avec succès.")

