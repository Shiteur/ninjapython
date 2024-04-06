from graphics import *
from gameobject import *
from sounds import *
from rulle import *
import pygame
import random


class Game:

    def __init__(self):
        # création de fenêtre pour le jeu
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("python ninja")

        # définir si on est sur l'écran titre
        self.is_starting = True
        # définir si on est sur l'écran d'acceuil
        self.in_menu = False
        # définir si on est en train de joué et à quel jeu on joue
        self.level = -1
        # gérer les effets sonore et la musique
        self.sound_manager = SoundManager()
        # Mettre le score du joueur à 0
        self.score = 0
        self.score_font = pygame.font.Font('dialogs/cityburn.ttf', 20)
        # Généré la vie du joueur
        self.all_health = pygame.sprite.Group()
        self.health = Health(self, 3, 1)
        self.update_health()
        # Générer les règle
        self.rulle = Rulle()
        self.possible_rulle = [RulleClassique, RulleBlitz, RulleBeginner, RulleSpeedUp]
        # Groupe d'objet
        self.nb_object = self.rulle.init_object_nb
        self.all_object = pygame.sprite.Group()
        self.possible_object = [Bulbizarre,Salamèche,Carapuce,Racaillou,Voltrobe,Herbizarre,Reptincel,Carabaffe,Gravalanch,Electrode,Florizarre,Dracaufeu,Tortank,Grolem]


    def game_start(self):
        self.in_menu = False
        self.nb_object = self.rulle.init_object_nb
        self.health = Health(self, self.rulle.health_player, 1)
        self.need_spawn_object(self.nb_object)
        self.need_spawn_object(self.nb_object)
        self.need_spawn_object(self.nb_object)
        self.update_health()

    def game_over(self):
        self.all_object = pygame.sprite.Group()
        self.all_health = pygame.sprite.Group()
        self.update_health()
        self.in_menu = True
        self.level = 0
        self.score = 0
        self.sound_manager.play('game_over')

    def spawn_health(self, name, y):
        health = HealthSprite(name, self.screen.get_width() - 30 * y, 10)
        self.all_health.add(health)

    def update_health(self):
        self.all_health = pygame.sprite.Group()
        for i in range(self.health.max_health):
            if i < self.health.current_health:
                self.spawn_health('heart', i+1)
            else:
                self.spawn_health('heart_kill', i+1)

    def spawn_game_object(self, object_class_name):
        object = object_class_name.__call__(self)
        if self.rulle.check_palier(self.score) >= 5:
            object.volcity=object.volcity*(self.rulle.check_palier(self.score)-5*self.rulle.add_boost+self.rulle.init_boost)
        else:
            object.volcity = object.volcity * self.rulle.init_boost
        self.all_object.add(object)

    def choose_rulle(self):
        self.rulle = self.possible_rulle[self.level]()

    def add_nb_object(self, amount, nb):
        self.nb_object = self.rulle.init_object_nb + amount * nb

    def randomize(self):
        if self.rulle.check_palier(self.score) >= 4:
            nb = random.randint(1, len(self.possible_object))
            self.add_nb_object(self.rulle.add_object_nb, 4)
        elif self.rulle.check_palier(self.score) >= 3:
            nb = random.randint(1, len(self.possible_object)-4)
            self.add_nb_object(self.rulle.add_object_nb, 3)
        elif self.rulle.check_palier(self.score) >= 2:
            nb = random.randint(1, len(self.possible_object) - 6)
            self.add_nb_object(self.rulle.add_object_nb, 2)
        elif self.rulle.check_palier(self.score) >= 1:
            nb = random.randint(1, len(self.possible_object) - 9)
            self.add_nb_object(self.rulle.add_object_nb, 1)
        else:
            nb = random.randint(1, len(self.possible_object) - 11)
            self.add_nb_object(self.rulle.add_object_nb, 0)
        return self.possible_object[nb-1]

    def need_spawn_object(self, nb):
        if len(self.all_object) < nb:
            self.spawn_game_object(self.randomize())

    def add_score(self, points=1):
        self.score += points * self.rulle.score_boost

    def run(self):
        # génère la musique
        pygame.mixer.init()
        pygame.mixer.music.load('musics/volt_ost.ogg')
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)

        intro = IntroScreen(self.screen)
        menu = MainMenu(self.screen)
        ingame = InGame(self.screen)

        clock = pygame.time.Clock()
        # boucle du jeu
        running = True
        while running:
            # Vérifié si on est sur l'écran d'accueil
            if self.is_starting:
                # affiche l'arière plan de l' écran d'accueil
                self.screen.blit(intro.background, (0,0))
                # affiche le titre du jeu
                self.screen.blit(intro.text_title, intro.title_rect)
                # affiche la phrase de bienvenu
                self.screen.blit(intro.text_text, intro.text_rect)
                # joue la musique de l'écran de bienvenu

            elif self.in_menu:
                # affiche l'arière plan de l' écran du menu
                self.screen.blit(menu.background, (0, 0))
                # affiche les niveau
                self.screen.blit(menu.text_game_beginner, menu.game_beginner_rect)
                self.screen.blit(menu.text_game_classique, menu.game_classique_rect)
                self.screen.blit(menu.text_game_blitz, menu.game_blitz_rect)
                self.screen.blit(menu.text_game_speedup, menu.game_speedup_rect)

            else:
                # affiche l'arière plan de l' écran de jeu
                self.screen.blit(ingame.background, (0, 0))
                self.need_spawn_object(self.nb_object)
                for obj in self.all_object:
                    obj.move(self.screen)

                # affiche les objet à détruire
                self.all_object.draw(self.screen)
                self.all_health.draw(self.screen)

                # affiche le score à l'écran
                score_text = self.score_font.render(f'Score : {self.score}', 1, (0, 0, 0))
                self.screen.blit(score_text, (10, 10))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if self.is_starting:
                            self.is_starting = False
                            self.in_menu = True
                            self.sound_manager.play('click')

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.is_starting:
                        self.is_starting = False
                        self.in_menu = True
                        self.sound_manager.play('click')

                    elif self.in_menu:
                        if menu.game_classique_rect.collidepoint(event.pos):
                            self.level = 0
                            self.choose_rulle()
                            self.sound_manager.play('click')
                            self.game_start()
                        elif menu.game_blitz_rect.collidepoint(event.pos):
                            self.level = 1
                            self.choose_rulle()
                            self.sound_manager.play('click')
                            self.game_start()
                        elif menu.game_beginner_rect.collidepoint(event.pos):
                            self.level = 2
                            self.choose_rulle()
                            self.sound_manager.play('click')
                            self.game_start()
                        elif menu.game_speedup_rect.collidepoint(event.pos):
                            self.level = 3
                            self.choose_rulle()
                            self.sound_manager.play('click')
                            self.game_start()

                    elif self.level != -1:
                        for obj in self.all_object:
                            if obj.rect.collidepoint(event.pos):
                                self.sound_manager.play('click_attack')
                                if obj.name in ['Racaillou','Gravalanch','Grolem','Voltrobe','Electrode']:
                                    self.sound_manager.play('destroy2')
                                    self.health.get_damage(obj.damage)
                                    self.update_health()
                                    obj.remove(self.all_object)
                                    self.need_spawn_object(self.nb_object)
                                else:
                                    self.need_spawn_object(self.nb_object)
                                    obj.damage_take(self.health.damage, self.all_object)

            for obj in self.all_object:
                if obj.rect.x<-1 or obj.rect.x>(self.screen.get_width()+1 ):
                    obj.remove(self.all_object)
                    if obj.name in ['Racaillou','Gravalanch','Grolem','Voltrobe','Electrode']:
                        self.add_score(obj.loot_amount)
                    else:
                        self.health.get_damage(obj.damage)
                    self.update_health()
                    if self.health.current_health > 0:
                        self.need_spawn_object(self.nb_object)

            clock.tick(60)

        pygame.quit()
