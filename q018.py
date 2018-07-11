import string as s

low = list(s.ascii_lowercase)
upp = list(s.ascii_uppercase)
digits = list(s.digits)
characters = ['$','#','@']

def password(texto):
    r = []
    fif = [list(word) for word in pw if len(word) >= 6 and len(word) <= 12] #first filter
    sf = [li for li in fif for i in li if i in characters] #second filter
    tf = [i for i in sf for j in i if j in low] #third filter
    fof = [i for i in tf for j in i if j in upp] #fourth filter
    lf = [i for i in fof for j in i if j in digits] #last filter
    for i in lf:
        if i not in r:
            r.append(i)
    fr = [j for i in r for j in i]

    print('el resultado es ', ''.join(fr))

if __name__ == '__main__':
    pw = str(input('tu contraseñas son ')).split(',')
    password(pw)
