from models.abstract.fisica import Fisica #Import Abstracts
from models.endereco import Endereco #Import Classes
from models.enums.setor import Setor #Import Enums
from abc import ABC, abstractclassmethod

from models.enums.sexo import Sexo

class Funcionario(Fisica, ABC):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cpf: str, rg: str, dataNascimento: str, sexo: Sexo, matricula:str, setor:Setor, salario:float) -> None:
        super().__init__(nome, telefone, email, endereco, cpf, rg, dataNascimento, sexo)

        self.matricula = matricula
        self.setor = setor
        self.salario = salario

    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nMatricula: {self.matricula}"
            f"\nSetor: {self.setor.value}"
            f"\nSalario: {self.salario}"
        )