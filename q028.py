def run(num):
    return int(num[0]) + int(num[1])


if __name__ == '__main__':
    n = str(input('los numeros son ')).split(',')
    print(run(n))
