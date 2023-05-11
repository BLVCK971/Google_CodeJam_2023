testcases = int(input())

for case in range(testcases):
    M,R,N = map(int, input().strip().split())
    street_lights = list(map(int, input().strip().split()))
    needed = 0
    i = 0
    covered = 0
    Impossible = False
    while covered < M:
        if i < N and street_lights[i] - R <= covered :
            covered = street_lights[i] + R
            i += 1
            needed += 1
        else:
            Impossible = True
            covered = 9999999
        if(i+1<N):
            if covered > street_lights[i] - R and street_lights[i+1] - R <= covered:
                i += 1

    else:
        print(f"Case #{case+1}: {needed}" if not Impossible else f"Case #{case+1}: IMPOSSIBLE")