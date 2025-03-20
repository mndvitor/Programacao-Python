# Exercícios com funções:

# 1 CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar).
#  UTILIZE VARIÁVEIS LOCAIS.

def compare ():
    p1 = float(input("Insira um numero: "))
    i1 = float(input("Insira um numero: "))
    sum (p1,i1)
    if sum % 2 == 0:
        print("Numero Par")
    else:
        print("Numero Impar")

compare()

# 2 CRIE UMA FUNÇÃO PARA MULTIPLICAR 3 NUMEROS.

def multi ():
    m1 = float(input("Digite o numero: "))
    m2 = float(input("Digite o numero: "))
    m3 = float(input("Digite o numero: "))
    multiplicar = m1 * m2 * m3
    print(multiplicar)

multi()

# 3 CRIE UMA FUNÇÃO PARA DESCOBRIR O VALOR ELEVADO DE UM NÚMERO.

def elevado ():
    e1 = float(input("Digite o numero: "))
    print(e1**2)

elevado()

# 4 CRIE UMA FUNÇÃO PARA MOSTRAR UMA MENSAGEM PERSONALIZADA NA TELA, 
# SE O USUÁRIO  DIGITAR, 18 ANOS
def mensagem ():
    digite = int(input('Digite sua idade: '))
    if digite == 18 :
        print("Parabens, mensagem premiada")
    else :
        print("Você nao tem a idade premiada")

mensagem ()

# 5 DESENVOLVA UMA FUNÇÃO PARA DESCOBRIR A IDADE DE UMA PESSOA.

def idade ():
    ano_nasc = int(input('Digite o ano que nasceu: '))
    descubra = ano_nasc - 2025
    print(descubra)

idade()

# 6 DESENVOLVA UM AFUNÇÃO PARA VER SE O BRASIL GANHOU A COPA DE 1999

# 7 DESENVOLVA UM SISTEMA DE RESTAURANTE,
# ONDE O CLIENTE TEM OPÇÃO DE ESCOLHER ENTRE
# SALADA, MACARRONADA, SANDUICHE, SORVETE.

def restaurante():
    menu = ["Salada", "Macarronada", "Sanduiche", "Sorvete"]
    escolha = int(input( f'''Seja bem vindo ao Restaurante
          O que você deseja ?
          0 - Salada
          1 - Macarronada
          2 - Sanduiche
          3 - Sorvete
:'''))
    if escolha == 0 :
        print("Combinado, Nós iremos trazer ", menu[0])
    elif escolha == 1 :
        print("Combinado, Nós iremos trazer ", menu[1])
    elif escolha == 2 :
        print("Combinado, Nós iremos trazer ", menu[2])
    elif escolha == 3 :
        print("Combinado, Nós iremos trazer ", menu[3])
    


# restaurante()
