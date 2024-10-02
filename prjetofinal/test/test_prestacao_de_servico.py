import pytest
from models.endereco import Endereco
from models.abstract.pjuridica import Juridica  # Ajuste conforme necessário
from models.prestacao_de_servico import PrestacaoDeServico

# Mock para Endereco
@pytest.fixture
def endereco_mock():
    return Endereco(
        logradouro="Avenida do Serviço",
        numero="123",
        complemento="Sala 5",
        cep="45678-910",
        cidade="Curitiba",
        uf="PR"  # Ajuste conforme necessário
    )

@pytest.fixture
def prestacao_de_servico(endereco_mock):
    return PrestacaoDeServico(
        nome="Serviço Exemplo Ltda",
        telefone="321654987",
        email="servico@example.com",
        endereco=endereco_mock,
        cnpj="12.345.678/0001-95",
        inscricaoEstadual="9876543210",
        iniciocontrato="2023-01-01",
        fimcontrato="2024-01-01"
    )

def test_prestacao_de_servico_inicializacao(prestacao_de_servico):
    assert prestacao_de_servico.nome == "Serviço Exemplo Ltda"
    assert prestacao_de_servico.telefone == "321654987"
    assert prestacao_de_servico.email == "servico@example.com"
    assert prestacao_de_servico.cnpj == "12.345.678/0001-95"
    assert prestacao_de_servico.inscricaoEstadual == "9876543210"
    assert prestacao_de_servico.iniciocontrato == "2023-01-01"
    assert prestacao_de_servico.fimcontrato == "2024-01-01"

def test_str_method(prestacao_de_servico):
    expected_str = (
        f"{prestacao_de_servico.nome} - {prestacao_de_servico.telefone} - {prestacao_de_servico.email} "
        f"\nInicio do Contrato: {prestacao_de_servico.iniciocontrato}"
        f"\nFim do Contrato: {prestacao_de_servico.fimcontrato}"
    )
    assert str(prestacao_de_servico) == expected_str
