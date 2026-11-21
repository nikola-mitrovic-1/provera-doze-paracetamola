# Educational exercise: fictional invoice lines only. Not for real use.
import re
import pandas as pd

fakture = ["Paracetamol 500mg x20 | LOT: A1234 | EXP:03/2027 | kol: 10",
           "Ibuprofen 400mg x30 | LOT: B5687 | EXP: 12/2026 | kol: 5",
           "Vitamin C 1000mg x10 | LOT: C9002 | EXP: 06/2028 | kol: 8",
           "Aspirin 500mg x20 | LOT: D3456 | EXP: 01/2027 | kol: 20"]

def procitaj_red(red):
    naziv = red.split("|")[0].strip()
    lot = re.findall(r"LOT:\s*(\w+)", red)[0]
    rok = re.findall(r"EXP:\s*(\d{2}/\d{4})", red)[0]
    mesec = int(rok.split("/")[0])
    godina = int(rok.split("/")[1])
    kol = int(re.findall(r"kol:\s*(\d+)", red)[0])
    return {"naziv": naziv, "lot": lot, "rok": rok,
            "mesec": mesec, "godina": godina, "kol": kol}

redovi = []
for red in fakture:
    redovi.append(procitaj_red(red))

tabela = pd.DataFrame(redovi)
print(tabela)

print(tabela[tabela["godina"] <= 2026])
