par = input()
length = len(par)
cnt = 0

for i in range(length):
    if par[i] == '(':
        for j in range(i + 1, length):
            if par[j] == ')':
                cnt += 1

print(cnt)