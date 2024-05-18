import pygame


class SoundManager:
    def __init__(self):
        self.sounds = {
            'click': pygame.mixer.Sound('Sounds/click.ogg'),
            'game_over': pygame.mixer.Sound('Sounds/game_over.ogg'),
            'click_attack': pygame.mixer.Sound('Sounds/attack_click.ogg'),
            'destroy1': pygame.mixer.Sound('Sounds/destroy_good_object.ogg'),
            'destroy2': pygame.mixer.Sound('Sounds/destroy_wrong_object.ogg')
        }
        self.level_sounds = 10

    def play(self, name):
        self.sounds[name].set_volume(0.01*self.level_sounds)
        self.sounds[name].play()
