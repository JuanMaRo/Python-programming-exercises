def run(texto):
    s = sorted(t)

    r = []
    for word in s:
        if word not in r:
            r.append(word)

    print(' '.join(r))


if __name__ == '__main__':
    t = str(input('Tu texto es ')).split(' ')
    run(t)
