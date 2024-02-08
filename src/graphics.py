import pygame

class IntroScreen:
    def __init__(self, screen):
        # charger et importer l'arrière plan
        self.background = pygame.image.load('graphics/title_bg.png')
        self.background = pygame.transform.scale(self.background, (800, 800))
        # charger le style et la taille du text du Titre
        self.font_title = pygame.font.Font('dialogs/cityburn.ttf', 50)
        self.text_title = self.font_title.render('NINJA PYTHON', True, (0, 0, 0))
        self.title_rect = self.text_title.get_rect()
        self.title_rect.center = (screen.get_width() // 2, screen.get_height() // 3)
        # charger le style et la taille du text de bienvenu
        self.font_text = pygame.font.Font('dialogs/cityburn.ttf', 20)
        self.text_text = self.font_text.render('click sur la fenêtre pour commencer', True, (0, 0, 0))
        self.text_rect = self.text_text.get_rect()
        self.text_rect.center = (screen.get_width() // 2, screen.get_height() - screen.get_height() // 3)

class MainMenu:
    def __init__(self, screen):
        # charger et importer l'arrière plan
        self.background = pygame.image.load('graphics/title_bg.png')
        self.background = pygame.transform.scale(self.background, (800, 800))
        # charger le style et la taille du text de bienvenu
        self.font_text = pygame.font.Font('dialogs/cityburn.ttf', 20)
        self.text_game_beginner = self.font_text.render('mode beginner', True, (0, 0, 0), (255, 0, 255))
        self.game_beginner_rect = self.text_game_beginner.get_rect()
        self.game_beginner_rect.topleft = (screen.get_width() // 10, screen.get_height() // 10)
        self.text_game_classique = self.font_text.render('mode classique', True, (0, 0, 0), (255,0,255))
        self.game_classique_rect = self.text_game_classique.get_rect()
        self.game_classique_rect.topleft = (screen.get_width() // 10, screen.get_height() // 6)
        self.text_game_blitz = self.font_text.render('mode blits', True, (0, 0, 0), (255, 0, 255))
        self.game_blitz_rect = self.text_game_blitz.get_rect()
        self.game_blitz_rect.topleft = (screen.get_width() // 10, screen.get_height() // 6 - (screen.get_height() // 10 - screen.get_height() // 6))
        self.text_game_speedup = self.font_text.render('mode Speed UP', True, (0, 0, 0), (255, 0, 255))
        self.game_speedup_rect = self.text_game_speedup.get_rect()
        self.game_speedup_rect.topleft = (screen.get_width() // 10, screen.get_height() // 6-2 * (screen.get_height() // 10 - screen.get_height() // 6))


class InGame:
    def __init__(self, screen):
        # charger et importer l'arrière plan
        self.background = pygame.image.load('graphics/title_bg.png')
        self.background = pygame.transform.scale(self.background, (800, 800))


class HealthSprite(pygame.sprite.Sprite):
    def __init__(self, name, x, y):
        super().__init__()
        self.image = pygame.image.load(f'graphics/{name}.png')
        self.image = pygame.transform.scale(self.image , (20, 20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
