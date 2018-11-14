import codecs

import pygame

from painter import Painter
from vector import Vector
from drawable import Drawable
from json_storage import JSONStorage


class Scores(Drawable):
    def __init__(self, position=None, score=0, level=0, lives=3):
        if position is None:
            position = Vector()
        super(Scores, self).__init__('../resrc/tabs/game/scores.gif', position)
        pygame.font.init()
        self.font = pygame.font.Font('../resrc/fonts/default.ttf', 30)
        self.js = JSONStorage('../resrc/storage.json')
        self.score = score
        self.level = level
        self.lives = lives
        self.highscore = self.js.load().get('hs', 0)

    def set_highscore(self, hs):
        # type: (int) -> None
        """Set highscore and write it to file"""
        self.highscore = hs
        self.js.store({'hs': self.highscore})

    def add_score(self, value):
        # type: (int) -> int
        self.score += value
        if self.score >= self.highscore:
            self.set_highscore(self.score)
        return self.score

    def draw(self):
        self.image = self.font.render(
            'SCORE: {score}, LIVES: {lives}, LEVEL: {level}, HIGHSCORE: {hs}'.format(score=str(self.score),
                                                                                     level=str(self.level),
                                                                                     lives=str(self.lives),
                                                                                     hs=str(self.highscore)),
            1, (128, 128, 128))
        Painter.surface.blit(self.image, self.get_position().get())
        # Painter.draw(self.image, self.get_position())
