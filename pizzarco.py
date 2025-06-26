# Liste d'accords avec indication de pizz. main gauche ("+") et arco
accords = [
    {"notes": "<a d'>", "marking": r'_\markup "+"'},
    {"notes": "<bes ees'>", "marking": r'^"arco"'},
    {"notes": "<b f'>", "marking": ""},
    {"notes": "<c g'>", "marking": ""}
]

# Construction du contenu LilyPond
lily_notes = ""
for accord in accords:
    lily_notes += f"{accord['notes']}4{accord['marking']}\n"

# Gabarit complet LilyPond
lilypond_code = f"""
\\version "2.24.2"
\\header {{
  title = "Double Cordes – Pizzicato main gauche et Arco"
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

# Écriture du fichier LilyPond
with open("double_cordes_arco.ly", "w") as f:
    f.write(lilypond_code)

print("Fichier LilyPond généré : double_cordes_arco.ly")

