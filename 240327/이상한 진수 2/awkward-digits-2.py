n = list(input())
length = len(n)

try:
    idx = n.index('0')
    n[idx] = '1'
except:
    n[-1] = '0'

i = 0
res = 0
while (i <= length):
    res += int(n[length - i - 1]) * pow(2, i)
    i += 1

print(res)