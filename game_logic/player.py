import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT


class Player:
    def __init__(self, name, color, board):
        self.name = name
        self.color = color
        self.position = 0  # Posición inicial del jugador
        self.board = board

    def move(self, steps):
        # Total de casillas en el tablero
        total_tiles = len(self.board.tiles)  # Ahora es dinámico según el tablero
        self.position = (self.position + steps) % total_tiles

    def draw(self, screen):
        # Obtener la posición actual en el tablero
        board_margin = 50
        tile_width = (SCREEN_WIDTH - 2 * board_margin) / 5
        tile_height = (SCREEN_HEIGHT - 2 * board_margin) / 5

        x, y, width, height = self.board.get_tile_position(self.position, board_margin, tile_width, tile_height)

        # Dibujar al jugador como un círculo
        center_x = x + width // 2
        center_y = y + height // 2
        pygame.draw.circle(screen, self.color, (center_x, center_y), 15)
