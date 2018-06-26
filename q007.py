def run(valor):
    x = int(c[0])
    y = int(c[1])

    l = [[i*row for row in range(y)] for i in range(x)]

    print(l)


if __name__ == '__main__':
    print('''
        El programa construira un array de dos dimensiones
    ''')
    c = input('¿Cuál es el tamaño de tu array? ').split(',')
    run(c)
