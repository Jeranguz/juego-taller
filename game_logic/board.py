import pygame
from constants import PROPERTIES
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

from settings import WHITE, BLACK

class Board:
    def __init__(self):
        self.tiles = PROPERTIES

    def draw(self, screen):
        board_margin = 50
        tile_width = (SCREEN_WIDTH - 2 * board_margin) / 5
        tile_height = (SCREEN_HEIGHT - 2 * board_margin) / 5

        #dibujar casillas
        for index, tile in enumerate(self.tiles):
            x, y, width, height = self.get_tile_position(index, board_margin, tile_width, tile_height)

            pygame.draw.rect(screen, WHITE, (x, y, width, height))
            pygame.draw.rect(screen, BLACK, (x, y, width, height), 2)

            font = pygame.font.Font(None, 20)
            name = tile["name"].split()
            for i, line in enumerate(name):
                text = font.render(line, True, BLACK)
                screen.blit(text, (x + 5, y + 5 + i * 15))

    def get_tile_position(self, index, margin, tile_width, tile_height):
        if index < 5:
            x = SCREEN_WIDTH - margin - (index + 1) * tile_width
            y = SCREEN_HEIGHT - margin - tile_height
            return x, y, tile_width, tile_height
        elif index < 9:
            x = margin
            y = SCREEN_HEIGHT - margin - ((index - 4 + 1) * tile_height)
            return x, y, tile_width, tile_height
        elif index < 14:
            x = margin + ((index - 9) * tile_width)
            y = margin
            return x, y, tile_width, tile_height
        elif index < 19:
            x = SCREEN_WIDTH - margin - tile_width
            y = margin + ((index - 14) * tile_height)
            return x, y, tile_width, tile_height
        return 0, 0, 0, 0


