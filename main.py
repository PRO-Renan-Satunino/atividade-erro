from models.pessoa import Pessoa, NomeInvalidoException, IdadeNegativaException, IdadeTipoInvalidoException
import os

os.system ("clear || cls")

def main():
    try:
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        
        pessoa = Pessoa(nome, idade)
        print(f'Pessoa criada com sucesso: {pessoa}')
        
    except (NomeInvalidoException, IdadeNegativaException, IdadeTipoInvalidoException, ValueError) as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
