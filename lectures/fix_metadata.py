import nbformat

# Notebook-Dateipfad
nb_path = "/Users/jplonnigs/Documents/code/Lehre/ProgrammierUebung/lectures/05c_Algorithmen.ipynb"  # Passe das an

print("Analyze: ", nb_path)
# Notebook laden
nb = nbformat.read(nb_path, as_version=4)

# Metadaten setzen, wenn "slideshow" noch nicht existiert
for cell in nb.cells:
    if "slideshow" not in cell.metadata:
        cell.metadata["slideshow"] = {"slide_type": "skip"}
    elif cell.metadata["slideshow"]["slide_type"]!="skip":
        cell.metadata["tags"] = ["remove-cell"]

# Notebook speichern
nbformat.write(nb, nb_path)
print("Metadaten wurden erfolgreich gesetzt.")