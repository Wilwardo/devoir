"""NOM ET PRENOM: Wilwardo DISANGO NGUI"""


"""ce programme demande un numéro de mois à l’utilisateur et
affiche le nom et le nombre de jours correspondant au numéro de mois
"""

mois = input("Le numéro de mois: ")

if mois == "1":
    print("janvier (31 jours)")
elif mois == "2":
    print("février (28 ou 29 jours)")
elif mois == "3":
    print("mars (31 jours)")
elif mois == "4":
    print("avril (30 jours)")
elif mois == "5":
    print("mai (31 jours)")
elif mois == "6":
    print("juin (30 jours)")
elif mois == "7":
    print("juillet (31 jours)")
elif mois == "8":
    print("août (31 jours)")
elif mois == "9":
    print("septembre (30 jours)")
elif mois == "10":
    print("octobre (31 jours)")
elif mois == "11":
    print("novembre (30 jours)")
elif mois == "12":
    print("décembre (31 jours)")
else:
    print("numéro invalide")



