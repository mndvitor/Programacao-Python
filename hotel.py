nomes = []
idades = []

for n in range (2):

    nome = input('Nome: ')
    idade = int(input('Idade:')) 

    nomes.append(nome)
    idades.append(idade)

    lista_quartos =  ['SIMPLES', 'DUPLO', 'LUXO']
    lista_valores_quartos = [100.0,150.0,250.0]

    print('escolha a partir do código do quarto 0 - 1 - 2  ', lista_quartos)

    escolha_quarto = int(input(f'Escolha o quarto{nome}'))
    dias_quarto = int(input(f'Digite os dias {nome}'))
    calc = lista_valores_quartos[escolha_quarto] * dias_quarto
    print('O Usuário ', nome, 'escolheu o quarto',lista_quartos[escolha_quarto])
    print('Total cliente',nome, 'R$', calc)
