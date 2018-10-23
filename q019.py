import operator


def run(t1,t2,t3,t4,t5):
    peopleTuples = [t1,t2,t3,t4,t5]
    print(sorted(peopleTuples, key=operator.itemgetter(0,1,2)))


if __name__ == '__main__':
    t1 = tuple(str(input()).split(','))
    t2 = tuple(str(input()).split(','))
    t3 = tuple(str(input()).split(','))
    t4 = tuple(str(input()).split(','))
    t5 = tuple(str(input()).split(','))
    run(t1,t2,t3,t4,t5)
