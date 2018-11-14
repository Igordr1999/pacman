# -*- coding: utf-8 -*-
from drawable import Drawable
from vector import Vector


class Cell(Drawable):
    """Class that represents a cell on the field"""
    path_to_images = '../resrc/field_images/'

    def __init__(self, type='0', position=Vector()):
        self.type = str(type)
        if self.type in ['p', 'g', 't']:
            path = '0.gif'
        else:
            path = self.type + '.gif'
        super(Cell, self).__init__(position=position, image_path=Cell.path_to_images + path)

    def get_type(self):
        # type: () -> str
        """Return cell type"""
        return self.type

    def set_type(self, type):
        # type: (str) -> None
        """"Set cell type"""
        self.type = str(type)
        path = Cell.path_to_images
        if self.type in ['p', 'g', 't']:
            path = '0.gif'
        else:
            path += self.type + '.gif'
        self.set_image(path)

    def is_passable(self):
        # type: () -> bool
        """"Return if cell is passable"""
        return self.type not in ['w', 'd']
