class Numbers:
    def __init__(self, rango):
        self.rango = range(0, rango + 1)

    def div(self):
        r = [i for i in self.rango if i % 7 == 0]
        print(r)


if __name__ == '__main__':
    n = Numbers(rango=int(input('El maximo es ')))
    n.div()
