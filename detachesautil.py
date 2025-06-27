# Nom du fichier .ly
nom_fichier = "alternance_doubles_croches.ly"

# Contenu LilyPond
lilypond_code = r"""
\version "2.24.2"
\language "français"

\header {
  title = "Étude : détaché et sautillé"
  composer = "Généré par Python"
}

\score {
  \new Staff {
    \clef treble
    \key do \major
    \time 4/4

    % Mesure 1 : détaché
    \repeat unfold 4 {
      mi'16-\markup { \italic "détaché" } fa'16-. sol'16-. la'16-.
    }

    % Mesure 2 : sautillé
    \repeat unfold 4 {
      mi'16-\markup { \italic "sautillé" } fa'16 sol'16 la'16
    }

    % Mesure 3 : alternance
    mi'16-\markup { \italic "détaché" } fa'16-. sol'16-. la'16-.
    mi'16-\markup { \italic "sautillé" } fa'16 sol'16 la'16
    mi'16-\markup { \italic "détaché" } fa'16-. sol'16-. la'16-.
    mi'16-\markup { \italic "sautillé" } fa'16 sol'16 la'16

    \bar "|."
  }
}
"""

# Écriture du fichier .ly
with open(nom_fichier, "w", encoding="utf-8") as f:
    f.write(lilypond_code)

print(f"✅ Fichier LilyPond '{nom_fichier}' généré avec succès.")

