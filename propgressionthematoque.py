ly_code = r'''
\version "2.24.2"

\header {
  title = "Progression thématique"
  subtitle = "Silence, proximité et intensité"
  composer = "Script par Python"
}

themeNarratif = \relative c' {
  \clef treble
  \key c \major
  \time 4/4
  \tempo 4 = 60

  % Instruction pédagogique
  \once \override Score.RehearsalMark.direction = #UP
  \mark \markup {
    \column {
      "*) Le seizième silence doit être nettement plus court que"
      "le triolet - croche de l'accompagnement."
      ""
      "544 b  —  P CC sol ré"
      ""
      "Dans les six premières mesures, la musique semble venir de loin."
      "Dans les mesures 7 à 9, elle devient plus présente."
      "À partir de la neuvième : montée du thème, sauf à la mesure 12 (scherzando)."
      "Mesures 15–16 : résolution thématique dans la continuité."
    }
  }

  % Mesures 1 à 6 – loin, pp
  r16^\pp r8.  c8( d16) r16 e8. r8
  r16 r r16  f8 e16 d r4
  r8 r8 g8 a16 r r4

  % Mesures 7 à 9 – présence croissante
  \tempo 4 = 66
  b4^\markup { \italic "plus proche" } d r16 g b d
  a8.\> g16 f4\! r4
  g8 a b c d r4

  % Mesures 10 à 14 – intensité accrue
  \tempo 4 = 76
  e16( d) c b a8 b r16 d d e
  e4^\f d r8 c c b
  \set Staff.midiInstrument = #"string ensemble 1"
  g4^\markup { \italic "scherzando (mes. 12)" } d'8. b16 c r r r
  d8 e r4  b2

  % Mesures 15–16 – dénouement
  \tempo 4 = 60
  c4\< d e f
  g1^\ff

  \bar "|."
}

\score {
  \new Staff \themeNarratif
  \layout { }
  \midi { \tempo 4 = 60 }
}
'''

with open("variation_narrative.ly", "w", encoding="utf-8") as file:
    file.write(ly_code)

print("Fichier LilyPond 'variation_narrative.ly' généré avec succès.")

