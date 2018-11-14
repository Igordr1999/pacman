# -*- coding: utf-8 -*-
import random

from vector import (Vector, Direction)
from music import Music
from drawable import MultiDrawable


class MovingUnit(MultiDrawable):
    default_speed = 6

    def __init__(self, game, spawn_cell=None):
        if spawn_cell is None:
            spawn_cell = Vector()
        imgs_dir_path = '../resrc/moving_units/' + self.__class__.__name__.lower() + '/'
        images = (imgs_dir_path + 'up.gif',
                  imgs_dir_path + 'left.gif',
                  imgs_dir_path + 'down.gif',
                  imgs_dir_path + 'right.gif')
        self.dir_indexes = {Direction.UP: 0,
                            Direction.LEFT: 1,
                            Direction.DOWN: 2,
                            Direction.RIGHT: 3,
                            Direction.ZERO: 3}
        super(MovingUnit, self).__init__(image_paths=images,
                                         position=spawn_cell.to_abs().cell_center())
        self.game = game
        self.spawn_cell = spawn_cell

        self.speed = 0
        self.direction = Direction.ZERO
        self.buffer_direction = self.direction
        self.buffer_position = self.position
        self.reset()

    def reset(self):
        # type: () -> None
        self.set_speed(self.__class__.default_speed)
        self.set_direction(Direction.ZERO)
        self.set_position(self.spawn_cell.to_abs().cell_center())
        self.buffer_direction = self.direction
        self.buffer_position = self.position

    def set_position(self, position):
        # type: (Vector) -> None
        super(MovingUnit, self).set_position(position % self.game.field.get_size().to_abs())

    def set_direction(self, vector):
        # type: (Vector) -> None
        self.direction = vector
        self.buffer_position = self.get_position()
        self.set_image(self.dir_indexes.get(self.direction, 3))

    def get_direction(self):
        # type: () -> Vector
        """Return direction of unit"""
        return self.direction

    def set_buffer_direction(self, buffer_direction):
        # type: (Vector) -> None
        """Set direction of unit"""
        if buffer_direction != self.buffer_direction:
            self.buffer_direction = buffer_direction
            self.buffer_position = self.get_position()

    def set_speed(self, speed):
        # type: (int) -> None
        """Set speed of unit"""
        self.speed = speed

    def get_speed(self):
        # type: () -> int
        """Return speed of unit"""
        return self.speed

    def set_spawn_cell(self, vector):
        # type: (Vector) -> None
        self.spawn_cell = vector
        super(MovingUnit, self).set_position(self.spawn_cell.to_abs().cell_center())

    def move(self):
        # type: () -> None
        """Move unit towards its direction or changing direction"""
        # buffer direction handle
        if self.buffer_direction != self.direction and self.game.field.get_cell(
                        self.get_position().to_rel() + self.buffer_direction).is_passable():  # если направление, куда мы бы хотели пойти, отличается от текущего и туда можно повернуть
            if self.buffer_direction in (-self.get_direction(),
                                         Direction.ZERO) or not self.get_direction():  # если хотим сменить нарпавление на обратное или остановиться, то делаем это сразу
                self.set_direction(self.buffer_direction)
            elif (self.get_direction() in [Direction.DOWN,
                                           Direction.RIGHT] and self.buffer_position <= self.get_position().cell_center() <= self.get_position()) or (
                            self.get_direction() in [Direction.UP,
                                                     Direction.LEFT] and self.get_position() <= self.get_position().cell_center() <= self.buffer_position):  # если хотим повернуть, и мы зохотели это сделать не позже, чем прошли место поворота
                self.set_direction(self.buffer_direction)
                self.set_position(
                    self.get_position().cell_center())  # при повороте перемещаемся на центр текущей клетки
        # direction handle
        if self.get_direction():
            next_pos = self.get_position() + self.get_direction().to_abs() * self.get_speed() * self.game.wrapper.get_delta_time()  # позиция, которую хотим принять по ходу направления
            if self.game.field.get_cell(
                            self.get_position().to_rel() + self.direction).is_passable():  # если следующая клетка доступна для прохода
                self.set_position(next_pos)
            else:  # если следующая клетка недоступна для прохода
                if self.get_direction() in [Direction.UP, Direction.LEFT]:
                    self.set_position(max(self.get_position().cell_center(), next_pos))
                if self.get_direction() in [Direction.DOWN, Direction.RIGHT]:
                    self.set_position(min(self.get_position().cell_center(), next_pos))


class Pacman(MovingUnit):
    def move(self):
        # type: () -> None
        cur_cell = self.game.field.get_cell(self.get_position().to_rel())
        if cur_cell.get_type() in self.game.type_scores:  # кушаем
            self.game.add_score(
                self.game.type_scores.get(cur_cell.get_type(), 0))  # добавляем соответствующее количество очков
            cur_cell.set_type('0')
            self.game.field.seed_count -= 1
            if cur_cell.get_type == 'e':  # если съели енерджайзер, то приведения переходят в режим разберания
                self.game.units.fear()
                Music.play('en')
            if cur_cell.get_type == 's':
                Music.play('se')
        super(Pacman, self).move()


class Ghost(MovingUnit):
    def __init__(self, game, spawn_cell=None):
        if spawn_cell is None:
            spawn_cell = Vector()
        super(Ghost, self).__init__(game=game, spawn_cell=spawn_cell)
        self.destination = Vector()
        self.mode = 0

    def reset(self):
        super(Ghost, self).reset()
        self.mode = 0

    def start(self):
        self.set_random_direction()

    def set_destination(self, destination_rel):
        # type: (Vector) -> None
        """Set destination of ghost"""
        self.destination = destination_rel

    def get_destination(self):
        # type: () -> Vector
        """Return destination of ghost"""
        return self.destination

    def set_spawn_cell(self, vector):
        # type: (Vector) -> None
        super(Ghost, self).set_spawn_cell(vector)

    def set_random_direction(self):
        # type: () -> None
        dirs = self.game.field.get_cell_directions(self.get_position().to_rel())
        if dirs:
            self.set_direction(dirs[random.randint(0, len(dirs) - 1)])
            self.set_buffer_direction(self.get_direction())
        else:
            self.set_buffer_direction(Direction.ZERO)

    def set_mode(self, mode):
        # type: (int) -> None
        """Set mode of ghost
        0: wait
        1: chase
        2: scatter
        3: frightened"""
        self.mode = int(mode)
        if self.mode == 1:
            self.set_random_direction()
        elif self.mode == 2:
            self.set_direction(-self.get_direction())
            # self.set_buffer_direction(-self.get_direction())

    def get_mode(self):
        # type: () -> int
        return self.mode

    def die(self):
        self.game.add_score(50)
        self.reset()

    def move(self):
        # type: () -> None
        if self.get_mode():
            if self.get_direction():
                dirs = self.game.field.get_cell_directions(
                    self.get_position().to_rel())  # получаем все возможные направления для данной клетки
                if dirs:  # если есть, куда идти
                    if -self.get_direction() in dirs:  # не идем обратно
                        dirs.remove(-self.get_direction())
                    if len(dirs) == 0:  # тупик
                        self.set_buffer_direction(-self.get_direction())
                    elif len(dirs) == 1:  # у клетки было два направления => идем не туда, откуда пришли
                        self.set_buffer_direction(dirs[0])
                    elif len(dirs) > 1:  # более одного направления, не считая того, откуда пришли
                        min_dir_dist = self.get_destination() - (self.get_position().to_rel() + dirs[0])
                        self.set_buffer_direction(dirs[0])  # пусть первое направление - самое лучшее, дальше посмотрим
                        for i in range(1, len(dirs)):
                            cur_dir_dist = self.get_destination() - (self.get_position().to_rel() + dirs[i])
                            if cur_dir_dist < min_dir_dist:  # если это направление лучше, то ставим его
                                min_dir_dist = cur_dir_dist
                                self.set_buffer_direction(dirs[i])
                else:  # если идти некуда(
                    self.set_direction(Direction.ZERO)
            super(Ghost, self).move()
        if self.get_position().to_rel() == self.game.units.pacman.get_position().to_rel():  # если в одной клетке с пакманом
            if self.get_mode():  # если в нормальном режиме
                self.game.pacman_die()
            else:  # если в режиме разбегания
                self.die()


class Blinky(Ghost):
    def move(self):
        # type: () -> None
        if self.get_mode() == 1:
            self.set_destination(self.game.units.pacman.get_position().to_rel())
        else:
            self.set_destination(Vector())
        super(Blinky, self).move()


class Pinky(Ghost):
    def move(self):
        # type: () -> None
        if self.get_mode() == 1:
            self.set_destination(
                self.game.units.pacman.get_position().to_rel() + self.game.units.pacman.get_direction() * 4)
        else:
            self.set_destination(Vector())
        super(Pinky, self).move()


class Inky(Ghost):
    def move(self):
        # type: () -> None
        if self.get_mode() == 1:
            self.set_destination(
                self.game.units.blinky.get_destination() * 2 - self.game.units.blinky.get_position().to_rel())
        else:
            self.set_destination(Vector())
        super(Inky, self).move()


class Clyde(Ghost):
    def get_distance_to_pacman(self):
        # type: () -> float
        return (self.position.to_rel() - self.game.units.pacman.get_position().to_rel()).get_length()

    def move(self):
        # type: () -> None
        if self.get_mode() == 1:
            if self.get_distance_to_pacman() >= 9:
                self.set_destination(self.game.units.pacman.get_position().to_rel())
        else:
            self.set_destination(Vector())
        super(Clyde, self).move()


class Units(object):
    """Represents all units in game"""

    def __init__(self, game):
        self.game = game
        self.pacman = None
        self.blinky = None
        self.pinky = None
        self.inky = None
        self.clyde = None

    def add_pacman(self, spawn_cell):
        # type: (Vector) -> None
        """Set Pacman from spawn cell"""
        self.pacman = Pacman(self.game, spawn_cell)

    def add_ghosts(self, spawn_cell):
        # type: (Vector) -> None
        self.blinky = Blinky(self.game, spawn_cell)
        self.pinky = Pinky(self.game, spawn_cell)
        self.inky = Inky(self.game, spawn_cell)
        self.clyde = Clyde(self.game, spawn_cell)

    def add_blinky(self, spawn_cell):
        # type: (Vector) -> None
        """Set Blinky from spawn cell"""
        self.blinky = Blinky(self.game, spawn_cell)

    def add_pinky(self, spawn_cell):
        # type: (Vector) -> None
        """Set Pinky from spawn cell"""
        self.pinky = Pinky(self.game, spawn_cell)

    def add_inky(self, spawn_cell):
        # type: (Vector) -> None
        """Set Inky from spawn cell"""
        self.inky = Inky(self.game, spawn_cell)

    def add_clyde(self, spawn_cell):
        # type: (Vector) -> None
        """Set Clyde from spawn cell"""
        self.clyde = Clyde(self.game, spawn_cell)

    def get_all(self):
        # type: () -> tuple
        """Return tuple of all units"""
        res = []
        for u in (self.pacman, self.blinky, self.pinky, self.inky, self.clyde):
            if u:
                res.append(u)
        return tuple(res)

    def move(self):
        # type: () -> None
        for u in self.get_all():
            u.move()

    def draw(self):
        # type: () -> None
        for u in self.get_all():
            u.draw()

    def fear(self):
        # type: () -> None
        for g in (self.blinky, self.pinky, self.inky, self.clyde):
            g.set_mode(2)
            # timer

    def reset(self):
        # type: () -> None
        for u in self.get_all():
            u.reset()
