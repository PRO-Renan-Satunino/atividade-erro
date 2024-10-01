import pytest
from models.pessoa import Pessoa, NomeInvalidoException, IdadeNegativaException, IdadeTipoInvalidoException

def test_pessoa_valida():
    pessoa = Pessoa("Alice", 30)
    assert pessoa.nome == "Alice"
    assert pessoa.idade == 30

def test_nome_vazio():
    with pytest.raises(NomeInvalidoException) as excinfo:
        Pessoa("", 25)
    assert str(excinfo.value) == "Nome inválido: O nome não pode ser vazio."

def test_idade_negativa():
    with pytest.raises(IdadeNegativaException) as excinfo:
        Pessoa("Alice", -5)
    assert str(excinfo.value) == "Idade negativa: A idade deve ser maior ou igual a zero."

def test_idade_tipo_invalido():
    with pytest.raises(IdadeTipoInvalidoException) as excinfo:
        Pessoa("Alice", "vinte")
    assert str(excinfo.value) == "Tipo de dado inválido: A idade deve ter apenas números inteiros."

def test_idade_acima_130():
    with pytest.raises(ValueError) as excinfo:
        Pessoa("Alice", 140)
    assert str(excinfo.value) == "A idade não pode ser maior que 130."
