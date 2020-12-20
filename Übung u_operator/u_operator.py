#Berechnung der Steuer mit berücksichtigung des Familienstands

print("Bitte geben Sie Ihr Gehalt ein")
g = input()
#Umrechnung der Eingabe in eine Zahl
Zahl = int(g)

print("Sind Sie Verheiratet oder Ledig?")
stand = input()



#Berechnung der Steuer vom Gehalt
mZahl = Zahl * 0.26
bZahl = Zahl * 0.22
kZahl = Zahl * 0.18

if Zahl > 4000 and stand == "ledig":
    print("Es ergibt sich eine Steuer von", mZahl)
    
elif Zahl > 4000 and stand == "Verheiratet":
    print("Es ergibt sich eine Steuer von", bZahl)
    
elif Zahl <= 4000 and stand == "Ledig":
    print("Es ergibt sich eine Steuer von", bZahl)
    
else:
    print("Es ergibt sich eine Steuer von", kZahl)





            #Gehaltsliste zur Orientierung
    """         >4000€  Ledig          26%
                >4000€  Verheiratet    22%
                <=4000€ Ledig          18%
                <=4000€ Verheiratet    18%   """
