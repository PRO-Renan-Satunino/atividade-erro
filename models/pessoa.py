class NomeInvalidoException(Exception):
    pass

class IdadeNegativaException(Exception):
    pass

class IdadeTipoInvalidoException(Exception):
    pass

class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.set_nome(nome)
        self.idade = self._verificar_idade(idade)

    def set_nome(self, nome: str) -> None:
        if not nome:
            raise NomeInvalidoException("Nome inválido: O nome não pode ser vazio.")
        self.nome = nome

    def _verificar_idade(self, valor: int) -> int:
        self._verificar_idade_tipo_invalido(valor)
        self._verificar_idade_negativa(valor)
        self._verificar_idade_acima_110(valor)
        
        return valor

    def _verificar_idade_tipo_invalido(self, valor) -> None:
        if not isinstance(valor, int):
            raise IdadeTipoInvalidoException("Tipo de dado inválido: A idade deve ter apenas números inteiros.")

    def _verificar_idade_negativa(self, valor: int) -> None:
        if valor < 0:
            raise IdadeNegativaException("Idade negativa: A idade deve ser maior ou igual a zero.")

    def _verificar_idade_acima_110(self, valor: int) -> None:
        if valor > 110:
            raise ValueError("A idade não pode ser maior que 110.")

    def __str__(self) -> str:
        return f'\nNome: {self.nome} \nIdade: {self.idade}'
