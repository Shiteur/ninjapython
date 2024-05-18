import pygame
import random
import math
from src.sounds import SoundManager


class Health(pygame.sprite.Sprite):
    def __init__(self,  game, x, d):
        super().__init__()
        self.current_health = x
        self.max_health = x
        self.damage = d
        self.game = game

    def get_damage(self, amount):
        self.current_health -= amount
        if self.current_health <= 0:
            self.game.game_over()


class Object(pygame.sprite.Sprite):
    def __init__(self, game, name, h, dmg, vmin, vmax):
        super().__init__()
        self.sounds = SoundManager()
        self.game = game
        self.health = h
        self.damage = dmg
        self.image = pygame.image.load(f'graphics/object/{name}.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, self.game.screen.get_width()-10)
        self.rect.y = random.randint(0, self.game.screen.get_height()-10)
        self.spawn_x = self.rect.x
        self.spawn_y = self.rect.y
        self.volcity = random.randint(vmin, vmax) * 0.7
        self.curve = random.randint(0, 12)
        self.loot_amount = 1
        self.extra_time = 0
        self.name = name

    def damage_take(self, amount, groupe):
        self.health -= amount

        if self.health <= 0:
            self.remove(groupe)
            #joué le son de mort
            self.sounds.play('destroy1')
            #ajouter des point au score
            self.game.add_score(self.loot_amount)
            #ajouter le temp supplémentaire accordé par l'objet
            self.game.rulle.limit_time += self.extra_time

    def set_loot_amount(self, amount):
        self.loot_amount = amount

    def set_extra_time(self, time):
        self.extra_time = time

    def move(self, screen):
        if self.curve > 8:
            if (self.spawn_x < screen.get_width()//2) and (self.spawn_y < screen.get_height()//2):
                self.rect.x += 1
                self.rect.y = self.rect.x//2 + self.volcity
            elif (self.spawn_x >= screen.get_width()//2) and (self.spawn_y < screen.get_height()//2):
                self.rect.x -= 1
                self.rect.y = self.rect.x//2 + self.volcity
            elif (self.spawn_x >= screen.get_width()//2) and (self.spawn_y >= screen.get_height()//2):
                self.rect.x -= 1
                self.rect.y = self.rect.x//2 + self.volcity
            else:
                self.rect.x += 1
                self.rect.y = self.rect.x//2 + self.volcity
        elif self.curve > 4:
            if (self.spawn_x < screen.get_width()//2) and (self.spawn_y < screen.get_height()//2):
                self.rect.x += 1
                self.rect.y = screen.get_height()//2 * math.sin(self.rect.x*10**-2)+screen.get_height()//2
            elif (self.spawn_x >= screen.get_width()//2) and (self.spawn_y < screen.get_height()//2):
                self.rect.x -= 1
                self.rect.y = screen.get_height()//2 * math.sin(self.rect.x*10**-2)+screen.get_height()//2
            elif (self.spawn_x >= screen.get_width()//2) and (self.spawn_y >= screen.get_height()//2):
                self.rect.x -= 1
                self.rect.y = screen.get_height()//2 * math.sin(self.rect.x*10**-2)+screen.get_height()//2
            else:
                self.rect.x += 1
                self.rect.y = screen.get_height()//2 * math.sin(self.rect.x*10**-2)+screen.get_height()//2
        else:
            if (self.spawn_x < screen.get_width()//2) and (self.spawn_y < screen.get_height()//2):
                self.rect.x += 1
                self.rect.y = -self.rect.x **2//200 + self.rect.x*4-230
            elif (self.spawn_x >= screen.get_width()//2) and (self.spawn_y < screen.get_height()//2):
                self.rect.x -= 1
                self.rect.y = -self.rect.x **2//200+ self.rect.x*4-230
            elif (self.spawn_x >= screen.get_width()//2) and (self.spawn_y >= screen.get_height()//2):
                self.rect.x -= 1
                self.rect.y = -self.rect.x **2//200+ self.rect.x*4-230
            else:
                self.rect.x += 1
                self.rect.y = -self.rect.x **2//200+ self.rect.x*4-230


# on défini ici une classe pour chaque objet à détruire
class SnakeA1(Object):
    def __init__(self, game):
        super().__init__(game, 'SnakeA1', 1, 1, 1, 1)
        self.set_loot_amount(1)


class SnakeA2(Object):
    def __init__(self, game):
        super().__init__(game, 'SnakeA2', 1, 1, 1, 2)
        self.set_loot_amount(5)


class SnakeA3(Object):
    def __init__(self, game):
        super().__init__(game, 'SnakeA3', 2, 1, 1, 3)
        self.set_loot_amount(10)


class SnakeB1(Object):
    def __init__(self, game):
        super().__init__(game, 'SnakeB1', 1, 1, 1, 1)
        self.set_loot_amount(1)


class SnakeB2(Object):
    def __init__(self, game):
        super().__init__(game, 'SnakeB2', 1, 1, 1, 2)
        self.set_loot_amount(5)


class SnakeB3(Object):
    def __init__(self, game):
        super().__init__(game, 'SnakeB3', 2, 1, 1, 3)
        self.set_loot_amount(10)


class SnakeC1(Object):
    def __init__(self, game):
        super().__init__(game, 'SnakeC1', 1, 1, 1, 1)
        self.set_loot_amount(1)


class SnakeC2(Object):
    def __init__(self, game):
        super().__init__(game, 'SnakeC2', 1, 1, 1, 2)
        self.set_loot_amount(5)


class SnakeC3(Object):
    def __init__(self, game):
        super().__init__(game, 'SnakeC3', 2, 1, 1, 3)
        self.set_loot_amount(10)


class SnakeD1(Object):
    def __init__(self, game):
        super().__init__(game, 'SnakeD1', 1, 1, 1, 1)
        self.set_loot_amount(1)


class SnakeD2(Object):
    def __init__(self, game):
        super().__init__(game, 'SnakeD2', 1, 1, 1, 2)
        self.set_loot_amount(5)


class SnakeD3(Object):
    def __init__(self, game):
        super().__init__(game, 'SnakeD3', 2, 1, 1, 3)
        self.set_loot_amount(10)


class SnakeSpeA1(Object):
    def __init__(self, game):
        super().__init__(game, 'SnakeSpeA1', 1, 1, 1, 1)
        self.set_loot_amount(1)
        self.set_extra_time(5)


class SnakeSpeA2(Object):
    def __init__(self, game):
        super().__init__(game, 'SnakeSpeA2', 1, 1, 1, 2)
        self.set_loot_amount(5)
        self.set_extra_time(10)


class SnakeSpeB1(Object):
    def __init__(self, game):
        super().__init__(game, 'SnakeSpeB1', 1, 1, 1, 1)
        self.set_loot_amount(1)
        self.set_extra_time(5)


class SnakeSpeB2(Object):
    def __init__(self, game):
        super().__init__(game, 'SnakeSpeB2', 1, 1, 1, 3)
        self.set_loot_amount(10)
        self.set_extra_time(10)


class DumyA1(Object):
    def __init__(self, game):
        super().__init__(game, 'DumyA1', 1, 1, 1, 1)
        self.set_loot_amount(1)


class DumyA2(Object):
    def __init__(self, game):
        super().__init__(game, 'DumyA2', 1, 2, 1, 2)
        self.set_loot_amount(5)


class DumyB1(Object):
    def __init__(self, game):
        super().__init__(game, 'DumyB1', 1, 1, 1, 1)
        self.set_loot_amount(1)


class DumyB2(Object):
    def __init__(self, game):
        super().__init__(game, 'DumyB2', 1, 2, 1, 2)
        self.set_loot_amount(5)


class DumyC1(Object):
    def __init__(self, game):
        super().__init__(game, 'DumyC1', 1, 1, 1, 2)
        self.set_loot_amount(1)


class DumyC2(Object):
    def __init__(self, game):
        super().__init__(game, 'DumyC2', 1, 3, 1, 3)
        self.set_loot_amount(10)


class DumyD1(Object):
    def __init__(self, game):
        super().__init__(game, 'DumyD1', 1, 1, 1, 1)
        self.set_loot_amount(1)


class DumyD2(Object):
    def __init__(self, game):
        super().__init__(game, 'DumyD2', 1, 2, 1, 3)
        self.set_loot_amount(10)
        self.set_extra_time(-10)
