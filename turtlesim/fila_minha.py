class fila(list):
    def __init__(self, sequencia):
        super().__init__(item for item in sequencia)
    def append(self, number):
        super().append(number)
    def pop(self):
        super().pop(0)

def main():
    f = fila([1,2,3])
    print(f)
    f.append(5)
    print(f)
    f.pop()
    print(f)

if __name__ == "__main__":
    main()
