import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK
from constants import PROPERTIES


class Board:
    def __init__(self):
        self.tiles = PROPERTIES

    def draw(self, screen):
        board_margin = 50
        tile_width = (SCREEN_WIDTH - 2 * board_margin) / 5
        tile_height = (SCREEN_HEIGHT - 2 * board_margin) / 5

        # Dibujar casillas
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
        """
        Calcula la posición de cada casilla en el tablero según su índice.
        """

        # Las posiciones para cada sección del tablero
        if index == 0:  # Esquina inferior derecha
            x = SCREEN_WIDTH - margin - tile_width
            y = SCREEN_HEIGHT - margin - tile_height
        elif index == 4:  # Esquina inferior izquierda
            x = margin
            y = SCREEN_HEIGHT - margin - tile_height
        elif index == 8:  # Esquina superior izquierda
            x = margin
            y = margin
        elif index == 12:  # Esquina superior derecha
            x = SCREEN_WIDTH - margin - tile_width
            y = margin

        # Parte inferior (entre las esquinas inferior derecha e izquierda)
        elif 1 <= index < 4:
            x = SCREEN_WIDTH - margin - tile_width - index * tile_width
            y = SCREEN_HEIGHT - margin - tile_height

        # # Parte izquierda (entre las esquinas inferior izquierda y superior izquierda)
        elif 5 <= index < 8:
            x = margin
            y = SCREEN_HEIGHT - margin - tile_height - (index - 4) * tile_height

        # # Parte superior (entre las esquinas superior izquierda y superior derecha)
        elif 9 <= index < 12:
            x = margin + (index - 8) * tile_width
            y = margin

        # # Parte derecha (entre las esquinas superior derecha e inferior derecha)
        elif 13 <= index < 16:
            x = SCREEN_WIDTH - margin - tile_width
            y = margin + (index - 12) * tile_height

        else:
            x, y, tile_width, tile_height = 0, 0, 0, 0  # En caso de error

        return x, y, tile_width, tile_height
