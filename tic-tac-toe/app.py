import tkinter as tk
from tkinter import messagebox

# Função para verificar se há um vencedor
def verificar_vencedor(tabuleiro):
    # Verifica se alguém ganhou na horizontal, vertical ou diagonal
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != "":
            return tabuleiro[i][0]
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != "":
            return tabuleiro[0][i]
    
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != "":
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != "":
        return tabuleiro[0][2]
    
    return None

# Função chamada quando um botão do tabuleiro é clicado
def ao_clicar(linha, coluna):
    global jogador_atual, tabuleiro, vencedor

    # Verifica se a célula está vazia e não há vencedor
    if tabuleiro[linha][coluna] == "" and vencedor is None:
        tabuleiro[linha][coluna] = jogador_atual
        botoes[linha][coluna].config(text=jogador_atual)
        
        # Verifica se há um vencedor
        vencedor = verificar_vencedor(tabuleiro)
        if vencedor:
            messagebox.showinfo("Jogo da Velha", f"O jogador {vencedor} venceu!")
            root.quit()
        # Verifica empate
        elif all(tabuleiro[i][j] != "" for i in range(3) for j in range(3)):
            messagebox.showinfo("Jogo da Velha", "Empate!")
            root.quit()
        
        # Alterna o jogador atual
        jogador_atual = "X" if jogador_atual == "O" else "O"

# Cria a janela principal
root = tk.Tk()
root.geometry("550x550")  # Define o tamanho da janela
root.title("Jogo da Velha")

# Cria o quadro principal
quadro_principal = tk.Frame(root, border=3, relief='groove')
quadro_principal.pack(expand=True, fill="both")

# Inicializa a matriz do tabuleiro, o jogador atual e a variável de vencedor
tabuleiro = [["" for _ in range(3)] for _ in range(3)]
jogador_atual = "X"
vencedor = None

# Cria os botões do tabuleiro e associa a função ao_clicar
botoes = []
for i in range(3):
    botoes_linha = []
    for j in range(3):
        botao = tk.Button(quadro_principal, text="", border=1, relief="groove", padx=20, pady=20,
                          width=10, height=3,  # Ajuste o tamanho dos botões aqui
                          command=lambda linha=i, coluna=j: ao_clicar(linha, coluna))
        botao.grid(row=i, column=j)
        botoes_linha.append(botao)
    botoes.append(botoes_linha)

# Inicia o loop principal da interface gráfica
root.mainloop()
