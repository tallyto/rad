import tkinter as tk


class PacmanGame:
    def __init__(self, root):
        self.pacman = None
        self.direcao = None
        self.root = root
        self.canvas = tk.Canvas(root)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Matriz do labirinto
        self.labirinto = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
            [1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
            [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
            [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
            [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1],
            [1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
            [1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1],
            [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1],
            [1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

        self.num_linhas = len(self.labirinto)
        self.num_colunas = len(self.labirinto[0])

        self.cell_size = 40  # Tamanho de cada célula

        self.moving_key = False  # Variável para controlar a movimentação por teclado
        self.canvas.bind("<KeyPress>", self.on_key_press)
        self.canvas.focus_set()

        self.desenhar_labirinto()

        # Posição inicial do Pac-Man
        self.pacman_pos = (1, 1)

        # Inicia o movimento automático
        self.direcao_auto = "Right"
        self.root.after(200, self.game_loop)

    def desenhar_labirinto(self):
        canvas_width = self.num_colunas * self.cell_size
        canvas_height = self.num_linhas * self.cell_size
        self.canvas.config(width=canvas_width, height=canvas_height)

        for row in range(self.num_linhas):
            for col in range(self.num_colunas):
                x0 = col * self.cell_size
                y0 = row * self.cell_size
                x1 = x0 + self.cell_size
                y1 = y0 + self.cell_size

                if self.labirinto[row][col] == 1:
                    self.canvas.create_rectangle(
                        x0, y0, x1, y1,
                        fill="blue", outline="blue"
                    )
                else:
                    self.canvas.create_oval(
                        x0 + 15, y0 + 15, x1 - 15, y1 - 15,
                        fill="white"
                    )

    def desenhar_pacman(self):
        x, y = self.pacman_pos
        x0 = x * self.cell_size + 2
        y0 = y * self.cell_size + 2
        x1 = x0 + self.cell_size - 4
        y1 = y0 + self.cell_size - 4

        self.pacman = self.canvas.create_oval(
            x0, y0, x1, y1,
            fill="yellow"
        )

    def game_loop(self):
        # Atualiza a lógica do jogo aqui
        self.mover_pacman_auto()

        # Redesenha o Pac-Man e outras atualizações visuais
        self.canvas.delete(self.pacman)
        self.desenhar_pacman()

        # Chama o loop principal novamente após um intervalo
        self.root.after(200, self.game_loop)

    def on_key_press(self, event):
        if self.moving_key:
            return

        self.moving_key = True

        key = event.keysym
        x, y = self.pacman_pos

        if key == "Up":
            self.direcao_auto = "Up"
        elif key == "Down":
            self.direcao_auto = "Down"
        elif key == "Left":
            self.direcao_auto = "Left"
        elif key == "Right":
            self.direcao_auto = "Right"

        self.moving_key = False

    def on_key_release(self, event):
        self.direcao_auto = None

    def mover_pacman_auto(self):
        x, y = self.pacman_pos

        if self.direcao_auto == "Right" and x < self.num_colunas - 1 and self.labirinto[y][x + 1] == 0:
            x += 1
        elif self.direcao_auto == "Left" and x > 0 and self.labirinto[y][x - 1] == 0:
            x -= 1
        elif self.direcao_auto == "Up" and y > 0 and self.labirinto[y - 1][x] == 0:
            y -= 1
        elif self.direcao_auto == "Down" and y < self.num_linhas - 1 and self.labirinto[y + 1][x] == 0:
            y += 1

        # Atualiza a posição do Pac-Man
        self.pacman_pos = (x, y)

    def alterar_direcao(self):
        if self.direcao == "Right":
            self.direcao = "Down"
        elif self.direcao == "Down":
            self.direcao = "Left"
        elif self.direcao == "Left":
            self.direcao = "Up"
        elif self.direcao == "Up":
            self.direcao = "Right"


def main():
    root = tk.Tk()
    game = PacmanGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
