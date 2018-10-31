def run():
    '''\nfunction run
    Print the documentation of abs(), int(), input()
    '''
    print('function abs\n', abs.__doc__)
    print('\nfunction int\n', int.__doc__)
    print('\nfunction input\n', input.__doc__)


if __name__ == '__main__':
    run()
    print(run.__doc__)
