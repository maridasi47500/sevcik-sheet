ly_code = r'''
\version "2.24.2"

\header {
  title = "Étude de Ricochet et Sautillé"
  composer = "Généré par Python"
  subtitle = "Travail de rebond, pointe, et relâchement du poignet"
}

etudeRicochet = \relative c'' {
  \clef treble
  \key d \minor
  \time 6/8
  \tempo "Léger, contrôlé" 4. = 66

  % Bloc pédagogique en français
  \once \override Score.RehearsalMark.direction = #UP
  \mark \markup {
    \column {
      "*) L’archet frappe toujours la corde avec la pointe."
      "Les notes doivent imiter le pizzicato, son sec et court."
      "Appuyer légèrement avec la phalange pour éviter les ampoules."
      "*) Pour maintenir le rebond : utiliser toute la largeur du poil"
      "et enchaîner les cordes si nécessaire."
      "Ricochet & sautillé alternés — 2, 3, 4 notes d’un seul coup."
      "Avant le ricochet → soulevez l’archet. Avant le détaché **) reste en contact."
      "Poignet reste plié près du milieu de l’archet."
    }
  }

  % Exemples de rebond
  \once \override TextScript.direction = #UP
  \tuplet 3/2 { d16^\markup { "ricochet x3" } e f } \tuplet 3/2 { d16 e f }
  \tuplet 4/3 { e16^\markup { "ricochet x4" } f g a }
  \tuplet 2/3 { a16^\markup { "ricochet x2" } b }

  % Alternance avec sautillé régulier
  d8^\markup { "sautillé détaché" } e f g a b

  % Détaché simple (archet reste posé)
  c8^\markup { "**) détaché en contact avec la corde" } c b a g a

  % Retour ricochet vers corde voisine
  \tuplet 3/2 { d16^\markup { "ricochet sur 2 cordes" } f a }
  \tuplet 4/3 { a16 b c d }

  \bar "|."
}

\score {
  \new Staff \etudeRicochet
  \layout { }
  \midi { \tempo 4. = 66 }
}
'''

with open("etude_ricochet.ly", "w", encoding="utf-8") as file:
    file.write(ly_code)

print("Fichier LilyPond 'etude_ricochet.ly' généré avec succès.")

