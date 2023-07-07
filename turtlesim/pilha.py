class Pilha (list):
    def  __init__(self, sequencia):
        super().__init__(item for item in sequencia)
    def append(self,x):
        super().append(x)
    def pop(self):
        return super().pop(-1)

def main():
    f = Pilha([1,2,3,4])
    print(f)
    f.append(5)
    print(f)
    f.pop()
    print(f)

if __name__ == "__main__":
    main()