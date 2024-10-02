from models.abstract.funcionario import Funcionario #Import Abstracts
from models.endereco import Endereco #Import Classes
#Import Enums
from models.enums.setor import Setor
from models.enums.sexo import Sexo

# Exceções 
class NomeInvalidoException(Exception):
    pass

class TelefoneInvalidoException(Exception):
    pass

class EmailInvalidoException(Exception):
    pass

class CpfInvalidoException(Exception):
    pass

class RgInvalidoException(Exception):
    pass

class OabInvalidoException(Exception):
    pass

class SalarioInvalidoException(Exception):
    pass

#Classe
class Advogado(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cpf: str, rg: str, dataNascimento: str, sexo: Sexo, matricula: str, setor: Setor, salario: float, oab: str) -> None:
        super().__init__(nome, telefone, email, endereco, cpf, rg, dataNascimento, sexo, matricula, setor, salario)

        self.set_oab(oab)

    def set_oab(self, oab: str) -> None:
        if not oab:
            raise OabInvalidoException("OAB inválido: O número OAB não pode ser vazio.")
        # Adicione outras validações de OAB se necessário
        self.oab = oab

    def set_salario(self, salario: float) -> None:
        if salario < 0:
            raise SalarioInvalidoException("Salário inválido: O salário deve ser maior ou igual a zero.")
        self.salario = salario

    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nOAB: {self.oab}"               
        )