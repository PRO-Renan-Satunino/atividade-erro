import pytest
from models.endereco import Endereco
from models.enums.setor import Setor
from models.enums.sexo import Sexo
from models.medico import Medico

# Mocks para Endereco e outros enums
@pytest.fixture
def endereco_mock():
    return Endereco(
        logradouro="Rua da Saúde",
        numero="101",
        complemento="Apto 4B",
        cep="12345-678",
        cidade="Belo Horizonte",
        uf="MG"  # Ajuste conforme necessário
    )

@pytest.fixture
def medico(endereco_mock):
    return Medico(
        nome="Dr. João Silva",
        telefone="987654321",
        email="joao@example.com",
        endereco=endereco_mock,
        cpf="12345678909",
        rg="987654321",
        dataNascimento="1975-12-30",
        sexo=Sexo.MASCULINO,
        matricula="MED123456",
        setor=Setor.SAÚDE,
        salario=15000.0,
        crm="12345"
    )

def test_medico_inicializacao(medico):
    assert medico.nome == "Dr. João Silva"
    assert medico.telefone == "987654321"
    assert medico.email == "joao@example.com"
    assert medico.cpf == "12345678909"
    assert medico.rg == "987654321"
    assert medico.dataNascimento == "1975-12-30"
    assert medico.sexo == Sexo.MASCULINO
    assert medico.matricula == "MED123456"
    assert medico.setor == Setor.SAÚDE
    assert medico.salario == 15000.0
    assert medico.crm == "12345"

def test_str_method(medico):
    expected_str = (
        f"{medico.nome} - {medico.telefone} - {medico.email} "
        f"\nCRM: {medico.crm}"
    )
    assert str(medico) == expected_str
