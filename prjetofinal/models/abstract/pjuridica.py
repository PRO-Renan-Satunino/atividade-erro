from models.abstract.pessoa import Pessoa #Import Abstracts
from models.endereco import Endereco #Import Classes
from abc import ABC, abstractclassmethod

class Juridica(Pessoa, ABC):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricaoEstadual: str) -> None:
        super().__init__(nome, telefone, email, endereco)

        self.cnpj = cnpj
        self.inscricaoEstadual = inscricaoEstadual

    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nCNPJ: {self.cnpj}"
            f"\nInscrição Estadual: {self.inscricaoEstadual}"
        ) 