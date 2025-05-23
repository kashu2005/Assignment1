from itertools import combinations
n = int(input())
letters = input().split()
k = int(input())
comb = list(combinations(range(n), k))
count = 0
for c in comb:
    if 'a' in [letters[i] for i in c]:
        count += 1
probability = count / len(comb)
print(f"{probability:4f}")
