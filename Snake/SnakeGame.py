import tkinter as tk
import random

# Importar a classe Snake do módulo Snake
from Snake import Snake

# Constantes
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
PLAY_AREA_PADDING = 10
PLAY_AREA_LEFT = PLAY_AREA_PADDING
PLAY_AREA_TOP = PLAY_AREA_PADDING
PLAY_AREA_RIGHT = CANVAS_WIDTH - PLAY_AREA_PADDING
PLAY_AREA_BOTTOM = CANVAS_HEIGHT - PLAY_AREA_PADDING
SNAKE_MOVE_INTERVAL = 100  # em milissegundos


class SnakeGame:
    def __init__(self, window: tk.Tk):
        self.window = window
        self.window.title("Snake Game")

        # Configurar o canvas
        self.canvas = tk.Canvas(window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.canvas.pack()

        # Inicializar a cobra, pontuação e status do jogo
        self.snake = Snake()
        self.score = 0
        self.game_over = False

        # Configurar frame para o botão "Play Again"
        self.frame_bottom = tk.Frame(window)
        self.frame_bottom.pack(side="bottom", pady=PLAY_AREA_PADDING)

        # Configurar botão "Play Again" no canto inferior esquerdo
        self.play_again_button = tk.Button(self.frame_bottom, text="Play Again", command=self.restart_game)
        self.play_again_button.pack(side="left")
        self.play_again_button.config(state="disabled")

        # Vincular evento de tecla ao método de pressionar tecla
        self.canvas.bind_all("<Key>", self.on_key_press)

        # Definir limites da área jogável
        self.play_area = (PLAY_AREA_LEFT, PLAY_AREA_TOP, PLAY_AREA_RIGHT, PLAY_AREA_BOTTOM)

        # Posição inicial da maçã
        self.apple = self.generate_new_apple_position()

        # Iniciar o jogo
        self.play()

    def on_key_press(self, e):
        # Atualizar a direção da cobra com base na tecla pressionada
        key = e.keysym
        if key == "Right" and self.snake.direction != "Left":
            self.snake.direction = "Right"
        elif key == "Left" and self.snake.direction != "Right":
            self.snake.direction = "Left"
        elif key == "Up" and self.snake.direction != "Down":
            self.snake.direction = "Up"
        elif key == "Down" and self.snake.direction != "Up":
            self.snake.direction = "Down"
        elif key in ["d", "D"] and self.snake.direction != "Left":
            self.snake.direction = "Right"
        elif key in ["a", "A"] and self.snake.direction != "Right":
            self.snake.direction = "Left"
        elif key in ["w", "W"] and self.snake.direction != "Down":
            self.snake.direction = "Up"
        elif key in ["s", "S"] and self.snake.direction != "Up":
            self.snake.direction = "Down"

    def play(self):
        # Movimentar a cobra
        self.snake.move()

        # Verificar colisão com a parede
        if (self.snake.positions[0][0] < self.play_area[0] or
                self.snake.positions[0][0] >= self.play_area[2] or
                self.snake.positions[0][1] < self.play_area[1] or
                self.snake.positions[0][1] >= self.play_area[3]):
            self.game_over = True

        # Verificar colisão com a maçã e atualizar a pontuação
        if not self.game_over and self.is_collision(self.snake.positions[0], self.apple):
            self.apple = self.generate_new_apple_position()
            self.score += 1

        # Atualizar o canvas
        self.update_canvas()

        # Agendar a próxima iteração do jogo
        if not self.game_over:
            self.window.after(SNAKE_MOVE_INTERVAL, self.play)
        else:
            self.show_game_over_message()

    def show_game_over_message(self):
        # Exibir mensagem de fim de jogo no centro da tela
        self.game_over_label = tk.Label(self.window, text="Game Over", font=("Helvetica", 24), fg="red")
        self.game_over_label.place(relx=0.5, rely=0.5, anchor="center")

        # Habilitar o botão "Play Again"
        self.play_again_button.config(state="normal")

    def restart_game(self):
        # Reiniciar o jogo
        self.snake = Snake()
        self.score = 0
        self.game_over = False
        # Remover a mensagem de Game Over
        self.game_over_label.destroy()
        self.apple = self.generate_new_apple_position()
        self.play_again_button.config(state="disabled")  # Desativar o botão novamente
        self.play()  # Iniciar o jogo novamente

    def is_collision(self, position1, position2):
        # Verificar se duas posições colidem
        return position1 == position2

    def generate_new_apple_position(self):
        # Gere uma nova posição aleatória para a maçã, dentro da área jogável
        new_apple_x = random.randint(self.play_area[0] // 10, self.play_area[2] // 10 - 1) * 10
        new_apple_y = random.randint(self.play_area[1] // 10, self.play_area[3] // 10 - 1) * 10
        return new_apple_x, new_apple_y

    def update_canvas(self):
        # Limpar o canvas
        self.canvas.delete("all")

        # Desenhar paredes internas
        self.canvas.create_rectangle(self.play_area, outline="gray")

        # Desenhar a cobra
        for segment in self.snake.positions:
            x, y = segment
            # Certifique-se de que a cobra permaneça dentro da área jogável
            x = max(self.play_area[0], min(x, self.play_area[2] - 10))
            y = max(self.play_area[1], min(y, self.play_area[3] - 10))
            self.canvas.create_rectangle(x, y, x + 10, y + 10, fill="green")

        # Desenhar a maçã
        apple_x, apple_y = self.apple
        self.canvas.create_oval(apple_x, apple_y, apple_x + 10, apple_y + 10, fill="red")

        # Desenhar a pontuação
        score_text = f"Score: {self.score}"
        self.canvas.create_text(PLAY_AREA_RIGHT, PLAY_AREA_BOTTOM, text=score_text, anchor="se")


if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(False, False)  # Impede o redimensionamento da janela
    game = SnakeGame(root)
    root.mainloop()
