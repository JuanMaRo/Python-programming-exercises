import math


def run(x1,x2,y1,y2):
    ecuacion = math.sqrt(((x1-x2)**2) + ((y1-y2)**2))
    print(int(ecuacion))


if __name__ == '__main__':
    x1 = int(input('UP '))
    x2 = int(input('DOWN '))
    y1 = int(input('LEFT '))
    y2 = int(input('RIGHT '))
    run(x1,x2,y1,y2)

#t = 12345, 54321, 'Tom'
#type(t)
#tuple
