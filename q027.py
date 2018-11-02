def run(n):
    return 'el numero {} es de tipo {} ahora es de tipo {}'.format(i, type(i), type(str(i)))


if __name__ == '__main__':
    i = int(input('el numero es '))
    print(run(i))
