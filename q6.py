import math

def formula(num):
    l = n.split(',')
    d = list(map(int, l))
    res = []

    for i in d:
        q = (2 * 50 * i)/30
        r = math.floor(math.sqrt(q))
        res.append(str(r))

    print(','.join(res))


if __name__ == '__main__':
    n = str(input('Tus números son '))
    formula(n)
