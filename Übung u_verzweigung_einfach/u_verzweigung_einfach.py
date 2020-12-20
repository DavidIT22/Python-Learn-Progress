print("Bitte geben Sie Ihr Gehalt ein")
g = input()

#Umrechnung der Eingabe in eine Zahl
Zahl = int(g)

#Berechnung der Steuer vom Gehalt
gZahl = Zahl/100 * 22
kZahl = Zahl/100 * 18

if Zahl >= 2500:
    print("Es ergibt sich eine Steuer von", gZahl)
else:
    print("Es ergibt sich eine Steuer von", kZahl)
    
