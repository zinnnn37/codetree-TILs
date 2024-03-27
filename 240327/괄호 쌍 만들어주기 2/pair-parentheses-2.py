s = input()
length = len(s)

cnt = 0
for i in range(length-3):
    if (s[i] == s[i+1] == '('):
        for j in range(i+1, length-1):
            if (s[j] == s[j+1] == ')'):
                cnt += 1
print(cnt)