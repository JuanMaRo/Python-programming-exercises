class Estudiante(object):
    def __init__(self):
        self.nombre = ''

    def getString(self):
        self.nombre = str(input('Tu nombre es '))

    def printString(self):
        return self.nombre.upper()


if __name__ == '__main__':
    e = Estudiante()
    e.getString()
    print(e.printString())
