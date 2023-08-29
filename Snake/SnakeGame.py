import tkinter as tk
import random
import time
from Snake import Snake

class SnakeGame:
    def __init__(self, window):
        self.window = window
        self.window.title("Snake Game")

        self.canvas = tk.Canvas(window, width=400, height=400)
        self.canvas.pack()

        self.snake = Snake()

        self.canvas.bind_all("<Key>", self.on_key_press)
        self.apple = (200, 100)  # Posição inicial da maçã
        self.play()

    def on_key_press(self, e):
        key = e.keysym
        if key == "Right" and self.snake.direction != "Left":
            self.snake.direction = "Right"
        elif key == "Left" and self.snake.direction != "Right":
            self.snake.direction = "Left"
        elif key == "Up" and self.snake.direction != "Down":
            self.snake.direction = "Up"
        elif key == "Down" and self.snake.direction != "Up":
            self.snake.direction = "Down"
        # Adicione outras condições de teclas aqui

    def play(self):
        self.snake.move()
         # Verifique colisões
        if self.is_collision(self.snake.positions[0], self.apple):
            # A cobra comeu a maçã, então você precisa atualizar a posição da maçã
            self.apple = self.generate_new_apple_position()

        # Atualize a tela
        self.update_canvas()

        self.window.after(100, self.play)

    def is_collision(self, position1, position2):
        # Verifique se duas posições colidem (por exemplo, cobra e maçã)
        return position1 == position2
    
    def generate_new_apple_position(self):
        # Gere uma nova posição aleatória para a maçã
        new_apple_x = random.randint(0, 39) * 10
        new_apple_y = random.randint(0, 39) * 10
        return new_apple_x, new_apple_y
    
    def update_canvas(self):
        self.canvas.delete("all")  # Limpe a tela

        # Desenhe a cobra
        for segment in self.snake.positions:
            x, y = segment
            self.canvas.create_rectangle(x, y, x + 10, y + 10, fill="green")

        # Desenhe a maçã
        apple_x, apple_y = self.apple
        self.canvas.create_oval(apple_x, apple_y, apple_x + 10, apple_y + 10, fill="red")


if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
