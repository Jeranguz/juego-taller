import pygame

class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.position = 0

    def move(self, steps):
        cells_per_side = 4  
        total_cells = cells_per_side * 4

        for _ in range(steps):
            
            if 0 <= self.position < cells_per_side:
                self.position += 1
            
            elif cells_per_side <= self.position < cells_per_side * 2:
                self.position += cells_per_side
            
            elif cells_per_side * 2 <= self.position < cells_per_side * 3:
                self.position -= 1
            
            elif cells_per_side * 3 <= self.position < total_cells:
                self.position -= cells_per_side

            
            self.position %= total_cells




    def draw(self, screen):
        x = (self.position % 5) * 100 + 120
        y = (self.position // 5) * 100 + 100
        pygame.draw.circle(screen, self.color, (x, y), 10)