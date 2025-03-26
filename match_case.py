# 2: Verificando se um número é positivo, negativo ou zero

num = float(input("Num: "))
match num:
 case 0 :
    print ("Zero")
 case x if x > 0:
    print ("Positivo")
 case _:
    print ("Negativo")

# 3: Verificando se uma string é vazia ou não

verificando = float(input("verificando: "))
match verificando:
 case "" :
    print ("vazio")
 case _:
    print ("Possui texto")

# 4: Verificando se um número é maior, menor ou igual a 10

m_10 = float(input("Num: "))
match m_10:
 case 10 :
    print ("Igual a dez")
 case x if x > 10:
    print ("Maior que dez")
 case _:
    print ("Menor que dez")

# 5: Classificando uma idade em faixas etárias - criança, jovem, adulto, idoso

idade = int(input("Idade: "))
match idade:
 case  13 :
    print ("Criança")
 case x if x <= 10:
    print ("Criança")
 case x if x <= 18:
    print ("adolescente")
 case _:
    print ("Adulto")
