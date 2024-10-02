from models.abstract.funcionario import Funcionario
from models.endereco import Endereco
from models.enums.sexo import Sexo
from models.enums.setor import Setor

class CrmInvalidoException(Exception):
    pass
class SalarioInvalidoException(Exception):
    pass

class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cpf: str, rg: str, dataNascimento: str, sexo: Sexo, matricula: str, setor: Setor, salario: float, crm: str) -> None:
        super().__init__(nome, telefone, email, endereco, cpf, rg, dataNascimento, sexo, matricula, setor, salario)

        self.set_crm(crm)

    def set_crm(self, crm: str) -> None:
        if not crm:
            raise CrmInvalidoException("CRM inválido: O número CRM não pode ser vazio.")
        self.crm = crm

    def set_salario(self, salario: float) -> None:
        if salario < 0:
            raise SalarioInvalidoException("Salário inválido: O salário deve ser maior ou igual a zero.")
        self.salario = salario

    def __str__(self) -> str:
        return f"{super().__str__()}\nCRM: {self.crm}"
