import yaml

def genere_partitions(fichier_yaml):
    with open(fichier_yaml, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    for exercice in data["exercices"]:
        titre = exercice["titre"]
        annotation = exercice.get("annotation", "")
        try:
          notes = " ".join(exercice["notes"])
        except:
          notes = "a b c d e f g a b c d e f g "

        ly_code = f'''
\\markup {{ \\bold "{titre}" }}
\\markup {{ "{annotation}" }}

\\score {{
  \\new Staff {{
    \\clef treble
    \\time 4/4
    \\relative c' {{
      {notes}
    }}
  }}
}}
'''
        with open(f"{titre.replace(' ', '_')}.ly", "w", encoding="utf-8") as out:
            out.write(ly_code)

genere_partitions('./exercise.yaml')
