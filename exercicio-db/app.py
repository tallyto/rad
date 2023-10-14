import tkinter as tk
import mysql.connector


db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="1234567890",
    database="rad"
)

cursor = db.cursor()

cursor.execute("use rad;")

def criaTabela(cursor):
    try:
        createTable = '''
        CREATE TABLE IF NOT EXISTS aluno (
            id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(50),
            av1 DECIMAL(5, 2),
            av2 DECIMAL(5, 2),
            av3 DECIMAL(5, 2),
            criadoPor VARCHAR(50),
            modificadoPor VARCHAR(50),
            dataCriacao TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            dataAtualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        );
        '''
        cursor.execute(createTable)
        print("Tabela criada com sucesso.")
    except Exception as e:
        print("Erro ao criar a tabela:", e)


# Função para adicionar um aluno
def adicionar_aluno():
    nome = entry_nome.get()
    av1 = entry_av1.get()
    av2 = entry_av2.get()
    av3 = entry_av3.get()
    criado_por = entry_criado_por.get()
    cursor.execute("INSERT INTO aluno (nome, av1, av2, av3, criadoPor) VALUES (%s, %s, %s, %s, %s)", (nome, av1, av2, av3, criado_por))
    db.commit()
    listar_alunos()

# Função para listar os alunos
def listar_alunos():
    cursor.execute("SELECT * FROM aluno")
    alunos = cursor.fetchall()
    resultado_text.delete(1.0, tk.END)  # Limpa o texto anterior

    for aluno in alunos:
        resultado_text.insert(tk.END, f"ID: {aluno[0]}\n")
        resultado_text.insert(tk.END, f"Nome: {aluno[1]}\n")
        resultado_text.insert(tk.END, f"AV1: {aluno[2]}\n")
        resultado_text.insert(tk.END, f"AV2: {aluno[3]}\n")
        resultado_text.insert(tk.END, f"AV3: {aluno[4]}\n")
        resultado_text.insert(tk.END, f"Criado por: {aluno[5]}\n")
        resultado_text.insert(tk.END, "\n")


# Configuração da janela principal
root = tk.Tk()
root.title("Cadastro de Alunos")

# Criação da tabela (se não existir)
criaTabela(cursor)

# Labels e campos de entrada
label_nome = tk.Label(root, text="Nome:")
entry_nome = tk.Entry(root)
label_av1 = tk.Label(root, text="AV1:")
entry_av1 = tk.Entry(root)
label_av2 = tk.Label(root, text="AV2:")
entry_av2 = tk.Entry(root)
label_av3 = tk.Label(root, text="AV3:")
entry_av3 = tk.Entry(root)
label_criado_por = tk.Label(root, text="Criado por:")
entry_criado_por = tk.Entry(root)


# Botão para adicionar aluno
btn_adicionar = tk.Button(root, text="Adicionar Aluno", command=adicionar_aluno)

# Área de exibição dos resultados
resultado_text = tk.Text(root)
resultado_text.config(state=tk.NORMAL)

# Organização dos elementos na janela
label_nome.grid(row=0, column=0)
entry_nome.grid(row=0, column=1)
label_av1.grid(row=1, column=0)
entry_av1.grid(row=1, column=1)
label_av2.grid(row=2, column=0)
entry_av2.grid(row=2, column=1)
label_av3.grid(row=3, column=0)
entry_av3.grid(row=3, column=1)
label_criado_por.grid(row=4, column=0)
entry_criado_por.grid(row=4, column=1)
btn_adicionar.grid(row=5, columnspan=2)
resultado_text.grid(row=6, columnspan=2)

# Listar alunos ao iniciar a aplicação
listar_alunos()

root.mainloop()