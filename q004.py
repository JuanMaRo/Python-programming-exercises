def run(x):
    lista = x.split(',')
    t = tuple(lista)
    print(lista)
    print(t)


if __name__ == '__main__':
    x = str(input('tu lista de números es '))
    run(x)
