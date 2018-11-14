# -*- coding: utf-8 -*-
from input import Input
from drawable import MultiDrawable


class Button(MultiDrawable):
    def __init__(self, path_to_images, name, func, position=None):
        super(Button, self).__init__(image_paths=(
            path_to_images + name + '.gif',
            path_to_images + name + '_selected.gif',
            path_to_images + name + '_pressed.gif'), position=position)
        self.name = str(name)
        self.func = func
        self.mode = 0

    def set_mode(self, mode):
        # type: (int) -> None
        """mode:
        0: default
        1: selected
        2: pressed"""
        self.mode = int(mode)
        self.set_image(self.mode)

    def update(self):
        if (
                        self.position.x - self.get_size().x // 2 <= Input.get_mouse_position().x <= self.position.x + self.get_size().x // 2 and self.position.y - self.get_size().y // 2 <= Input.get_mouse_position().y <= self.position.y + self.get_size().y // 2):
            if Input.get_mouse_mode() == 1:
                self.set_mode(2)
            else:
                self.set_mode(1)
                if Input.get_mouse_mode() == 2:
                    self.func()
        else:
            self.set_mode(0)
