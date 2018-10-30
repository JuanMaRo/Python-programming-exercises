def run(string):
    d = {}
    for i in s:
        if i not in d:
            d[i] = 1
        elif i in d:
            d[i] += 1

    for key, value in sorted(d.items()):
        print('{}:{}'.format(key, value))


if __name__ == '__main__':
    s = str(input('~ ')).split(' ')
    run(s)
