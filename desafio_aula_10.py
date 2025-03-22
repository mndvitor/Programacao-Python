# Desafio 1

# VOCÊ É UM DEV E PRECISA CRIAR UM action PARA UMA ESCOLA. 
# SISTEMA DE NOTAS DE ALUNOS QUE MOSTRE COM ESTATISTICA
# A MODA MEDIA E DESVIO DE PADRÃO, DAS NOTAS DE ALUNOS,
# ALÉM DE MOSTRAR A MENOR E A MAIOR NOTA, SEPARE EM FUNÇÕES DIFERENTES 
# 1 -  ***VOCÊ CRIAR SEUS PRÓPRIOS MÓDULOS***
# 2 - ***OU USAR STATISTICS *****
import statistics as st

notas_alunos = []
usuario = []
senha = []

def insert():
    for n in range (3):
        print('-------- Nota dos Alunos --------')
        notas = float(input("Insira as notas: "))
        notas_alunos.append(notas)

def n_moda():
    moda = st.mode(notas_alunos)
    print(f'''Moda dos alunos {moda:.0f}''')

def n_media():
    media = st.mean(notas_alunos)
    print(f'''Nota média dos alunos {media:.2f}''')

def desv():
    desvio = st.stdev(notas_alunos)
    print(f'''Desvio padrão de Nota dos alunos {desvio:.2f}''')


def sistema():
    print("---Sistema de Notas---")
    acesso = input("Já possui acesso sim ou nao ? ")
    if acesso == "nao":
        print("Novo Acesso")
        novo_usuario = input("Crie seu login")
        usuario.append(novo_usuario)
        nova_senha = input("Crie sua senha")
        senha.append(nova_senha)
        print("Seja bem vindo ao sistema de Notas")

    elif acesso == 'sim':
            print('Faça login aqui')
    else :
        print("Algo deu errado")

    for n in range (2):
        user = input("Insira seu usuario: ")
        password = input("Insira sua senha: ")
        if user == usuario and password == senha :
            print("---Seja bem vindo---")

            
        elif user != usuario or password != senha :
            print("Usuario ou senha incorretos tente novamente")
            
        else :
            print("acesso Bloqueado")
