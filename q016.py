def run(texto):
    rl = [i for i in x if int(i)%2==1]
    print(','.join(rl))


if __name__ == '__main__':
    x = str(input('Tus numeros son ')).split(',')
    run(x)
