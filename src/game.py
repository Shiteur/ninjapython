from graphics import *
from gameobject import *
from musics import *
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
        # définir si on est sur l'écran de prarmètre
        self.in_setting = False
        # définir si on est sur l'écran de crédits
        self.in_credit = False
        # définir si on est sur l'écran de règle
        self.in_rule = False
        # définir si on est en train de joué et à quel jeu on joue
        self.level = -1
        # gérer les effets sonore et la musique
        self.sound_manager = SoundManager()
        self.music_manager = MusicManager()
        self.current_music = 'intro'
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
        # initialise le temps
        self.time = 0
        # Groupe d'objet
        self.nb_object = self.rulle.init_object_nb
        self.all_object = pygame.sprite.Group()
        self.possible_object = [SnakeA1, SnakeB1, SnakeC1, SnakeD1, DumyA1, DumyB1, SnakeA2, SnakeB2, SnakeC2, SnakeD2,
                                DumyC1, DumyD1, SnakeSpeA1, SnakeSpeB1, DumyA2, DumyB2, SnakeA3, SnakeB3, SnakeC3,
                                SnakeD3, SnakeSpeA2, SnakeSpeB2, DumyC2, DumyD2]


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
        if self.rulle.check_palier(self.score) >= 6:
            object.volcity=object.volcity*(self.rulle.check_palier(self.score)-6*self.rulle.add_boost+self.rulle.init_boost)
        else:
            object.volcity = object.volcity * self.rulle.init_boost
        self.all_object.add(object)

    def choose_rulle(self):
        self.rulle = self.possible_rulle[self.level]()

    def add_nb_object(self, amount, nb):
        self.nb_object = self.rulle.init_object_nb + amount * nb

    def randomize(self):
        if self.rulle.check_palier(self.score) >= 5:
            nb = random.randint(1, len(self.possible_object))
            self.add_nb_object(self.rulle.add_object_nb, 3)
        elif self.rulle.check_palier(self.score) >= 4:
            nb = random.randint(1, len(self.possible_object)-4)
            self.add_nb_object(self.rulle.add_object_nb, 3)
        elif self.rulle.check_palier(self.score) >= 3:
            nb = random.randint(1, len(self.possible_object)-10)
            self.add_nb_object(self.rulle.add_object_nb, 2)
        elif self.rulle.check_palier(self.score) >= 2:
            nb = random.randint(1, len(self.possible_object) - 14)
            self.add_nb_object(self.rulle.add_object_nb, 2)
        elif self.rulle.check_palier(self.score) >= 1:
            nb = random.randint(1, len(self.possible_object) - 18)
            self.add_nb_object(self.rulle.add_object_nb, 1)
        else:
            nb = random.randint(1, len(self.possible_object) - 20)
            self.add_nb_object(self.rulle.add_object_nb, 0)
        return self.possible_object[nb-1]

    def need_spawn_object(self, nb):
        if len(self.all_object) < nb:
            self.spawn_game_object(self.randomize())

    def add_score(self, points=1):
        self.score += points * self.rulle.score_boost

    def run(self):
        # génère la musique
        self.music_manager.play_music(self.current_music)

        intro = IntroScreen(self.screen)
        menu = MainMenu(self.screen)
        ingame = InGame(self.screen)
        insetting = InSetting(self.screen)
        inrule = InRule(self.screen)

        clock = pygame.time.Clock()
        # boucle du jeu
        running = True
        #génère un minuteur:
        start_tiks = pygame.time.get_ticks()
        while running:
            # Vérifié si on est sur l'écran d'accueil
            if self.is_starting:
                # change la musique si besoin
                self.current_music = self.music_manager.need_change_music(self.current_music, 'intro')
                # affiche l'arière plan de l' écran d'accueil
                self.screen.blit(intro.background, (0,0))
                # affiche le titre du jeu
                self.screen.blit(intro.text_title, intro.title_rect)
                # affiche la phrase de bienvenu
                self.screen.blit(intro.text_text, intro.text_rect)
                # joue la musique de l'écran de bienvenu

            elif self.in_menu:
                # change la musique si besoin
                self.current_music = self.music_manager.need_change_music(self.current_music, 'select_level')
                # affiche l'arière plan de l' écran du menu
                self.screen.blit(menu.background, (0, 0))
                # affiche les niveau
                self.screen.blit(menu.background_text, (self.screen.get_width() // 2.5, self.screen.get_height() // 10-5))
                self.screen.blit(menu.text_game_beginner, menu.game_beginner_rect)
                self.screen.blit(menu.background_text, (self.screen.get_width() // 2.5, self.screen.get_height() // 6-5))
                self.screen.blit(menu.text_game_classique, menu.game_classique_rect)
                self.screen.blit(menu.background_text, (self.screen.get_width() // 2.5, self.screen.get_height() // 6 - (self.screen.get_height() // 10 - self.screen.get_height() // 6)-5))
                self.screen.blit(menu.text_game_blitz, menu.game_blitz_rect)
                self.screen.blit(menu.background_text, (self.screen.get_width() // 2.5, self.screen.get_height() // 6-2 * (self.screen.get_height() // 10 - self.screen.get_height() // 6)-5))
                self.screen.blit(menu.text_game_speedup, menu.game_speedup_rect)
                self.screen.blit(menu.background_text, (self.screen.get_width() // 2.5, self.screen.get_height() // 6-3 * (self.screen.get_height() // 10 - self.screen.get_height() // 6)-5))
                self.screen.blit(menu.text_game_setting, menu.game_setting_rect)
                self.screen.blit(menu.background_text, (self.screen.get_width() // 2.5, self.screen.get_height() // 6-4 * (self.screen.get_height() // 10 - self.screen.get_height() // 6)-5))
                self.screen.blit(menu.text_game_credit, menu.game_credit_rect)
                self.screen.blit(menu.background_text, (self.screen.get_width() // 2.5,self.screen.get_height() // 6-5 * (self.screen.get_height() // 10 - self.screen.get_height() // 6) - 5))
                self.screen.blit(menu.text_game_rule, menu.game_rule_rect)
                self.screen.blit(menu.background_text, (self.screen.get_width() // 2.5,self.screen.get_height() // 6 - 6 * (self.screen.get_height() // 10 - self.screen.get_height() // 6) - 5))
                self.screen.blit(menu.text_game_leave, menu.game_leave_rect)

            elif self.in_setting:
                # affiche l'arière plan de l' écran des paramètre
                self.screen.blit(insetting.background_setting, (0, 0))
                self.screen.blit(insetting.UpButton_music, (self.screen.get_width() // 2.5 - 60, self.screen.get_height() //10))
                self.screen.blit(insetting.DownButton_music, (self.screen.get_width() // 2.5 + 180, self.screen.get_height() //10))
                self.screen.blit(insetting.UpButton_music_text, insetting.UpButton_music_rect)
                self.screen.blit(insetting.DownButton_music_text, insetting.DownButton_music_rect)
                music_text = self.score_font.render(f'Music Volume = {self.music_manager.level_music}', 1, (255, 255, 255))
                self.screen.blit(music_text, (self.screen.get_width() // 2.5-5, self.screen.get_height() // 10))
                self.screen.blit(insetting.UpButton_sound,(self.screen.get_width() // 2.5 - 60, self.screen.get_height() // 6))
                self.screen.blit(insetting.DownButton_sound,(self.screen.get_width() // 2.5 + 180, self.screen.get_height() // 6))
                self.screen.blit(insetting.UpButton_sound_text, insetting.UpButton_sound_rect)
                self.screen.blit(insetting.DownButton_sound_text, insetting.DownButton_sound_rect)
                sound_text = self.score_font.render(f'Sound Volume = {self.sound_manager.level_sounds}', 1, (255, 255, 255))
                self.screen.blit(sound_text, (self.screen.get_width() // 2.5 - 5, self.screen.get_height() // 6))
                self.screen.blit(insetting.background_text2, (self.screen.get_width() // 2.5-20,self.screen.get_height() // 6 - (self.screen.get_height() // 10 - self.screen.get_height() // 6) - 5))
                self.screen.blit(insetting.text_setting_full_screen_e, insetting.setting_full_screen_e_rect)
                self.screen.blit(insetting.background_text2, (self.screen.get_width() // 2.5-20,self.screen.get_height() // 6 - 2 * (self.screen.get_height() // 10 - self.screen.get_height() // 6) - 5))
                self.screen.blit(insetting.text_setting_full_screen_d, insetting.setting_full_screen_d_rect)
                self.screen.blit(insetting.background_text1, (self.screen.get_width() // 2.5,self.screen.get_height() // 6 - 3 * (self.screen.get_height() // 10 - self.screen.get_height() // 6) - 5))
                self.screen.blit(insetting.text_setting_back, insetting.setting_back_rect)

            elif self.in_rule:
                # affiche l'arière plan de l' écran des règle
                self.screen.blit(inrule.background_rule, (0, 0))
                self.screen.blit(inrule.text_rule_title, inrule.rule_title_rect)
                for i in range(0,len(inrule.text_rule)):
                    self.screen.blit(self.score_font.render(inrule.text_rule[i], 1, (255, 255, 255)),(15, self.screen.get_height()//6- i * (self.screen.get_height() // 10 - self.screen.get_height() // 6)))
                self.screen.blit(inrule.background_text,(self.screen.get_width() // 2.5,self.screen.get_height() // 6 - 9 * (self.screen.get_height() // 10 - self.screen.get_height() // 6) - 5))
                self.screen.blit(inrule.text_rule_back,inrule.rule_back_rect)

            else:
                # change la musique si besoin
                self.current_music = self.music_manager.need_change_music(self.current_music, self.rulle.music)
                # affiche l'arière plan de l' écran de jeu
                if (self.level==2 or self.level==0):
                    self.screen.blit(ingame.background_classique, (0, 0))
                if(self.level==1 or self.level==3):
                    self.screen.blit(ingame.background_hard, (0, 0))
                self.need_spawn_object(self.nb_object)
                for obj in self.all_object:
                    obj.move(self.screen)

                # affiche les objet à détruire
                self.all_object.draw(self.screen)
                self.all_health.draw(self.screen)

                # affiche le score à l'écran
                score_text = self.score_font.render(f'Score : {self.score}', 1, (255, 255, 255))
                self.screen.blit(score_text, (10, 10))
                # affiche le temps à l'écran
                self.time=(pygame.time.get_ticks()-start_tiks)//1000
                time_text = self.score_font.render(f'Temps : {self.time}/{self.rulle.limit_time}',1,(255, 255, 255))
                self.screen.blit(time_text, (10, 40))

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
                            start_tiks = pygame.time.get_ticks()
                        elif menu.game_blitz_rect.collidepoint(event.pos):
                            self.level = 1
                            self.choose_rulle()
                            self.sound_manager.play('click')
                            self.game_start()
                            start_tiks = pygame.time.get_ticks()
                        elif menu.game_beginner_rect.collidepoint(event.pos):
                            self.level = 2
                            self.choose_rulle()
                            self.sound_manager.play('click')
                            self.game_start()
                            start_tiks = pygame.time.get_ticks()
                        elif menu.game_speedup_rect.collidepoint(event.pos):
                            self.level = 3
                            self.choose_rulle()
                            self.sound_manager.play('click')
                            self.game_start()
                            start_tiks = pygame.time.get_ticks()
                        elif menu.game_setting_rect.collidepoint(event.pos):
                            self.sound_manager.play('click')
                            self.in_menu=False
                            self.in_setting=True
                        elif menu.game_rule_rect.collidepoint(event.pos):
                            self.sound_manager.play('click')
                            self.in_menu=False
                            self.in_rule=True
                        elif menu.game_leave_rect.collidepoint(event.pos):
                            self.sound_manager.play('click')
                            pygame.quit()

                    elif self.in_setting:
                        if insetting.setting_back_rect.collidepoint(event.pos):
                            self.sound_manager.play('click')
                            self.in_setting = False
                            self.in_menu = True
                        elif insetting.setting_full_screen_e_rect.collidepoint(event.pos):
                            self.sound_manager.play('click')
                            self.screen = pygame.display.set_mode((800, 600), pygame.FULLSCREEN)
                        elif insetting.setting_full_screen_d_rect.collidepoint(event.pos):
                            self.sound_manager.play('click')
                            self.screen = pygame.display.set_mode((800, 600))
                        elif insetting.UpButton_music_rect.collidepoint(event.pos) and self.music_manager.level_music < 100:
                            self.sound_manager.play('click')
                            self.music_manager.level_music += 5
                            self.music_manager.change_volume()
                        elif insetting.DownButton_music_rect.collidepoint(event.pos) and self.music_manager.level_music > 0:
                            self.sound_manager.play('click')
                            self.music_manager.level_music -= 5
                            self.music_manager.change_volume()
                        elif insetting.UpButton_sound_rect.collidepoint(event.pos) and self.sound_manager.level_sounds < 100:
                            self.sound_manager.level_sounds += 5
                            self.sound_manager.play('click')
                        elif insetting.DownButton_sound_rect.collidepoint(event.pos) and self.sound_manager.level_sounds> 0:
                            self.sound_manager.level_sounds -= 5
                            self.sound_manager.play('click')

                    elif self.in_rule:
                        if inrule.rule_back_rect.collidepoint(event.pos):
                            self.sound_manager.play('click')
                            self.in_rule = False
                            self.in_menu= True

                    elif self.level != -1:
                        for obj in self.all_object:
                            if obj.rect.collidepoint(event.pos):
                                self.sound_manager.play('click_attack')
                                if obj.name in ['DumyA1','DumyA2','DumyB1','DumyB2','DumyC1','DumyC2','DumyD1','DumyD2']:
                                    self.sound_manager.play('destroy2')
                                    self.health.get_damage(obj.damage)
                                    self.rulle.limit_time += obj.extra_time
                                    self.update_health()
                                    obj.remove(self.all_object)
                                    self.need_spawn_object(self.nb_object)
                                else:
                                    self.need_spawn_object(self.nb_object)
                                    obj.damage_take(self.health.damage, self.all_object)

            if self.level != -1:
                if self.time == self.rulle.limit_time:
                    self.game_over()

            for obj in self.all_object:
                if obj.rect.x<-1 or obj.rect.x>(self.screen.get_width()+1 ):
                    obj.remove(self.all_object)
                    if obj.name in ['DumyA1','DumyA2','DumyB1','DumyB2','DumyC1','DumyC2','DumyD1','DumyD2']:
                        self.add_score(obj.loot_amount)
                    else:
                        self.health.get_damage(obj.damage)
                    self.update_health()
                    if self.health.current_health > 0:
                        self.need_spawn_object(self.nb_object)

            clock.tick(60)

        pygame.quit()
