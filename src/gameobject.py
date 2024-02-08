import pygame
import random
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
        self.volcity = random.randint(vmin, vmax) *0.7
        self.curve = random.randint(0, 12)
        self.loot_amount = 1
        self.name = name

    def damage_take(self, amount, groupe):
        self.health -= amount

        if self.health <= 0:
            self.remove(groupe)
            #joué le son de mort
            self.sounds.play('destroy1')
            #ajouter des point au score
            self.game.add_score(self.loot_amount)

    def set_loot_amount(self, amount):
        self.loot_amount = amount

    def move(self, screen):
        if self.curve > 8:
            if (self.spawn_x < screen.get_width()//2) and (self.spawn_y < screen.get_height()//2):
                self.rect.x += self.volcity
                self.rect.y += self.volcity
            elif (self.spawn_x >= screen.get_width()//2) and (self.spawn_y < screen.get_height()//2):
                self.rect.x -= self.volcity
                self.rect.y += self.volcity
            elif (self.spawn_x >= screen.get_width()//2) and (self.spawn_y >= screen.get_height()//2):
                self.rect.x -= self.volcity
                self.rect.y -= self.volcity
            else:
                self.rect.x += self.volcity
                self.rect.y -= self.volcity
        elif self.curve > 4:
            if (self.spawn_x < screen.get_width()//2) and (self.spawn_y < screen.get_height()//2):
                self.rect.x += 2 * self.volcity
                self.rect.y += self.volcity
            elif (self.spawn_x >= screen.get_width()//2) and (self.spawn_y < screen.get_height()//2):
                self.rect.x -= 2 * self.volcity
                self.rect.y += self.volcity
            elif (self.spawn_x >= screen.get_width()//2) and (self.spawn_y >= screen.get_height()//2):
                self.rect.x -= 2 * self.volcity
                self.rect.y -= self.volcity
            else:
                self.rect.x += 2 * self.volcity
                self.rect.y -= self.volcity
        else:
            if (self.spawn_x < screen.get_width()//2) and (self.spawn_y < screen.get_height()//2):
                self.rect.x += self.volcity
                self.rect.y += 3 * self.volcity
            elif (self.spawn_x >= screen.get_width()//2) and (self.spawn_y < screen.get_height()//2):
                self.rect.x -= self.volcity
                self.rect.y += 3 * self.volcity
            elif (self.spawn_x >= screen.get_width()//2) and (self.spawn_y >= screen.get_height()//2):
                self.rect.x -= self.volcity
                self.rect.y -= 3 * self.volcity
            else:
                self.rect.x += self.volcity
                self.rect.y -= 3 * self.volcity


# on défini ici une classe pour chaque objet à détruire
class Bulbizarre(Object):
    def __init__(self, game):
        super().__init__(game, 'Bulbizarre', 1, 1, 1, 1)
        self.set_loot_amount(1)


class Herbizarre(Object):
    def __init__(self, game):
        super().__init__(game, 'Herbizarre', 1, 1, 1, 2)
        self.set_loot_amount(5)


class Florizarre(Object):
    def __init__(self, game):
        super().__init__(game, 'Florizarre', 2, 1, 1, 3)
        self.set_loot_amount(10)


class Salamèche(Object):
    def __init__(self, game):
        super().__init__(game, 'Salamèche', 1, 1, 1, 1)
        self.set_loot_amount(1)


class Reptincel(Object):
    def __init__(self, game):
        super().__init__(game, 'Reptincel', 1, 1, 1, 2)
        self.set_loot_amount(5)


class Dracaufeu(Object):
    def __init__(self, game):
        super().__init__(game, 'Dracaufeu', 2, 1, 1, 3)
        self.set_loot_amount(10)


class Carapuce(Object):
    def __init__(self, game):
        super().__init__(game, 'Carapuce', 1, 1, 1, 1)
        self.set_loot_amount(1)


class Carabaffe(Object):
    def __init__(self, game):
        super().__init__(game, 'Carabaffe', 1, 1, 1, 2)
        self.set_loot_amount(5)


class Tortank(Object):
    def __init__(self, game):
        super().__init__(game, 'Tortank', 2, 1, 1, 3)
        self.set_loot_amount(10)


class Racaillou(Object):
    def __init__(self, game):
        super().__init__(game, 'Racaillou', 1, 1, 1, 1)
        self.set_loot_amount(1)


class Gravalanch(Object):
    def __init__(self, game):
        super().__init__(game, 'Gravalanch', 1, 1, 1, 2)
        self.set_loot_amount(5)


class Grolem(Object):
    def __init__(self, game):
        super().__init__(game, 'Grolem', 1, 2, 1, 3)
        self.set_loot_amount(10)


class Voltrobe(Object):
    def __init__(self, game):
        super().__init__(game, 'Voltrobe', 1, 1, 1, 1)
        self.set_loot_amount(1)


class Electrode(Object):
    def __init__(self, game):
        super().__init__(game, 'Electrode', 1, 2, 1, 2)
        self.set_loot_amount(5)
