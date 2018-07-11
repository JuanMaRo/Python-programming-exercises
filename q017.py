#deposit, withdrawal

def account():
    dep = 0
    while True:
        command = str(input('''
            [d] deposito
            [w] retiro
            [s] salir
        '''))
        if command == 'd':
            d = int(input('deposito de $'))
            dep += d
        elif command == 'w':
            w = int(input('retiro de $'))
            print('deposito de ${}'.format(dep - w))
        else:
            break


if __name__ == '__main__':
    account()
