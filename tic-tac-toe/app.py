import tkinter as tk
from tkinter import messagebox

# Função para verificar se há um vencedor
def check_winner(board):
    # Verifica se alguém ganhou na horizontal, vertical ou diagonal
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]
    
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    
    return None

# Função chamada quando um botão do tabuleiro é clicado
def on_click(row, col):
    global current_player, board, winner

    # Verifica se a célula está vazia e não há vencedor
    if board[row][col] == "" and winner is None:
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)
        
        # Verifica se há um vencedor
        winner = check_winner(board)
        if winner:
            messagebox.showinfo("Tic-Tac-Toe", f"Jogador {winner} venceu!")
            root.quit()
        # Verifica empate
        elif all(board[i][j] != "" for i in range(3) for j in range(3)):
            messagebox.showinfo("Tic-Tac-Toe", "Empate!")
            root.quit()
        
        # Alterna o jogador atual
        current_player = "X" if current_player == "O" else "O"

# Cria a janela principal
root = tk.Tk()
root.geometry("550x550")  # Define o tamanho da janela
root.title("Tic-Tac-Toe")

# Cria o quadro principal
main_frame = tk.Frame(root, border=3, relief='groove')
main_frame.pack(expand=True, fill="both")

# Inicializa a matriz do tabuleiro, o jogador atual e a variável de vencedor
board = [["" for _ in range(3)] for _ in range(3)]
current_player = "X"
winner = None

# Cria os botões do tabuleiro e associa a função on_click
buttons = []
for i in range(3):
    row_buttons = []
    for j in range(3):
        button = tk.Button(main_frame, text="", border=1, relief="groove", padx=20, pady=20,
                           width=10, height=3,  # Ajuste o tamanho dos botões aqui
                           command=lambda row=i, col=j: on_click(row, col))
        button.grid(row=i, column=j)
        row_buttons.append(button)
    buttons.append(row_buttons)

# Inicia o loop principal da interface gráfica
root.mainloop()
