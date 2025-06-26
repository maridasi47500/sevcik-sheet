# Définition des notes en double corde
# Chaque double corde est représentée par un accord <note1 note2>
accords = [
    ("<a d'>", "4"),
    ("<bes ees'>", "4"),
    ("<b f'>", "4")
]

# Pizzicato main gauche noté avec un "+" sous la note
# En LilyPond, on utilise \\markup { \\draw-circle #0.6 #0.2 ##t } pour placer un +
lily_notes = ""
for acc, duree in accords:
    lily_notes += f"""
    {acc}{duree}_\\markup "+" 
    """

# Code complet
lilypond_code = f"""
\\version "2.24.2"
\\header {{
  title = "Double Cordes avec Pizz. Main Gauche"
}}
\\score {{
  \\new Staff {{
    \\clef treble
    \\time 4/4
    \\relative c' {{
      {lily_notes.strip()}
    }}
  }}
}}
"""

# Écriture du fichier .ly
with open("double_cordes_pizz_plus.ly", "w") as f:
    f.write(lilypond_code)

print("Fichier LilyPond généré : double_cordes_pizz_plus.ly")

