# import random

# chances = 3 
# while chances > 0 :
#     aleatorio = random.randint(1,10)
#     escolha = int(input("Digite um numero: "))
#     if escolha == aleatorio:
#         print("Acertou em cheio")
#         print("O numero da sorte é", aleatorio)
#         break

#     else :
#         chances = chances - 1 
#         print('Você tem ', chances, 'chances')
#         print('o número sorteado foi ', aleatorio)

# else :
#     print('Chances esgotadas', chances)
#     print('você perdeu o jogo!!!! ;(')

dicionario = {
    'nome': [],
    'email':[],
    'senha':[]
}

numero = int(input('digite a quantidade de cadastros: '))
print('cadastre-se: ')
for n in range(0,numero):
    nome = input('nome: ')
    email = input('E-mail: ')
    senha = input('Senha: ')
    dicionario['nome'].append(nome)
    dicionario['email'].append(email)
    dicionario['senha'].append(senha)
    print(dicionario)


dados_usuario = dicionario


email_usuario = input('digite o email')
senha_usuario = input('digite a senha')
carrinho = []
while email_usuario in dicionario['email'] and senha_usuario in dicionario['senha']:
    escolha = input('Deseja fazer o pedido?')
    while escolha == 's' or escolha =='sim' or escolha =='S' or escolha == 'SIM':
        produtos = ['a','b','c','d']
        print('produtos', produtos)
        meu_prod  = int(input('digite o indice 0 1 2 3 '))
        carrinho.append(produtos[meu_prod])
        print('CARRINHO: ', carrinho)
        escolha = input('Deseja continuar? s/n')
    else:
        print('Obrigada volte sempre!!')   
        break 
else:
    print('Acesso negado dados incorretos! ')        
