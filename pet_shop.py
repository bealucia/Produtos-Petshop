from enum import Enum

# Marcas dos produtos enumeradas 
class Marca(Enum):
    PEDIGREE = 1
    WHISKAS = 2
    QUATREE = 3

# Produtos gerais de Petshop
class Produto:
    def __init__(self, codigo_barra, nome, preco, Marca):
        self.codigo_barra = codigo_barra
        self.nome = nome
        self.preco = preco
        self.marca = Marca

class Coleira(Produto):
    def __init__(self, codigo_barra, nome, preco, Marca, material):
        super().__init__(codigo_barra, nome, preco)
        self.material = material

class Racao(Produto):
    def __init__(self, codigo_barra, nome, preco, Marca, sabor):
        super().__init__(codigo_barra, nome, preco)
        self.sabor = sabor

class Brinquedo(Produto):
    def __init__(self, codigo_barra, nome, preco, Marca, tipo):
        super().__init__(codigo_barra, nome, preco)
        self.tipo = tipo

class Inventario:
    def __init__(self):
        self.estoque = []

    def adicionar_produto(self, produto, quantidade):
        if quantidade < 0:
            raise QuantidadeInvalidaException("A quantidade de produtos deve ser um número positivo.")
        self.estoque.extend([produto] * quantidade)

    def retornar_produto(self, produto):
        if produto not in self.estoque:
            raise ProdutoNaoEncontradoException("O produto não está no estoque e não pode ser retornado.")
        self.estoque.remove(produto)

def vender_produto(estoque, codigo_barra):
    if not estoque:
        raise EstoqueVazioException("O estoque está vazio.")
    for produto in estoque:
        if produto.codigo_barra == codigo_barra:
            estoque.remove(produto)
            return produto
    raise ProdutoNaoEncontradoException(f"Produto com código de barras {codigo_barra} não encontrado no estoque.")

# Exceções 
class ProdutoNaoEncontradoException(Exception):
    pass

class EstoqueVazioException(Exception):
    pass

class QuantidadeInvalidaException(Exception):
    pass

