def run():
    rl=[]
    for i in range(1000,3001):
        n = str(i)
        if (int(n[0])%2==0) and (int(n[1])%2==0) and (int(n[2])%2==0) and (int(n[3])%2==0):
            rl.append(n)

    print(','.join(rl))


if __name__ == '__main__':
    run()
