import pygame

class MusicManager:

    def __init__(self):
        self.music = {
            'intro': 'musics/intro.ogg',
            'game_music1': 'musics/volt_ost.ogg',
            'game_music2': 'musics/xy_gts.ogg',
            'select_level': 'musics/hall-of-fame.ogg'
        }
        self.level_music = 20

    def play_music(self, name):
        pygame.mixer.init()
        pygame.mixer.music.load(self.music[name])
        pygame.mixer.music.set_volume(0.01*self.level_music)
        pygame.mixer.music.play(-1)

    def change_volume(self):
        pygame.mixer.music.set_volume(0.01 * self.level_music)

    def need_change_music(self, curent_music, new_music):
        if curent_music != new_music:
            curent_music = new_music
            pygame.mixer.stop()
            self.play_music(curent_music)
        return curent_music
