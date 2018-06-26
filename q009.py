def run():
    l = []
    while True:
        s = input('')
        if s:
            l.append(s.upper())
        else:
            break;

    for i in l:
        print(i)


if __name__ == '__main__':
    run()
