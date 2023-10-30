class Produto:
    def __init__(self, codigo_barra, nome, preco):
        self.codigo_barra = codigo_barra
        self.nome = nome
        self.preco = preco

class Coleira(Produto):
    def __init__(self, codigo_barra, nome, preco, material):
        super().__init__(codigo_barra, nome, preco)
        self.material = material

class Racao(Produto):
    def __init__(self, codigo_barra, nome, preco, tipo):
        super().__init__(codigo_barra, nome, preco)
        self.tipo = tipo

class Briquedo(Produto):
    def __init__(self, codigo_barra, nome, preco, marca):
        super().__init__(codigo_barra, nome, preco)
        self.marca = marca
