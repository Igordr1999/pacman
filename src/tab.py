# -*- coding:utf8 -*-
from vector import Vector
from drawable import Drawable


class Tab(object):
    path_to_tabs = '../resrc/tabs/'

    def __init__(self, wrapper, background_image_path=None):
        self.path_to_images = Tab.path_to_tabs + (
            self.__class__.__name__.lower() if self.__class__ != Tab else '') + '/'
        if background_image_path is None:
            background_image_path = self.path_to_images + 'background.gif'
        self.wrapper = wrapper
        self.background = Drawable(background_image_path)
        self.objects = []

    def add_drawable(self, obj):
        # type: (Drawable) -> None
        obj.set_position(obj.position + obj.get_size() // 2)
        self.objects.append(obj)

    def start(self):
        pass

    def get_size(self):
        # type: () -> Vector
        return self.background.get_size()

    def update(self):
        for obj in self.objects:
            obj.update()

    def draw(self):
        self.background.draw()
        for obj in self.objects:
            obj.draw()
