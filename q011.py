'''value = []
items=[x for x in input().split(',')]
for p in items:
    intp = int(p, 2)
    if not intp%5:
        value.append(p)

print(','.join(value))'''


def run(num):
    ent = [int(i, 2) for i in n]
    r = [str(i) for i in ent if i % 5 == 0]

    print(','.join(r))


if __name__ == '__main__':
    n = str(input('tus numeros BINARIOS son ')).split(',')
    run(n)
