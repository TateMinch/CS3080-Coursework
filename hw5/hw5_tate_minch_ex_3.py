from sys import getsizeof
def genRange(stop,start = 0,step = 1):
    i = start
    while i < stop:
        yield i
        i+=step

def main():
    for i in genRange(10,0,2):
        print(i)

if __name__ == '__main__':
    main()
