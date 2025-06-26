notes = [
    {"note": "c'4", "archet": "1/4"},
    {"note": "d'2", "archet": "2.3/4"},
    {"note": "e'4", "archet": "4/4"},
    {"note": "f'4", "archet": "1/4"},
    {"note": "g'2", "archet": "2.3/4"},
    {"note": "a'4", "archet": "4/4"},
    {"note": "c'4", "archet": "talon"},
    {"note": "d'4", "archet": ""},
    {"note": "e'2", "archet": "1/1"},
    {"note": "f'4", "archet": "pointe"},
    {"note": "g'4", "archet": ""},
    {"note": "a'2", "archet": "1/1"},
    {"note": "c'2", "archet": "tout l'archet"},
    {"note": "d'4", "archet": "première moitié"},
    {"note": "e'4", "archet": "premoiere moitié"},
    {"note": "f'2", "archet": "tout l'archet"},
    {"note": "g'4", "archet": "seconde moitié"},
    {"note": "a'4", "archet": "seconde moitié"}
]

# Crée les lignes musicales avec indication d’archet
lily_notes = ""
for n in notes:
    line = f"{n['note']}^\\markup \\italic \"{n['archet']}\""
    lily_notes += line + " "

# Corps du fichier LilyPond
lilypond_code = f"""
\\version "2.24.2"
\\header {{
  title = "Étude d’archet"
  subtitle = "Trajectoire de l’archet par note"
}}
\\score {{
  \\new Staff {{
    \\clef treble
    \\time 4/4
    \\tempo 4 = 72
    \\relative c' {{
      {lily_notes.strip()}
    }}
  }}
}}
"""

# Écrit dans un fichier .ly
with open("etude_archet.ly", "w") as f:
    f.write(lilypond_code)

print("Fichier LilyPond généré : etude_archet.ly")

