# -*- coding: utf-8 -*-
from button import Button
from tab import Tab
from vector import Vector


class MainMenu(Tab):
    button_size = Vector(300, 79)

    def __init__(self, wrapper):
        super(MainMenu, self).__init__(wrapper)
        self.objects_position = Vector(self.get_size().x // 2 - MainMenu.button_size.x // 2, 200)
        self.objects_spacing = Vector(0, 20)
        self.add_drawable(Button(path_to_images=self.path_to_images,
                                 name='play',
                                 func=lambda: self.wrapper.set_current_tab('game')))
        # self.add_drawable(Button(path_to_images=self.path_to_images,
        #                          name='shop',
        #                          func=lambda: self.wrapper.set_current_tab('shop')))
        # self.add_drawable(Button(path_to_images=self.path_to_images,
        #                          name='records',
        #                          func=lambda: self.wrapper.set_current_tab('records')))
        self.add_drawable(Button(path_to_images=self.path_to_images,
                                 name='exit',
                                 func=lambda: self.wrapper.quit()))

    def add_drawable(self, obj):
        obj.set_position(self.objects_position + Vector(0, sum(
            obj.get_size().y for obj in self.objects)) + self.objects_spacing * len(self.objects))
        super(MainMenu, self).add_drawable(obj)

    def draw(self):
        super(MainMenu, self).draw()
