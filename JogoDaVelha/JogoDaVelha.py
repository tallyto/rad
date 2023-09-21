import tkinter as tk
import tkinter.font as font
import tkinter.messagebox as messagebox

class JogoDaVelha:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Jogo da Velha")
        self.root.resizable(False, False)
        self.ultimaJogada = "X"
        self.vencedor = None

        self.tabuleiro = [[" " for _ in range(3)] for _ in range(3)]

        self.mainFrame = tk.Frame(self.root, border=0.25, relief=tk.GROOVE)
        self.mainFrame.grid()
        self.root.geometry("550x550")

        self.botoes = []
        for i in range(3):
            linha = []
            for j in range(3):
                button = tk.Button(self.mainFrame, text=" ", padx=20, pady=20, relief=tk.RAISED, border=1)
                button.grid(row=i, column=j, ipadx=65, ipady=60)
                button["command"] = lambda b=button, row=i, col=j: self.processarBotao(b, row, col)
                linha.append(button)
            self.botoes.append(linha)

    def processarBotao(self, button: tk.Button, row, col):
        fonte = font.Font(family="Arial", size=10)

        if self.tabuleiro[row][col] == " " and not self.vencedor:
            if self.ultimaJogada == "X":
                button.configure(text="O", bg="#0052cc", fg="#FFFFFF")
                self.ultimaJogada = "O"
                self.tabuleiro[row][col] = "O"
            else:
                button.configure(text="X", bg="#222222", fg="#FFFFFF")
                self.ultimaJogada = "X"
                self.tabuleiro[row][col] = "X"

            button.configure(font=fonte)
            self.verificarVencedor()

    def verificarVencedor(self):
        for i in range(3):
            if self.tabuleiro[i][0] == self.tabuleiro[i][1] == self.tabuleiro[i][2] != " ":
                self.vencedor = self.tabuleiro[i][0]

            if self.tabuleiro[0][i] == self.tabuleiro[1][i] == self.tabuleiro[2][i] != " ":
                self.vencedor = self.tabuleiro[0][i]

        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] != " ":
            self.vencedor = self.tabuleiro[0][0]

        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] != " ":
            self.vencedor = self.tabuleiro[0][2]

        if self.vencedor:
            resultado = messagebox.askquestion("Fim de Jogo", f"Jogador {self.vencedor} venceu! Jogar novamente?")
            if resultado == "yes":
                self.novoJogo()
            else:
                self.root.quit()
        elif all(all(cell != " " for cell in row) for row in self.tabuleiro):
            resultado = messagebox.askquestion("Fim de Jogo", "O jogo empatou! Jogar novamente?")
            if resultado == "yes":
                self.novoJogo()
            else:
                self.root.quit()

    def bloquearBotoes(self):
        for linha in self.botoes:
            for button in linha:
                button.configure(state="disabled")

    def mostrarBotaoJogarNovamente(self):
        botao_novo_jogo = tk.Button(self.mainFrame, text="Jogar Novamente", command=self.novoJogo)
        botao_novo_jogo.grid(row=3, column=0, columnspan=3, padx=20, pady=10)

    def novoJogo(self):
        self.tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
        self.ultimaJogada = "X"
        self.vencedor = None
        for linha in self.botoes:
            for button in linha:
                button.configure(text=" ", state="active")

    def iniciar(self):
        self.root.mainloop()

if __name__ == "__main__":
    jogo = JogoDaVelha()
    jogo.iniciar()
