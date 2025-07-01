ly_code = r'''
\version "2.24.2"

\header {
  title = "Exercices expressifs"
  subtitle = "(Transposé en 1/4 de mesure)"
  composer = "Créé par Python"
}

# (in C major for simplicity)
expressiveEtude = \relative c' {
  \clef treble
  \key c \major
  \time 4/4

  % Instruction block
  \once \override Score.RehearsalMark.direction = #UP
  \mark \markup {
    \column {
      "(Transposé en 1/4 de mesure.)"
      "Les notes de même hauteur et de même longueur sont jouées à la même hauteur."
      "Notes ascendantes → crescendo, descendantes → decrescendo."
      "Accentuez la 1ère noire et légèrement la tierce."
      "Syncopes → accent sur temps faibles."
      "Croches: accent sur 1ère & 5e; Doubles: 1ère & 9e."
      "Début de groupe: accent léger sur 3e (croches), 5e (doubles), 9e (triples)."
      "Accents: coup d’archet rapide ou pression du doigt (ou les deux)."
      "Forte: crin entier près du chevalet. Pianissimo: bord du crin près de la touche."
    }
  }

  % Sample rhythm with expressive markings
  \partial 4
  c4^\f
  e8\< e f g
  a4\!^\> g
  f8^\accent f r8 r8
  e4^\< f g a\!
  b8\> b b b
  c2^\pp^\markup { \italic "dolce" }

  \bar "|."
}

\score {
  \new Staff \expressiveEtude
  \layout { }
  \midi { \tempo 4 = 80 }
}
'''

with open("exercice_expressif.ly", "w", encoding="utf-8") as file:
    file.write(ly_code)

print("Fichier LilyPond 'exercice_expressif.ly' généré avec succès.")

