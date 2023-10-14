import mysql.connector

cnx = mysql.connector.connect(user="root", password="1234567890", host="127.0.0.1", database="rad")
cursor = cnx.cursor()

# Adicione o comando USE para selecionar o banco de dados
cursor.execute("USE rad;")

def criaTabela():
    try:
        createTable = 'CREATE TABLE minha_cidade (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, nome_cidade VARCHAR(50), estado VARCHAR(2));'
        cursor.execute(createTable)
        cnx.commit()
        print("Tabela criada com sucesso.")
    except Exception as e:
        print("Erro ao criar a tabela:", e)
        cnx.rollback()

def insereCidade(cidade, estado):
    try:
        sql = f"insert into minha_cidade (nome_cidade, estado) values ('{cidade}','{estado}')"
        cursor.execute(sql)
        cnx.commit()
        print("Cidade inserida com sucesso!")
    except Exception as e:
        print("Erro ao inserir cidade:", e)
        cnx.rollback()

def mostraCidades():
    sql = "select * from minha_cidade"
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data)

# Feche a conexão com o banco de dados

# insereCidade("Boa Vista", "RR")
mostraCidades()
cursor.close()
cnx.close()
