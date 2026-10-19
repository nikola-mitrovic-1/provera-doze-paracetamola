# Educational exercise: fictional patients only. Not for clinical use.
imena_u_redu = []
imena_za_proveru = []
u_redu = 0
za_proveru = 0
ponovo = "da"
while ponovo == "da":
  ime = input("Ime pacijenta: ")
  tezina_kg = int(input("Tezina (kg): "))
  alkohol = input("Hronicna upotreba alkohola? (da/ne): ")
  godine = int(input("Godine: "))
  broj_dana = int(input("Koliko dugo dana pijete tablete: "))
  insuficijencija = input("Da li imate insuficijenciju jetre? (da/ne): ")
  tablete = int(input("Tableta po dozi: "))
  doza = int(input("Dnevna doza: "))
  max_tableta_po_dozi = 0
  max_doza_dnevno = 4
  sve_u_redu = True

  if insuficijencija == "da":
    print("Maksimalna dnevna doza tri grama!")
    sve_u_redu = False
  if alkohol == "da":
    print("Oprez!")
    sve_u_redu = False
  if godine <10:
    print ("Tablete od 500mg nisu pogodne. Preporuka: sirup.")
    sve_u_redu = False
  elif godine <= 15:
    max_tableta_po_dozi = 1
  else:
    max_tableta_po_dozi = 2
  if broj_dana > 3:
    print("Konsultujte se sa lekarom")
    sve_u_redu = False
  if doza > max_doza_dnevno:
    print("Prekoracena maksimalna dnevna doza")
    sve_u_redu = False
  if tablete > max_tableta_po_dozi:
    print("Prekoracena maksimalna pojedinacna doza")
    sve_u_redu = False
  if sve_u_redu:
    u_redu = u_redu + 1
    imena_u_redu.append(ime)
  else:
    za_proveru = za_proveru + 1
    imena_za_proveru.append(ime)
  ponovo = input("Jos jedan pacijent (da/ne): ")

print("U redu", imena_u_redu)
for ime_pacijenta in imena_u_redu:
  print(" -", ime_pacijenta)
print("Za proveru", imena_za_proveru,)
for ime_pacijenta in imena_za_proveru:
  print(" -", ime_pacijenta)

print("Brojač:", u_redu, "| len liste:", len(imena_u_redu))

