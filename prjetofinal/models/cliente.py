from models.enums.sexo import Sexo
from models.endereco import Endereco
from models.abstract.fisica import Fisica

class ClienteInvalidoException(Exception):
    pass

class Cliente(Fisica):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cpf: str, rg: str, dataNascimento: str, sexo: Sexo, protocolo: int) -> None:
        super().__init__(nome, telefone, email, endereco, cpf, rg, dataNascimento, sexo)

        self.set_protocolo(protocolo)

    def set_protocolo(self, protocolo: int) -> None:
        if protocolo <= 0:
            raise ClienteInvalidoException("Protocolo inválido: Deve ser um número positivo.")
        self.protocolo = protocolo

    def __str__(self) -> str:
        return f"{super().__str__()}\nProtocolo de Atendimento: {self.protocolo}"
