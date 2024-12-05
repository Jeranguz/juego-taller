import pygame

from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from ui.menu import main_menu
from game_logic.board import Board
from game_logic.player import Player

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame .display.set_caption("Monopoly")
clock = pygame.time.Clock()

def main():
    main_menu(screen)

    board = Board()
    player1 = Player("Jugador 1", (255, 0, 0), board)
    player2 = Player("Jugador 2", (0, 0, 255), board)

    running = True
    while running:
        screen.fill((0, 0, 0))
        board.draw(screen)
        player1.draw(screen)
        player2.draw(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player1.move(1)
                elif event.key == pygame.K_d:
                    player1.move(-1)

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()