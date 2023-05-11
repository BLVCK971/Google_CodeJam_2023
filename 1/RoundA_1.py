def colliding_encoding(testcases, data):
    results = []

    for case in range(testcases):
        digits = data.pop(0).split()
        code_set = set()
        num_words = int(data.pop(0))
        is_colliding = False

        for _ in range(num_words):
            word = data.pop(0)
            code = ''.join(digits[ord(digit) - 65] for digit in word)

            if code in code_set:
                is_colliding = True
                break
            else:
                code_set.add(code)

        results.append("Case #{}: {}".format(case + 1, "YES" if is_colliding else "NO"))

    return results


testcases = int(input())
data = []

for _ in range(testcases):
    data.append(input())  # Encoding input
    data.append(input())  # Number of words input
    num_words = int(data[-1])

    for _ in range(num_words):
        data.append(input())  # Word inputs

results = colliding_encoding(testcases, data)

for result in results:
    print(result)
