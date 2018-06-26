def run(x):
    mi_diccionario = {i:i**2 for i in range(1, n + 1)}
    print(mi_diccionario)


if __name__ == '__main__':
    n = int(input('Es el limite de una lista de potencias '))
    run(n)
