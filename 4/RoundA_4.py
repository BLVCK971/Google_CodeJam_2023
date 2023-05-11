def find_char_at_position_optimized(position):
    i = 1
    total_chars = 0

    # Trouver la valeur de i pour la position donnée
    while total_chars + 26 * i < position:
        total_chars += 26 * i
        i += 1

    # Calculer le nombre de caractères restant après les cycles complets
    remaining_chars = position - total_chars

    # Trouver le caractère correspondant
    letter_cycle = (remaining_chars - 1) // i
    letter = chr(ord('A') + letter_cycle)

    return letter

# Lecture de l'entrée
T = int(input())
for t in range(T):
    N = int(input())
    result = find_char_at_position_optimized(N)
    print(f"Case #{t+1}: {result}")
