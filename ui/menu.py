import pygame
from settings import WHITE

def main_menu(screen):
    font = pygame.font.Font(None, 36)
    running = True
    while running:
        screen.fill(WHITE)
        text = font.render("Bienvenido a Monopoly, precione enter para iniciar", True, (0, 0, 0))
        screen.blit(text, (50, 300))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                running = False

        pygame.display.update()