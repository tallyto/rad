import mysql.connector
from datetime import datetime

cnx = mysql.connector.connect(user="root", password="1234567890", host="127.0.0.1", database="rad")
cursor = cnx.cursor()

# Adicione o comando USE para selecionar o banco de dados
cursor.execute("USE rad;")

def criaTabela():
    try:
        createTable = 'CREATE TABLE IF NOT EXISTS carro (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(50), data_fabricacao timestamp);'
        cursor.execute(createTable)
        cnx.commit()
        print("Tabela criada com sucesso.")
    except Exception as e:
        print("Erro ao criar a tabela:", e)
        cnx.rollback()

def insereCarro(nomeCarro):
    try:
        sql = f"insert into carro (nome, data_fabricacao) values ('{nomeCarro}','{datetime.now().date()}')"
        cursor.execute(sql)
        cnx.commit()
        print("Carro inserido com sucesso!")
    except Exception as e:
        print("Erro ao inserir carro:", e)
        cnx.rollback()

def mostraCarros():
    sql = "select * from carro"
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data)

criaTabela()

insereCarro("Ranger")
insereCarro("Fusca")

mostraCarros()

# Feche a conexão com o banco de dados
cursor.close()
cnx.close()
