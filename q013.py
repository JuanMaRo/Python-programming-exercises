def run(num):
    letter = 0
    digits = 0

    for i in x:
        for d in i:
            try:
                if int(d)==True:
                    print(d)
            except ValueError:
                letter = letter + 1
            else:
                digits = digits + 1

    print('LETTERS {}'.format(letter))
    print('DIGITS {}'.format(digits))


if __name__ == '__main__':
    x = input('').split(' ')
    run(x)
