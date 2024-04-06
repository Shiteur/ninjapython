import pygame


class Rulle:
    def __init__(self):
        self.init_boost = 1.0
        self.add_boost = 1.1
        self.health_player = 3
        self.palier = 25
        self.score_boost = 1
        self.init_object_nb = 3
        self.add_object_nb = 2
        self.limit_time = 300

    def set_init_boost(self, amount):
        self.init_boost = amount

    def set_add_boost(self, amount):
        self.add_boost = amount

    def set_palier(self, amount):
        self.palier = amount

    def set_health_player(self, amount):
        self.health_player = amount

    def set_score_boost(self, amount):
        self.score_boost = amount

    def set_init_object_nb(self, amount):
        self.init_object_nb = amount

    def set_add_object_nb(self, amount):
        self.add_object_nb = amount

    def set_limit_time(self, amount):
        self.limit_time = amount

    def check_palier(self, score):
          return score // self.palier


class RulleClassique(Rulle):
    def __init__(self):
        super().__init__()
        self.set_init_boost(1.0)
        self.set_add_boost(1.1)
        self.set_health_player(3)
        self.set_palier(30)
        self.set_score_boost(1)
        self.set_init_object_nb(2)
        self.set_add_object_nb(2)
        self.set_limit_time(300)


class RulleBlitz(Rulle):
    def __init__(self):
        super().__init__()
        self.set_init_boost(1.0)
        self.set_add_boost(1.1)
        self.set_health_player(3)
        self.set_palier(15)
        self.set_score_boost(3)
        self.set_init_object_nb(3)
        self.set_add_object_nb(2)
        self.set_limit_time(120)

class RulleBeginner(Rulle):
    def __init__(self):
        super().__init__()
        self.set_init_boost(1.0)
        self.set_add_boost(1.1)
        self.set_health_player(5)
        self.set_palier(30)
        self.set_score_boost(1)
        self.set_init_object_nb(1)
        self.set_add_object_nb(1)
        self.set_limit_time(300)

class RulleSpeedUp(Rulle):
    def __init__(self):
        super().__init__()
        self.set_init_boost(1.5)
        self.set_add_boost(1.2)
        self.set_health_player(5)
        self.set_palier(30)
        self.set_score_boost(5)
        self.set_init_object_nb(2)
        self.set_add_object_nb(1)
        self.set_limit_time(180)