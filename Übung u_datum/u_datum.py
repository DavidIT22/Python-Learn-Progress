#Programm zur Prüfung einer Datumsangabe

print("Tag des Datums eingeben:")
t = input()
Tag = int(t)
print("Monat des Datums eingeben:")
m = input()
Monat = int(m)
print("Jahr des Datums:")
Jahr = input()

if Tag < 1 or Tag > 31:
    print("Es handelt sich um ein falsches Datum")
if Monat <1 or Monat > 12:
    print("Es handelt sich um ein falsches Datum")