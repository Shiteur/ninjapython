import pygame


class IntroScreen:
    def __init__(self, screen):
        # charger et importer l'arrière plan
        self.background = pygame.image.load('graphics/Background/Background_intro.png')
        self.background = pygame.transform.scale(self.background, (800, 800))
        # charger le style et la taille du text du Titre
        self.font_title = pygame.font.Font('dialogs/cityburn.ttf', 50)
        self.text_title = self.font_title.render('NINJA PYTHON', True, (0, 0, 0))
        self.title_rect = self.text_title.get_rect()
        self.title_rect.center = (screen.get_width() // 2, screen.get_height() // 3)
        # charger le style et la taille du text de bienvenu
        self.font_text = pygame.font.Font('dialogs/cityburn.ttf', 20)
        self.text_text = self.font_text.render('click sur la fenêtre pour commencer', True, (255, 255, 255))
        self.text_rect = self.text_text.get_rect()
        self.text_rect.center = (screen.get_width() // 2, screen.get_height() - screen.get_height() // 3)

class MainMenu:
    def __init__(self, screen):
        # charger et importer l'arrière plan
        self.background = pygame.image.load('graphics/Background/Background_main_menu.jpg')
        self.background = pygame.transform.scale(self.background, (800, 800))
        #importer l'arrière plan des text
        self.background_text = pygame.image.load('graphics/Background/Background_text.png')
        self.background_text = pygame.transform.scale(self.background_text, (140, 30))
        # charger le style et la taille du text de bienvenu
        self.font_text = pygame.font.Font('dialogs/cityburn.ttf', 20)
        #charger le text pour le mode débutant
        self.text_game_beginner = self.font_text.render('mode beginner', True, (0, 0, 0))
        self.game_beginner_rect = self.text_game_beginner.get_rect()
        self.game_beginner_rect.topleft = (screen.get_width() // 2.5+7, screen.get_height() // 10)
        #charger le text pour le mode normal
        self.text_game_classique = self.font_text.render('mode classique', True, (0, 0, 0))
        self.game_classique_rect = self.text_game_classique.get_rect()
        self.game_classique_rect.topleft = (screen.get_width() // 2.5+2, screen.get_height() // 6)
        #charger le text pour le mode rapide
        self.text_game_blitz = self.font_text.render('mode blits', True, (0, 0, 0))
        self.game_blitz_rect = self.text_game_blitz.get_rect()
        self.game_blitz_rect.topleft = (screen.get_width() // 2.5+20, screen.get_height() // 6 - (screen.get_height() // 10 - screen.get_height() // 6-1))
        #charger le text pour le mode vitesse augmenté
        self.text_game_speedup = self.font_text.render('mode Speed UP', True, (0, 0, 0))
        self.game_speedup_rect = self.text_game_speedup.get_rect()
        self.game_speedup_rect.topleft = (screen.get_width() // 2.5, screen.get_height() // 6-2 * (screen.get_height() // 10 - screen.get_height() // 6+1))
        #charger le text pour les paramètres
        self.text_game_setting = self.font_text.render('setting', True, (0, 0, 0))
        self.game_setting_rect = self.text_game_setting.get_rect()
        self.game_setting_rect.topleft = (screen.get_width() // 2.5+40, screen.get_height() // 6-3 * (screen.get_height() // 10 - screen.get_height() // 6))
        #charger le text pour les crédits
        self.text_game_credit = self.font_text.render('credits', True, (0, 0, 0))
        self.game_credit_rect = self.text_game_credit.get_rect()
        self.game_credit_rect.topleft = (screen.get_width() // 2.5+40, screen.get_height() // 6-4 * (screen.get_height() // 10 - screen.get_height() // 6))
        # charger le text pour les règles
        self.text_game_rule = self.font_text.render('rule', True, (0, 0, 0))
        self.game_rule_rect = self.text_game_rule.get_rect()
        self.game_rule_rect.topleft = (screen.get_width() // 2.5 + 50, screen.get_height() // 6 - 5 * (screen.get_height() // 10 - screen.get_height() // 6))
        # charger le text pour quitter
        self.text_game_leave = self.font_text.render('leave', True, (0, 0, 0))
        self.game_leave_rect = self.text_game_leave.get_rect()
        self.game_leave_rect.topleft = (screen.get_width() // 2.5 + 50, screen.get_height() // 6 - 6 * (screen.get_height() // 10 - screen.get_height() // 6))


class InGame:
    def __init__(self, screen):
        # charger et importer l'arrière plan
        self.background_classique = pygame.image.load('graphics/Background/Background_classique.png')
        self.background_classique = pygame.transform.scale(self.background_classique, (800, 800))
        self.background_hard = pygame.image.load('graphics/Background/Background_SpeedUp.png')
        self.background_hard = pygame.transform.scale(self.background_hard, (800, 800))


class InSetting:
    def __init__(self, screen):
        # charger et importer l'arrière plan
        self.background_setting = pygame.image.load('graphics/Background/Background_setting.png')
        self.background_setting = pygame.transform.scale(self.background_setting, (800, 800))
        # importer l'arrière plan des text
        self.background_text1 = pygame.image.load('graphics/Background/Background_text.png')
        self.background_text1 = pygame.transform.scale(self.background_text1, (140, 30))
        self.background_text2 = pygame.image.load('graphics/Background/Background_text.png')
        self.background_text2 = pygame.transform.scale(self.background_text2, (180, 30))
        #importer les boutton pour la music
        self.UpButton_music = pygame.image.load('graphics/UpButton.png')
        self.UpButton_music = pygame.transform.scale(self.UpButton_music,(30,30))
        self.DownButton_music = pygame.image.load('graphics/DownButton.png')
        self.DownButton_music = pygame.transform.scale(self.DownButton_music, (30, 30))
        # importer les boutton pour les effets sonores
        self.UpButton_sound = pygame.image.load('graphics/UpButton.png')
        self.UpButton_sound = pygame.transform.scale(self.UpButton_sound, (30, 30))
        self.DownButton_sound = pygame.image.load('graphics/DownButton.png')
        self.DownButton_sound = pygame.transform.scale(self.DownButton_sound, (30, 30))
        # charger le style et la taille du text de bienvenu
        self.font_text = pygame.font.Font('dialogs/cityburn.ttf', 20)
        # charger le text pour le niveau de la musique
        self.UpButton_music_text = self.font_text.render('', True, (0, 0, 0))
        self.UpButton_music_rect = self.UpButton_music.get_rect()
        self.UpButton_music_rect.height = 30
        self.UpButton_music_rect.width = 30
        self.UpButton_music_rect.topleft = (screen.get_width() // 2.5 - 60, screen.get_height() // 10)
        self.DownButton_music_text = self.font_text.render('', True, (0, 0, 0))
        self.DownButton_music_rect = self.DownButton_music.get_rect()
        self.DownButton_music_rect.height = 30
        self.DownButton_music_rect.width = 30
        self.DownButton_music_rect.topleft = (screen.get_width() // 2.5 + 180, screen.get_height() // 10)
        # charger le text pour le niveau des effets sonores
        self.UpButton_sound_text = self.font_text.render('', True, (0, 0, 0))
        self.UpButton_sound_rect = self.UpButton_music.get_rect()
        self.UpButton_sound_rect.height = 30
        self.UpButton_sound_rect.width = 30
        self.UpButton_sound_rect.topleft = (screen.get_width() // 2.5 - 60, screen.get_height() // 6)
        self.DownButton_sound_text = self.font_text.render('', True, (0, 0, 0))
        self.DownButton_sound_rect = self.DownButton_music.get_rect()
        self.DownButton_sound_rect.height = 30
        self.DownButton_sound_rect.width = 30
        self.DownButton_sound_rect.topleft = (screen.get_width() // 2.5 + 180, screen.get_height() // 6)
        # charger le text pour activer le mode pleine écran
        self.text_setting_full_screen_e = self.font_text.render('Full Screen enable', True, (0, 0, 0))
        self.setting_full_screen_e_rect = self.text_setting_full_screen_e.get_rect()
        self.setting_full_screen_e_rect.topleft = (screen.get_width() // 2.5 -5, screen.get_height() // 6 - (
                    screen.get_height() // 10 - screen.get_height() // 6))
        # charger le text pour désactiver le mode pleine écran
        self.text_setting_full_screen_d = self.font_text.render('Full Screen disable', True, (0, 0, 0))
        self.setting_full_screen_d_rect = self.text_setting_full_screen_d.get_rect()
        self.setting_full_screen_d_rect.topleft = (screen.get_width() // 2.5-5, screen.get_height() // 6 - 2 * (
                    screen.get_height() // 10 - screen.get_height() // 6))
        # charger le text pour retourner dans le menu
        self.text_setting_back = self.font_text.render('Back', True, (0, 0, 0))
        self.setting_back_rect = self.text_setting_back.get_rect()
        self.setting_back_rect.topleft = (screen.get_width() // 2.5 + 50, screen.get_height() // 6 - 3 * (
                    screen.get_height() // 10 - screen.get_height() // 6)-13)


class InRule:
    def __init__(self, screen):
        # charger et importer l'arrière plan
        self.background_rule = pygame.image.load('graphics/Background/Background_setting.png')
        self.background_rule = pygame.transform.scale(self.background_rule, (800, 800))
        # charger le style et la taille du text de bienvenu
        self.font_text = pygame.font.Font('dialogs/cityburn.ttf', 20)
        # importer l'arrière plan des text
        self.background_text = pygame.image.load('graphics/Background/Background_text.png')
        self.background_text = pygame.transform.scale(self.background_text, (140, 30))
        #chargé les explication du jeu
        self.text_rule_title = self.font_text.render('Les règles du jeu NinjaPython:', True, (255, 255, 255))
        self.rule_title_rect = self.text_rule_title.get_rect()
        self.rule_title_rect.topleft = (screen.get_width() // 2.5 -60, screen.get_height() // 10)
        self.text_rule = ["Le but du jeu est d'attraper le plus de serpent qui se ballade sur votre écran dans un temps ",
                          "imparti mais attention à ne pas attraper autre chose que des serpent cela pourrais être ",
                          "dangereux.Chaque mode de jeu possède sa spécificité et son rangé dans un ordre de dificulté ",
                          "croissante. Le premier est le mode facile ou le joueur possède 5 vies et 300 secondes pour ",
                          "attraper les serpents. Le deuxième mode de jeu est le mode classique ou l'on a 3 vies et 300 ",
                          "secondes pour attraper les serpents. Le quatrième mode de jeu est le mode blitz où le joueur ",
                          "possède 3 vies et 120 secondes pour attraper les serments.Et le dernier mode de jeu est le ",
                          "mode Speed Up où le joueur à 180 secondes et 5 vies pour attraper les serpent avec une ",
                          "vitesse augmenté."]
        # charger le text pour quitter
        self.text_rule_back = self.font_text.render('Back', True, (0, 0, 0))
        self.rule_back_rect = self.text_rule_back.get_rect()
        self.rule_back_rect.topleft = (screen.get_width() // 2.5 + 50, screen.get_height() // 6 - 9 * (screen.get_height() // 10 - screen.get_height() // 6)-13)

class Incredit:
    def __init__(self,screen):
        # charger et importer l'arrière plan
        self.background_credit = pygame.image.load('graphics/Background/Background_setting.png')
        self.background_credit = pygame.transform.scale(self.background_credit, (800, 800))
        # charger le style et la taille du text de bienvenu
        self.font_text = pygame.font.Font('dialogs/cityburn.ttf', 20)
        # importer l'arrière plan des text
        self.background_text = pygame.image.load('graphics/Background/Background_text.png')
        self.background_text = pygame.transform.scale(self.background_text, (140, 30))
        # chargé les explication du jeu
        self.text_credit_title = self.font_text.render('Les crédits du jeu NinjaPython:', True, (255, 255, 255))
        self.credit_title_rect = self.text_credit_title.get_rect()
        self.credit_title_rect.topleft = (screen.get_width() // 2.5 - 60, screen.get_height() // 10)
        self.text_credit = [
            "GRAPHIC:",
            "sprite: Carol-aredesu(deviant art)",
            "BackGround:FlorentLlamas(deviant art),JoeyJazz(deviant art),SebastianWagner(deviant art),",
            "ElenaDudina(deviant art),itsmejackusephot(deviant art)",
            "Le rest des ressources graphiques: Thomas DANJOU et Rayan EID",
            "Testeur: Rayan EID",
            "Dévelloppement: Thomas DANJOU",
            "Music et effet sonore: PSDK",
            "Le rest(calcule de trajectoire,idées du projet,idées des fonctionnalités,...):",
            "Guillaume BIVILLE, XIAO Jingfan, LICHNEROWICZ Achille, DESFORGES Alexandre"]
        # charger le text pour quitter
        self.text_credit_back = self.font_text.render('Back', True, (0, 0, 0))
        self.credit_back_rect = self.text_credit_back.get_rect()
        self.credit_back_rect.topleft = (screen.get_width() // 2.5 + 50, screen.get_height() // 6 - 10 * (
                    screen.get_height() // 10 - screen.get_height() // 6) - 13)
class HealthSprite(pygame.sprite.Sprite):
    def __init__(self, name, x, y):
        super().__init__()
        self.image = pygame.image.load(f'graphics/{name}.png')
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
