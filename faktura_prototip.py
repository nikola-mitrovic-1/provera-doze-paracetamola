# Educational exercise: fictional invoice lines only. Not for real use.
import re
import pandas as pd
from datetime import date

# 1. Podaci (izmišljene fakture)
fakture = ["Paracetamol 500mg x20 | LOT: A1234 | EXP:03/2027 | kol: 10",
           "Ibuprofen 400mg x30 | LOT: B5687 | EXP: 12/2026 | kol: 5",
           "Vitamin C 1000mg x10 | LOT: C9002 | EXP: 06/2028 | kol: 8",
           "Aspirin 500mg x20 | LOT: D3456 | EXP: 01/2027 | kol: 20",
           "Cetirizin 10mg x20 | LOT: E7788 | EXP: 09/2026 | kol: 6"]


# 2. Funkcija: čita jedan red fakture i vraća rečnik
def procitaj_red(red):
    naziv = red.split("|")[0].strip()
    lot = re.findall(r"LOT:\s*(\w+)", red)[0]
    rok = re.findall(r"EXP:\s*(\d{2}/\d{4})", red)[0]
    mesec = int(rok.split("/")[0])
    godina = int(rok.split("/")[1])
    kol = int(re.findall(r"kol:\s*(\d+)", red)[0])
    return {"naziv": naziv, "lot": lot, "rok": rok,
            "mesec": mesec, "godina": godina, "kol": kol}


# 3. Funkcija: pretvara broj meseci do isteka u status
def status_roka(do_isteka):
    if do_isteka < 0:
        return "istekao"
    elif do_isteka <= 6:
        return "istice uskoro"
    else:
        return "u redu"


# 4. Pravimo tabelu od svih faktura
redovi = []
for red in fakture:
    redovi.append(procitaj_red(red))

tabela = pd.DataFrame(redovi)

# 5. Računamo koliko meseci je ostalo do isteka roka
# Današnji datum uzimamo iz sistema (date.today())
danas = date.today()
tabela["ukupno_meseci"] = tabela["godina"] * 12 + tabela["mesec"]
danas_meseci = danas.year * 12 + danas.month
tabela["do_isteka"] = tabela["ukupno_meseci"] - danas_meseci
tabela["status"] = tabela["do_isteka"].apply(status_roka)

print(tabela)

# 6. Samo lekovi koji ističu u narednih 6 meseci
print(tabela[(tabela["do_isteka"] >= 0) & (tabela["do_isteka"] <= 6)])
