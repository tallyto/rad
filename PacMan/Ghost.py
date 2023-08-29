import random


class Ghost:
    def __init__(self, canvas, x, y, labirinto):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.cell_size = 40
        self.ghost = None
        self.labirinto = labirinto  # Adiciona o labirinto como atributo
        self.draw_ghost()

    def draw_ghost(self):
        x0 = self.x * self.cell_size + 2
        y0 = self.y * self.cell_size + 2
        x1 = x0 + self.cell_size - 4
        y1 = y0 + self.cell_size - 4

        self.ghost = self.canvas.create_oval(
            x0, y0, x1, y1,
            fill="red"
        )

    def is_valid_move(self, x, y):
        if x < 0 or y < 0 or x >= len(self.labirinto[0]) or y >= len(self.labirinto):
            return False
        return self.labirinto[y][x] == 0

    def random_direction(self):
        directions = ["Up", "Down", "Left", "Right"]
        valid_directions = []

        for direction in directions:
            x_new, y_new = self.x, self.y

            if direction == "Up":
                y_new -= 1
            elif direction == "Down":
                y_new += 1
            elif direction == "Left":
                x_new -= 1
            elif direction == "Right":
                x_new += 1

            if self.is_valid_move(x_new, y_new):
                valid_directions.append(direction)

        if valid_directions:
            return random.choice(valid_directions)
        else:
            return None

    def get_new_position(self, direction):
        x_new, y_new = self.x, self.y

        if direction == "Up":
            y_new -= 1
        elif direction == "Down":
            y_new += 1
        elif direction == "Left":
            x_new -= 1
        elif direction == "Right":
            x_new += 1

        return x_new, y_new

    def move(self):
        direction = self.random_direction()

        if direction:
            self.canvas.delete(self.ghost)
            self.x, self.y = self.get_new_position(direction)
            self.draw_ghost()
