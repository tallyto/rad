import tkinter as tk
from tkinter import messagebox
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
            matricula VARCHAR(10) PRIMARY KEY,
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
    matricula = entry_matricula.get()
    nome = entry_nome.get()
    av1 = entry_av1.get()
    av2 = entry_av2.get()
    av3 = entry_av3.get()
    criado_por = entry_criado_por.get()
    cursor.execute("INSERT INTO aluno (matricula, nome, av1, av2, av3, criadoPor) VALUES (%s, %s, %s, %s, %s, %s)", (matricula, nome, av1, av2, av3, criado_por))
    db.commit()
    listar_alunos()

# Função para listar os alunos
def listar_alunos():
    cursor.execute("SELECT * FROM aluno")
    alunos = cursor.fetchall()
    resultado_text.delete(1.0, tk.END)  # Limpa o texto anterior

    for aluno in alunos:
        media = (aluno[2] + aluno[3] + aluno[4]) / 3
        resultado_text.insert(tk.END, f"Matrícula: {aluno[0]}\n")
        resultado_text.insert(tk.END, f"Nome: {aluno[1]}\n")
        resultado_text.insert(tk.END, f"AV1: {aluno[2]}\n")
        resultado_text.insert(tk.END, f"AV2: {aluno[3]}\n")
        resultado_text.insert(tk.END, f"AV3: {aluno[4]}\n")
        resultado_text.insert(tk.END, f"Média: {media:.2f}\n")
        resultado_text.insert(tk.END, f"Criado por: {aluno[5]}\n")
        resultado_text.insert(tk.END, "\n")

        # Adicione botões "Editar" e "Remover" para cada aluno
        btn_editar = tk.Button(root, text="Editar", command=lambda matricula=aluno[0]: editar_aluno(matricula))
        btn_remover = tk.Button(root, text="Remover", command=lambda matricula=aluno[0]: remover_aluno(matricula))
        resultado_text.window_create(tk.END, window=btn_editar)
        resultado_text.window_create(tk.END, window=btn_remover)
        resultado_text.insert(tk.END, "\n")

# Função para remover um aluno
def remover_aluno(matricula):
    # Confirmação de remoção
    if messagebox.askyesno("Confirmação", "Tem certeza de que deseja remover este aluno?"):
        cursor.execute("DELETE FROM aluno WHERE matricula = %s", (matricula,))
        db.commit()
        listar_alunos()

# Função para editar um aluno
def editar_aluno(matricula):
    # Função para salvar as alterações no aluno
    def salvar_alteracoes():
        novo_nome = entry_novo_nome.get()
        nova_av1 = entry_nova_av1.get()
        nova_av2 = entry_nova_av2.get()
        nova_av3 = entry_nova_av3.get()
        cursor.execute("UPDATE aluno SET nome = %s, av1 = %s, av2 = %s, av3 = %s WHERE matricula = %s", (novo_nome, nova_av1, nova_av2, nova_av3, matricula))
        db.commit()
        listar_alunos()
        popup.destroy()

    # Obtenha a matrícula do aluno selecionado (passado como argumento)
    matricula = matricula

    # Consulte o aluno pela matrícula
    cursor.execute("SELECT * FROM aluno WHERE matricula = %s", (matricula,))
    aluno = cursor.fetchone()

    # Criação da janela popup para edição
    popup = tk.Toplevel()
    popup.title("Editar Aluno")

    # Defina as dimensões e a posição do popup
    popup.geometry("400x250")  # Ajuste o tamanho conforme necessário
    popup.transient(root)
    popup.grab_set()

    label_novo_nome = tk.Label(popup, text="Novo Nome:")
    entry_novo_nome = tk.Entry(popup)
    entry_novo_nome.insert(0, aluno[1])  # Preencha com o nome atual
    label_nova_av1 = tk.Label(popup, text="Nova AV1:")
    entry_nova_av1 = tk.Entry(popup)
    entry_nova_av1.insert(0, str(aluno[2]))  # Preencha com a AV1 atual
    label_nova_av2 = tk.Label(popup, text="Nova AV2:")
    entry_nova_av2 = tk.Entry(popup)
    entry_nova_av2.insert(0, str(aluno[3]))  # Preencha com a AV2 atual
    label_nova_av3 = tk.Label(popup, text="Nova AV3:")
    entry_nova_av3 = tk.Entry(popup)
    entry_nova_av3.insert(0, str(aluno[4]))  # Preencha com a AV3 atual
    btn_salvar = tk.Button(popup, text="Salvar Alterações", command=salvar_alteracoes)

    label_novo_nome.pack()
    entry_novo_nome.pack()
    label_nova_av1.pack()
    entry_nova_av1.pack()
    label_nova_av2.pack()
    entry_nova_av2.pack()
    label_nova_av3.pack()
    entry_nova_av3.pack()
    btn_salvar.pack()

# Configuração da janela principal
root = tk.Tk()
root.title("Cadastro de Alunos")

# Criação da tabela (se não existir)
criaTabela(cursor)

# Labels e campos de entrada
label_matricula = tk.Label(root, text="Matrícula:")
entry_matricula = tk.Entry(root)
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
label_matricula.grid(row=0, column=0)
entry_matricula.grid(row=0, column=1)
label_nome.grid(row=1, column=0)
entry_nome.grid(row=1, column=1)
label_av1.grid(row=2, column=0)
entry_av1.grid(row=2, column=1)
label_av2.grid(row=3, column=0)
entry_av2.grid(row=3, column=1)
label_av3.grid(row=4, column=0)
entry_av3.grid(row=4, column=1)
label_criado_por.grid(row=5, column=0)
entry_criado_por.grid(row=5, column=1)
btn_adicionar.grid(row=6, columnspan=2)
resultado_text.grid(row=7, columnspan=2)

# Listar alunos ao iniciar a aplicação
listar_alunos()

root.mainloop()
