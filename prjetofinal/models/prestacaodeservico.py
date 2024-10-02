from models.abstract.pjuridica import Juridica
from models.endereco import Endereco

class CnpjInvalidoException(Exception):
    pass

class PrestacaoDeServico(Juridica):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricaoEstadual: str, iniciocontrato: str, fimcontrato: str) -> None:
        super().__init__(nome, telefone, email, endereco, cnpj, inscricaoEstadual)

        self.set_iniciocontrato(iniciocontrato)
        self.set_fimcontrato(fimcontrato)

    def set_iniciocontrato(self, iniciocontrato: str) -> None:
        if not iniciocontrato:
            raise ValueError("Data de início do contrato inválida: Não pode ser vazia.")
        self.iniciocontrato = iniciocontrato

    def set_fimcontrato(self, fimcontrato: str) -> None:
        if not fimcontrato:
            raise ValueError("Data de fim do contrato inválida: Não pode ser vazia.")
        self.fimcontrato = fimcontrato

    def __str__(self) -> str:
        return f"{super().__str__()}\nInicio do Contrato: {self.iniciocontrato}\nFim do Contrato: {self.fimcontrato}"
