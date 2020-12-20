print("Bitte geben Sie Ihr Gehalt ein")
g = input()

#Umrechnung der Eingabe in eine Zahl
Zahl = int(g)

#Berechnung der Steuer vom Gehalt
mZahl = Zahl/100 * 26
bZahl = Zahl/100 * 22
kZahl = Zahl/100 * 18

if Zahl > 4000:
    print("Es ergibt sich eine Steuer von", mZahl)
elif Zahl>= 2500:
    print("Es ergibt sich eine Steuer von", bZahl)
else:
    print("Es ergibt sich eine Steuer von", kZahl)





            #Gehaltsliste zur Orientierung
    """Mehr als 4000 €      26%
      2500€ bis 4000 €      22%
    weniger als 4000 €      18%"""
