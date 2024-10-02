from models.abstract.funcionario import Funcionario
from models.endereco import Endereco
from models.enums.sexo import Sexo
from models.enums.setor import Setor

class CreaInvalidoException(Exception):
    pass
class SalarioInvalidoException(Exception):
    pass

class Engenheiro(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cpf: str, rg: str, dataNascimento: str, sexo: Sexo, matricula: str, setor: Setor, salario: float, crea: str) -> None:
        super().__init__(nome, telefone, email, endereco, cpf, rg, dataNascimento, sexo, matricula, setor, salario)

        self.set_crea(crea)

    def set_crea(self, crea: str) -> None:
        if not crea:
            raise CreaInvalidoException("CREA inválido: O número CREA não pode ser vazio.")
        self.crea = crea

    def set_salario(self, salario: float) -> None:
        if salario < 0:
            raise SalarioInvalidoException("Salário inválido: O salário deve ser maior ou igual a zero.")
        self.salario = salario

    def __str__(self) -> str:
        return f"{super().__str__()}\nCREA: {self.crea}"
