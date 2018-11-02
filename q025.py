class Perro:
    def __init__(self):
        self.nombre = 'Firulais'
        self.ladrido = str(input('el dice '))
        self.patas = int(input('cuantas patas tiene '))

        print('{} es un perro que ladra {} y tiene {} patas'.format(self.nombre, self.ladrido, self.patas))


if __name__ == '__main__':
    p = Perro()
