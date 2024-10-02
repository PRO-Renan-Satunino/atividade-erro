from models.abstract.pjuridica import Juridica
from models.endereco import Endereco

class ProdutoInvalidoException(Exception):
    pass

class Fornecedor(Juridica):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricaoEstadual: str, produto: str) -> None:
        super().__init__(nome, telefone, email, endereco, cnpj, inscricaoEstadual)

        self.set_produto(produto)

    def set_produto(self, produto: str) -> None:
        if not produto:
            raise ProdutoInvalidoException("Produto inválido: O nome do produto não pode ser vazio.")
        self.produto = produto

    def __str__(self) -> str:
        return f"{super().__str__()}\nProduto: {self.produto}"
