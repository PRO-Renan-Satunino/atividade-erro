import pytest
from prjetofinal.models.endereco import Endereco
from prjetofinal.models.enums.setor import Setor
from prjetofinal.models.enums.sexo import Sexo
from prjetofinal.models.advogado import Advogado
from prjetofinal.models.advogado import OabInvalidoException, SalarioInvalidoException

# Mocks para Endereco e outros enums
@pytest.fixture
def endereco_mock():
    return Endereco(...)  # preencha com valores válidos para Endereco

@pytest.fixture
def advogado():
    return Advogado(
        nome="John Doe",
        telefone="123456789",
        email="john@example.com",
        endereco=endereco_mock(),
        cpf="12345678901",
        rg="123456789",
        dataNascimento="1990-01-01",
        sexo=Sexo.MASCULINO,
        matricula="MATRICULA123",
        setor=Setor.EXEMPLO,
        salario=5000.0,
        oab="123456"
    )

def test_advogado_inicializacao(advogado):
    assert advogado.nome == "John Doe"
    assert advogado.telefone == "123456789"
    assert advogado.email == "john@example.com"
    assert advogado.cpf == "12345678901"
    assert advogado.rg == "123456789"
    assert advogado.dataNascimento == "1990-01-01"
    assert advogado.sexo == Sexo.MASCULINO
    assert advogado.matricula == "MATRICULA123"
    assert advogado.setor == Setor.EXEMPLO
    assert advogado.salario == 5000.0
    assert advogado.oab == "123456"

def test_set_oab_invalido():
    with pytest.raises(OabInvalidoException) as excinfo:
        Advogado(
            nome="John Doe",
            telefone="123456789",
            email="john@example.com",
            endereco=endereco_mock(),
            cpf="12345678901",
            rg="123456789",
            dataNascimento="1990-01-01",
            sexo=Sexo.MASCULINO,
            matricula="MATRICULA123",
            setor=Setor.EXEMPLO,
            salario=5000.0,
            oab=""
        )
    assert str(excinfo.value) == "OAB inválido: O número OAB não pode ser vazio."

def test_set_salario_invalido(advogado):
    with pytest.raises(SalarioInvalidoException) as excinfo:
        advog
