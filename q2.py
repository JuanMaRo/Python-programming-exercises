def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)


if __name__ == '__main__':
    x = int(input('Factorial de '))
    fact(x)
    print(fact(x))

'''def factorial(numero):
    num = 1
    r = []

    for i in range(2, n+1):
        num = num * i
        r.append(str(num))

    print(','.join(r))


if __name__ == '__main__':
    n = int(input('Factorial de '))
    factorial(n)
'''
