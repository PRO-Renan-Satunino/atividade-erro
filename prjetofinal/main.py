from models.enums.sexo import Sexo
from models.enums.setor import Setor
from models.endereco import Endereco
from models.enums.uf import UnidadeFederativa
from models.advogado import Advogado, CpfInvalidoException, EmailInvalidoException, NomeInvalidoException, OabInvalidoException, RgInvalidoException, SalarioInvalidoException, TelefoneInvalidoException
from models.cliente import Cliente
from models.fornecedor import Fornecedor
from models.prestacaodeservico import PrestacaoDeServico
from models.medico import Medico
from models.engenheiro import Engenheiro


import os

os.system ("clear || cls")

#Programa Principal

#Cliente 1
endereco1 = Endereco ("Rua das Flores", "01", "Depois da Prefeitura", "41200-444", "Salvador", UnidadeFederativa.BA)
cliente1 = Cliente ("Joao", "71 90000-0000", "jaozin@gmail.com", endereco1, "222.333.444-55", "22.333.444.55", "11/09/2001", Sexo.MASCULINO, 4444222)

#Advogado 1
endereco2 = Endereco ("Rua dos Advogado", "55", "STF", "44111-222", "Sao Paulo", UnidadeFederativa.SP)
advog1 = Advogado ("Xandinho", "11 92222-2222", "xandinhomusk@spacex.com", endereco2, "666.666.777-77", "21.221.112-11", "12/12/1986", Sexo.MASCULINO, "2222222", Setor.JURIDICO, 60000, "Aprovado")

#Engenheiro 1
endereco3 = Endereco ("GDM City", "8", "Encontro de carros", "33333-333", "Rio de Janeiro", UnidadeFederativa.RJ)
enge1 = Engenheiro ("Dominic Toretto", "09 91222-2222", "domtoretto@hotmail.com", endereco3, "222.111.000-66", "21.222.111-22", "21/06/1993", Sexo.MASCULINO, "2222222", Setor.OPERACOES, 3444, "Aprovado")

#Medico 1
endereco4 = Endereco ("Californa City", "11", "Casa branca", "22222-222", "Jurassic Park", UnidadeFederativa.AC)
medica1 = Medico ("Grey", "21 9333-2211", "dragrey@gmail.com", endereco4, "222.111.111-29", "21.222.111", "01/01/1001", Sexo.FEMININO, "212121", Setor.SAUDE, 30000, "Positivo")

#Fornecedor
endereco5 = Endereco ("Comercio", "22", "no comercio", "222222", "Salvador", UnidadeFederativa.BA)
spacesooftx = Fornecedor ("SpaceSooftx", "21 92222-1111", "contato@spcsftx.org", endereco5, "21212121", "Aprovado", "Aplicativos")

#Prestacao de Servico
prestador = PrestacaoDeServico("Google", "71 9.92929229", "askaska@gmail.com", endereco5, "21212121", "Aprovador", "12/03/2010", "22/02/2025")

#Mostrando Resultados
print(f"\n {enge1}")
print(f"\n {medica1}")
print(f"\n {advog1}")
print(f"\n {spacesooftx}")
print(f"\n {cliente1}")
print(f"\n{prestador}")