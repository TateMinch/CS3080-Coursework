class ReverseIter():
    def __init__(self, items:list):
        self.items = items
        self.a = len(items)

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > 0:
            x = self.items[self.a-1]
            self.a -= 1
            return x
        else:
            raise StopIteration


def main():
    it = ReverseIter([1,2,3,4])
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))

if __name__ == '__main__':
    main()
