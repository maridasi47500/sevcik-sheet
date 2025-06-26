# Motifs chromatiques avec doigtés et coups d’archet
motifs = [
    [("c", "1", "\\downbow"), ("cis", "2", "\\upbow"), ("c", "1", "\\downbow"), ("cis", "2", "\\upbow")],
    [("cis", "2", "\\downbow"), ("d", "3", "\\upbow"), ("cis", "2", "\\downbow"), ("d", "3", "\\upbow")],
    [("d", "3", "\\downbow"), ("ees", "4", "\\upbow"), ("d", "3", "\\downbow"), ("ees", "4", "\\upbow")],
    [("ees", "4", "\\downbow"), ("e", "1", "\\upbow"), ("ees", "4", "\\downbow"), ("e", "1", "\\upbow")],
    [("e", "1", "\\downbow"), ("f", "2", "\\upbow"), ("e", "1", "\\downbow"), ("f", "2", "\\upbow")],
    [("f", "2", "\\downbow"), ("fis", "3", "\\upbow"), ("f", "2", "\\downbow"), ("fis", "3", "\\upbow")],
    [("fis", "3", "\\downbow"), ("g", "4", "\\upbow"), ("fis", "3", "\\downbow"), ("g", "4", "\\upbow")],
    [("g", "4", "\\downbow"), ("gis", "1", "\\upbow"), ("g", "4", "\\downbow"), ("gis", "1", "\\upbow")]
]

# Générer le code LilyPond avec doigtés et coups d’archet
lily_notes = ""
for motif in motifs:
    for note, doigt, archet in motif:
        lily_notes += f"{note}8^{archet}-{doigt} "

# Modèle LilyPond
lilypond_code = f"""
\\version "2.24.2"
\\header {{
  title = "Préparation Chromatique"
}}
\\score {{
  \\new Staff {{
    \\time 4/4
    \\tempo 4 = 80
    \\clef treble
    \\relative c' {{
      {lily_notes.strip()}
    }}
  }}
}}
"""

# Écriture du fichier
with open("preparation_chromatique_violin.ly", "w") as f:
    f.write(lilypond_code)

print("Fichier avec doigtés et coups d’archet créé : preparation_chromatique_violin.ly")

