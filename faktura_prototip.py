# Educational exercise: fictional invoice lines only. Not for real use.
import re
import pandas as pd
from datetime import date

# 1. Podaci (izmišljene fakture)
fakture = ["Paracetamol 500mg x20 | LOT: A1234 | EXP:03/2027 | kol: 10",
           "Ibuprofen 400mg x30 | LOT: B5687 | EXP: 12/2026 | kol: 5",
           "Vitamin C 1000mg x10 | LOT: C9002 | EXP: 06/2028 | kol: 8",
           "Aspirin 500mg x20 | LOT: D3456 | EXP: 01/2027 | kol: 20",
           "Cetirizin 10mg x20 | LOT: E7788 | EXP: 09/2026 | kol: 6",
           "Amoksicilin 500mg x16 | LOT: F1111 | kol: 4",
           "Ibuprofen 200mg x30 | LOT: G2222 | EXP: 5/2027 | kol: 3"]


# 2. Funkcija: čita jedan red fakture i vraća rečnik
def procitaj_red(red):
    naziv = red.split("|")[0].strip()
    lot = re.findall(r"LOT:\s*(\w+)", red)[0]
    nadjeno = re.findall(r"EXP:\s*(\d{1,2}/\d{4})", red)
    if nadjeno:
        rok = nadjeno[0]
        mesec = int(rok.split("/")[0])
        godina = int(rok.split("/")[1])
    else:
        rok = None
        mesec = None
        godina = None
    kol = int(re.findall(r"kol:\s*(\d+)", red)[0])
    return {"naziv": naziv, "lot": lot, "rok": rok,
            "mesec": mesec, "godina": godina, "kol": kol}


# 3. Funkcija: pretvara broj meseci do isteka u status
def status_roka(do_isteka):
    if pd.isna(do_isteka):
        return "nema roka"
    elif do_isteka < 0:
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

# 5. Racunanje danasnjeg datuma'

danas = date.today()

# 6. Računamo koliko meseci je ostalo do isteka roka
tabela["ukupno_meseci"] = tabela["godina"] * 12 + tabela["mesec"]
danas_meseci = danas.year * 12 + danas.month
tabela["do_isteka"] = tabela["ukupno_meseci"] - danas_meseci
tabela["status"] = tabela["do_isteka"].apply(status_roka)
print(tabela[tabela["status"] == "nema roka"])
print(tabela)

# 7. Samo lekovi koji ističu u narednih 6 meseci
print(tabela[(tabela["do_isteka"] >= 0) & (tabela["do_isteka"] <= 6)])

tabela.to_csv("fakture_rokovi.csv", index=False)
