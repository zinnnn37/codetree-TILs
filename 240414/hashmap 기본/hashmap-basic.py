n = int(input())

if __name__ == '__main__':
    d = dict()

    for _ in range(n):
        cmd = list(input().split())

        if cmd[0] == 'add':
            d[int(cmd[1])] = int(cmd[2])
        elif cmd[0] == 'remove':
            del d[int(cmd[1])]
        elif cmd[0] == 'find':
            try:
                print(d[int(cmd[1])])
            except:
                print('None')