# Definição das direções como constantes
RIGHT = "Right"
LEFT = "Left"
DOWN = "Down"
UP = "Up"


class Snake:
    def __init__(self):
        # Inicialização das posições da cobra e direção
        self.positions = [(100, 50), (90, 50), (80, 50)]  # Posições iniciais dos segmentos da cobra
        self.direction = "Right"  # Direção inicial da cobra

    def move(self):
        # Obter a posição da cabeça da cobra
        head_x, head_y = self.positions[0]

        # Calcular a nova posição da cabeça baseada na direção
        if self.direction == RIGHT:
            new_head = (head_x + 10, head_y)
        elif self.direction == LEFT:
            new_head = (head_x - 10, head_y)
        elif self.direction == UP:
            new_head = (head_x, head_y - 10)
        elif self.direction == DOWN:
            new_head = (head_x, head_y + 10)

        # Atualizar as posições da cobra com a nova posição da cabeça
        self.positions = [new_head] + self.positions[:-1]
