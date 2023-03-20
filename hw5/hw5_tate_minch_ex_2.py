def take(n, seq):
    seq = iter(seq)
    result = []
    try:
        result = [next(seq) for i in range(n)]
    except StopIteration:
        pass
    return result

def pythagoreanTriplets():
    c, m = 0,2
    count = 0
    while True:
        for i in range(1,m):
            a = m**2 - i**2
            b = 2*m*i
            c = m**2+i**2

            yield (a,b,c)
            count += 1
        m+=1

def main():
    pyt = pythagoreanTriplets()
    print(take(10,pyt))

if __name__ == '__main__':
    main()
