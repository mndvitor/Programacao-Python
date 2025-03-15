dados = {}


usuario_nome  =  input('Digite seu nome:')
usuario_login = input('Digite o login')
usuario_senha = input('Digite sua senha')


dados['nome'] = usuario_nome
dados['login'] = usuario_login
dados['senha'] = usuario_senha


senha_acess = input('Digite a senha')
if dados['senha'] == senha_acess:
    carrinho = []
    meu_total = []
    prod = ['IPHONE','DELL', 'MESA DE PC', 'FONE'] 
    valores = [10.45,20.25,35.00,50.00]
    print('Escolha o produto pelo ID - 0 - 1 - 2 - 3', prod)
    escolha_produto1 = int(input('Escolha:'))
    escolha_produto2 = int(input('Escolha:'))
    carrinho.append(prod[escolha_produto1])
    carrinho.append(prod[escolha_produto2])
    meu_total.append(valores[escolha_produto1])
    meu_total.append(valores[escolha_produto2])
    print('Seus produtos', carrinho)
    
    print('>>>>'*10)
    soma  =sum(meu_total)
    print('Total do pedido R$', soma)
else:
    print('Acesso negado, senha incorreta')