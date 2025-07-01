ly_code = r'''
\version "2.24.2"

\header {
  title = "Étude expressive à développement progressif"
  composer = "Script généré avec Python"
}

expressiveStudy = \relative c' {
  \clef treble
  \key g \major
  \time 4/4
  \tempo 4 = 63

  % Instruction générale
  \once \override Score.RehearsalMark.direction = #UP
  \mark \markup {
    \column {
      "<<*)" 
      "En montant, crescendo — en descendant, decrescendo."
      "Chaque groupe devient plus profond → le crescendo décroît."
      "La fondamentale de la mélodie est mise en valeur, puis pp à la mesure 3."
      "Deux fois plus lent en p et pp, avec expression & vibrato."
      "Mes. 5–6 : petit accelerando avec crescendo/decrescendo modérés."
      "Mes. 16 : crescendo après un ritardando prolongé → jusqu'au forte."
    }
  }

  % Phrase introductive avec crescendo en montée
  g4\< a b c\!
  d4^\pp c b a
  g2~ g

  % Tempo lent, pp, vibrato expressif (indiqué par "dolce")
  \tempo 4 = 50
  b4^\p^\markup { \italic "dolce, vib." } b b b
  c8( b) a( g)
  \tempo 4 = 63

  % petit accelerando et dynamique modérée
  \tempo 4 = 66
  g4\< a b\! b\>
  a4 g\! \tempo 4 = 72

  % reprise thématique énergique
  g4^\f b c d
  d2~ d4 b

  % Final : mesure 16 avec crescendo et ritardando
  \tempo 4 = 66
  c4\< b a g
  \tempo 4 = 60
  f2\>^\markup { \italic "rit." } g\!

  \bar "|."
}

\score {
  \new Staff \expressiveStudy
  \layout { }
  \midi { \tempo 4 = 63 }
}
'''

# Sauvegarde dans un fichier .ly
with open("etude_expressive.ly", "w", encoding="utf-8") as file:
    file.write(ly_code)

print("Fichier LilyPond 'etude_expressive.ly' généré avec succès.")

