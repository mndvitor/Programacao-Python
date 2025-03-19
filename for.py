# ***ATIVIDADE 1***
# 1 - Faça um programa, utilizando while, 
#     que mostre na tela os números de 0 a 1000.
# num = 0 
# while num <= 1000:
#     print(num)
#     num += 1

# # 2 - Faça um sistema, utilizando while e listas,
# #     que permita o usuário escrever o nome de 10 pessoas e os mostre na tela.
# nomes = []

# for n in range (10):
#     add_nome = input("Digite o nome: ")
#     nomes.append(add_nome)
# print(nomes)

# # ***ATIVIDADE 2***
# # Crie um sistema de notas, com as seguintes operações:
# # Utilize While ou for
# # Sistema de notas de alunos

usuario = ["aaa"]
senha = [123]

notas_alunos = {'aluno':[],
                'nota': []
                }

# - Acesso a conta com condicionais
# - 3 chances de acessar o sistema
# - Após errar 3 x mensagem que diga que a conta bloqueada 
# - Inserir notas 
# - Fazer a média

for n in range (3):
    login_usuario = input('Digite seu usuario')
    login_senha = int(input('Digite sua senha'))
    if login_usuario == usuario[0] and login_senha == senha[0] :
        print("Seja bem vindo ao sistema de notas")
    else :
        print("Usuario ou senha incorretos")
    for n in range(4):
        aluno = input("Digite o nome do aluno:")
        nota = float(input("Digite a nota"))
        notas_alunos = ['aluno'].append(aluno)
        notas_alunos = ['nota'].append(nota)
        media = sum(aluno['nota'] for aluno in notas_alunos) / len(notas_alunos)
        print(media)

else :
    print("Sua conta foi bloqueada")
