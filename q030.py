def run(s1,s2):
    if len(s1) == len(s2):
        print(s1)
        print(s2)
    elif len(s1) > len(s2):
        print(s1)
    else:
        print(s2)


if __name__ == '__main__':
    s1 = str(input('~ '))
    s2 = str(input('~ '))
    run(s1,s2)
