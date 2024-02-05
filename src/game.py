import pygame

class Game:

    def __init__(self):

        # création de fenêtre pour le jeu
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("python ninja")

    def run(self):
        clock = pygame.time.Clock()
        # boucle du jeu
        running = True
        while running:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            clock.tick(60)

        pygame.quit()