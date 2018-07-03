d = {'UPPER CASE':0, 'LOWER CASE':0}

def run(texto):
    for i in x:
        if i.isupper():
            d['UPPER CASE']+=1
        elif i.islower():
            d['LOWER CASE']+=1

    print('UPPER CASE {}'.format(d['UPPER CASE']))
    print('LOWER CASE {}'.format(d['LOWER CASE']))


if __name__ == '__main__':
    x = str(input('Tu texto es '))
    run(x)
