# Educational exercise: fictional invoice lines only. Not for real use.
import re
import pandas as pd
from datetime import date

# 1. Podaci (izmišljene fakture)
with open("fakture.txt", encoding="utf-8") as f:
    fakture = f.read().splitlines()

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
