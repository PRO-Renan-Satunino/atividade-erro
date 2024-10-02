import pytest
from models.endereco import Endereco
from models.enums.setor import Setor
from models.enums.sexo import Sexo
from models.engenheiro import Engenheiro

# Mocks para Endereco e outros enums
@pytest.fixture
def endereco_mock():
    return Endereco(
        logradouro="Avenida Exemplo",
        numero="456",
        complemento="Sala 3",
        cep="98765-432",
        cidade="Rio de Janeiro",
        uf=UnidadeFederativa.SP  # Ajuste conforme necessário
    )

@pytest.fixture
def engenheiro(endereco_mock):
    return Engenheiro(
        nome="Carlos Mendes",
        telefone="123456789",
        email="carlos@example.com",
        endereco=endereco_mock,
        cpf="98765432100",
        rg="654321987",
        dataNascimento="1988-08-08",
        sexo=Sexo.MASCULINO,
        matricula="ENG123456",
        setor=Setor.ENGENHARIA,
        salario=8000.0,
        crea="1234567890"
    )

def test_engenheiro_inicializacao(engenheiro):
    assert engenheiro.nome == "Carlos Mendes"
    assert engenheiro.telefone == "123456789"
    assert engenheiro.email == "carlos@example.com"
    assert engenheiro.cpf == "98765432100"
    assert engenheiro.rg == "654321987"
    assert engenheiro.dataNascimento == "1988-08-08"
    assert engenheiro.sexo == Sexo.MASCULINO
    assert engenheiro.matricula == "ENG123456"
    assert engenheiro.setor == Setor.ENGENHARIA
    assert engenheiro.salario == 8000.0
    assert engenheiro.crea == "1234567890"

def test_str_method(engenheiro):
    expected_str = (
        f"{engenheiro.nome} - {engenheiro.telefone} - {engenheiro.email} "
        f"\nCrea: {engenheiro.crea}"
    )
    assert str(engenheiro) == expected_str
