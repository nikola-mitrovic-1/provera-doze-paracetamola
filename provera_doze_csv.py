   # Educational exercise: fictional patients only. Not for clinical use.
import csv

pacijenti = []
with open("pacijent.csv") as f:
  citac = csv.DictReader(f)
  for red in citac:
    pacijenti.append({
        "ime": red["ime"],
        "godine": int(red["godine"]),
        "tablete": int(red["tablete"]),
        "dani": int(red["dani"]),
        "alkohol": red["alkohol"]
    })

def proveri_pacijenta(p):
  razlozi = []
  max_tableta = max_tableta_po_godinama(p["godine"])
  if p["tablete"] > max_tableta:
    razlozi.append("prekoracena pojedinacna doza")
  if p["dani"] > 3:
    razlozi.append("terapija duza od 3 dana")
  if p["alkohol"] == "da":
    razlozi.append("Oprez - alkohol!")

  return razlozi

def max_tableta_po_godinama(godine):
  if godine < 10:
    return 0
  elif godine <=15:
    return 1
  else:
    return 2
print(pacijenti[0])

for p in pacijenti:
  razlozi = proveri_pacijenta(p)
  if len(razlozi) == 0:
    print(p["ime"], "- u redu")
  else:
    print(p["ime"], "- za proveru")
    for r in razlozi:
      print(" -", r)



