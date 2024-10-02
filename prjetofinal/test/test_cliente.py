import pytest
from models.endereco import Endereco
from models.enums.sexo import Sexo
from models.cliente import Cliente

# Mocks para Endereco e outros enums
@pytest.fixture
def endereco_mock():
    return Endereco(...)  # preencha com valores válidos para Endereco

@pytest.fixture
def cliente():
    return Cliente(
        nome="Maria Silva",
        telefone="987654321",
        email="maria@example.com",
        endereco=endereco_mock(),
        cpf="12345678901",
        rg="987654321",
        dataNascimento="1985-05-05",
        sexo=Sexo.FEMININO,
        protocolo=123456
    )

def test_cliente_inicializacao(cliente):
    assert cliente.nome == "Maria Silva"
    assert cliente.telefone == "987654321"
    assert cliente.email == "maria@example.com"
    assert cliente.cpf == "12345678901"
    assert cliente.rg == "987654321"
    assert cliente.dataNascimento == "1985-05-05"
    assert cliente.sexo == Sexo.FEMININO
    assert cliente.protocolo == 123456

def test_str_method(cliente):
    expected_str = (
        f"{cliente.nome} - {cliente.telefone} - {cliente.email} "
        f"\nProtocolo de Atendimento: {cliente.protocolo}"
    )
    assert str(cliente) == expected_str
