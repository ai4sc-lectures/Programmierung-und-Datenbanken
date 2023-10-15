# Lesson plan
  
main.py
```python3
from replit import db

for k in db.keys():
  print(db[k].value)
```

parse.py
```python3
from replit import db
import json

db.clear()

#Geojson-Datei als Dictionary auslesen
with open("gebaeude.json") as f:
  buildings1 = json.load(f)

#Datei zeilenweise auslesen
with open("gebaeude.csv") as f:
  lines = f.readlines()
  header = lines[0].strip().split(";")
  buildings2 = []
  for row in lines[1:]:
    count = 0
    object = {}
    for col in row.strip().split(";"):
      object[header[count]] = col
      count += 1
    buildings2.append(object)

for b in buildings1 + buildings2:
  db[b["ID"]] = b
```