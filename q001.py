def run():
    n = []

    for i in range(2000, 3201):
        if i % 7 == 0 and not i % 5 == 0:
            n.append(str(i))

    print(','.join(n))

if __name__ == '__main__':
    run()

'''
n = [str(i) for i in range(2000, 3201) if i % 7 == 0 and not i % 5 == 0]
'''
