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
            print('deposito de ${}'.format(dep))
        elif command == 'w':
            w = int(input('retiro de $'))
            dep -= w
            print('deposito de ${}'.format(dep))
        else:
            break


if __name__ == '__main__':
    account()
