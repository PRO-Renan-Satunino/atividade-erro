from abc import ABC, abstractclassmethod
from models.endereco import Endereco #Import Classes

class Pessoa(ABC):
    def __init__(self, idade:int, nome:str, telefone:str, email:str, endereco:Endereco) -> None:
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def __str__(self) -> str:
        return (
            f"\nNome: {self.nome}"
            f"\nIdade: {self.idade}"
            f"\nTelefone: {self.telefone}"
            f"\nEmail: {self.email}"
            f"\n--Endereço-- {self.endereco}"
        )