testcases = int(input())

for case in range(testcases):
    digits = input().split()
    fail = 0
    codes = []
    # Vérifier si les codes générés ne sont pas redondants
    for words in range(int(input())):
        word = input()
        code = ''.join(digits[ord(digit) - 65] for digit in word)
        codes.append(code)
    print("Case #{}: YES".format(case+1)) if len(set(codes)) < len(codes) else print("Case #{}: NO".format(case+1))
