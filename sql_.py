import sqlite3

conexao = sqlite3.connect('meu_banco.bd')

cursor = conexao.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS pessoas(
        id INTEGER PRIMARY KEY NOT NULL,
        nome TEXT NOT NULL, 
        idade INTEGER NOT NULL,
        cidade TEXT NOT NULL)''')

nome = input('Digite o nome')
idade = int(input('Digite a idade'))
cidade = input('Digite a cidade')
cursor.execute(''''
    INSERT INTO pessoas (nome, idade, cidade)
    VALUES(?, ?, ?)
''', (nome, idade, cidade))

conexao.commit()

cursor.execute('SELECT * FROM pessoas')
pessoas = cursor.fetchall()

for pessoa in pessoas :
    print(f''' ID: {pessoa [0]}, Nome: {pessoa [1]}, 
            Idade: {pessoa [2]}, cidade: {pessoa [3]}
''')
    
conexao.close()