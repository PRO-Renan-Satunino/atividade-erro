import pytest
from models.endereco import Endereco
from models.abstract.pjuridica import Juridica  # Ajuste conforme necessário
from models.fornecedor import Fornecedor

# Mocks para Endereco
@pytest.fixture
def endereco_mock():
    return Endereco(
        logradouro="Rua Fornecedor",
        numero="789",
        complemento="Sala 2",
        cep="12345-678",
        cidade="São Paulo",
        uf="SP"  # Ajuste conforme necessário
    )

@pytest.fixture
def fornecedor(endereco_mock):
    return Fornecedor(
        nome="Fornecedor Exemplo Ltda",
        telefone="123456789",
        email="fornecedor@example.com",
        endereco=endereco_mock,
        cnpj="12.345.678/0001-95",
        inscricaoEstadual="1234567890",
        produto="Produto Exemplo"
    )

def test_fornecedor_inicializacao(fornecedor):
    assert fornecedor.nome == "Fornecedor Exemplo Ltda"
    assert fornecedor.telefone == "123456789"
    assert fornecedor.email == "fornecedor@example.com"
    assert fornecedor.cnpj == "12.345.678/0001-95"
    assert fornecedor.inscricaoEstadual == "1234567890"
    assert fornecedor.produto == "Produto Exemplo"

def test_str_method(fornecedor):
    expected_str = (
        f"{fornecedor.nome} - {fornecedor.telefone} - {fornecedor.email} "
        f"\nProduto: {fornecedor.produto}"
    )
    assert str(fornecedor) == expected_str
