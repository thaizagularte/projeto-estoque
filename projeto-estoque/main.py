class Ações:
    def __init__(self):
        print("Olá, bem vinde!")

    def adicionarProd(self, prod, max, min):
        self.prod = prod
        self.max = max
        self.min = min
        print(f"Produto {self.prod} maximo {self.max}")
        