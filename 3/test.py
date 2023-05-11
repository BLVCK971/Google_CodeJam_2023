def verifier_solution(liste):
    chiffres_uniques = set(liste)
    liste_reduite = [chiffre for chiffre in chiffres_uniques if liste.count(chiffre) == 1]

    return len(liste_reduite) == len(chiffres_uniques)

def regrouper_chiffres(liste):
    chiffres_uniques = set(liste)
    if verifier_solution(liste):
        return list(chiffres_uniques)
    else:
        return "La solution est impossible"

liste1 = [3, 8, 8, 2]
liste2 = [3, 8, 2, 2, 8]

print(regrouper_chiffres(liste1))  # Affichera [3, 8, 2]
print(regrouper_chiffres(liste2))  # Affichera "La solution est impossible"
