def pop(a, b):
    tmp = []
    
    for i in range(a-1):
        tmp.append(lst[i])

    for i in range(b, len(lst)):
        tmp.append(lst[i])

    return tmp

if __name__ == '__main__':
    n = int(input())
    lst = []
    for _ in range(n):
        lst.append(input())
    s1, e1 = list(map(int, input().split()))
    s2, e2 = list(map(int, input().split()))
    
    lst = pop(s1, e1)
    lst = pop(s2, e2)

    print(len(lst))
    print('\n'.join(lst))