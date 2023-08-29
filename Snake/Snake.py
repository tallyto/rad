class Snake:
    def __init__(self):
        self.positions = [(100, 50), (90, 50), (80, 50)]
        self.direction = "Right"

    def move(self):
        head_x, head_y = self.positions[0]
        if self.direction == "Right":
            new_head = (head_x + 10, head_y)
        elif self.direction == "Left":
            new_head = (head_x - 10, head_y)
        elif self.direction == "Up":
            new_head = (head_x, head_y - 10)
        elif self.direction == "Down":
            new_head = (head_x, head_y + 10)

        self.positions = [new_head] + self.positions[:-1]
