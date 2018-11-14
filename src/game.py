# -*- coding: utf-8 -*-
from input import Input
from music import Music
from vector import Vector
from tab import Tab
from scores import Scores
from field import Field
from moving_unit import Units


class Game(Tab):
    """Tab class that represents logic of a game"""

    def __init__(self, wrapper):
        super(Game, self).__init__(wrapper)
        self.type_scores = {'s': 10, 'e': 50}
        self.field = Field('1_lvl.txt')
        self.units = Units(self)
        self.scores = Scores(position=Vector(10, self.field.get_size().to_abs().y + 5), level=1)

    def set_hs(self, hs):
        # type: (int) -> None
        """Set highscore and write it to file"""
        pass

    def start(self):
        Input.reset()
        self.field = Field(str(self.scores.level) + '_lvl.txt')
        self.units.add_pacman(self.field.get_pacman_spawn())
        self.units.add_ghosts(self.field.get_ghosts_spawn())
        Music.play('bg', .1)

    def pacman_die(self):
        if self.scores.lives >= 1:
            self.scores.lives -= 1
            if self.scores.lives:
                Music.play('go')
                self.units.reset()
                Input.reset()
            else:
                self.game_over()

    def add_score(self, value):
        # type: (int) -> int
        return self.scores.add_score(value)

    def next_level(self):
        # type: () -> None
        """Switch to next level"""
        self.scores.level += 1
        Input.reset()
        self.field = Field(str(self.scores.level) + '_lvl.txt')
        self.units.add_pacman(self.field.get_pacman_spawn())
        self.units.add_ghosts(self.field.get_ghosts_spawn())
        Music.play('bg', .1)

    def get_size(self):
        # type: () -> Vector
        """Return size vector of tab"""
        return Vector(self.field.get_size().to_abs().x, self.field.get_size().to_abs().y + self.scores.get_size().y)

    def update(self):
        # type: () -> None
        """Update the objects"""
        if self.field.seed_count <= 0:  # все зерна съедены
            self.next_level()
        else:
            if self.scores.score:
                if self.field.get_door_status() == 1:
                    self.field.get_cell(self.field.door).set_type('0')
                for g in (self.units.blinky, self.units.pinky, self.units.clyde):
                    if not g.get_mode():
                        g.set_mode(1)
                if not self.units.inky.get_mode() and self.scores >= 30 * self.type_scores.get('s'):
                    self.units.inky.set_mode(1)
            self.units.pacman.set_buffer_direction(Input.key_direction)
            self.units.move()

    def game_over(self):
        Music.stop('bg')
        Music.play('go')
        self.wrapper.set_current_tab('mainmenu')
        self.wrapper.add_tab('game', Game(self.wrapper))

    def draw(self):
        # type: () -> None
        """Draw all objects"""
        self.field.draw()
        self.units.draw()
        self.scores.draw()
