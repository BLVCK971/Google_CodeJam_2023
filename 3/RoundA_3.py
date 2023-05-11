def verifier_solution(liste):
    chiffres_uniques = set(liste)
    return len(chiffres_uniques) < len(liste)

def regrouper_chiffres(liste):
    if verifier_solution(liste):
        return "La solution est impossible"
    
    chiffres_uniques = set(liste)
    return list(chiffres_uniques)



# Lecture de l'entrée
T = int(input())
for t in range(T):
    _ = input()
    T = list(map(int, input().strip().split()))
    print(T)
    result = regrouper_chiffres(T)
    print(f"Case #{t+1}: {result}")
