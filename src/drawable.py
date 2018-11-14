# -*- coding: utf-8 -*-
from vector import Vector
from image import GIFImage


class Drawable(object):
    """Represents object that can be drawn by Painter class"""
    images_cache = {}

    def __init__(self, image_path, position=None):
        """
        :type position: Vector
        :type image_path: str
        """
        self.image = GIFImage(image_path)
        if position is None:
            position = self.get_size()//2
        self.position = position

    def set_position(self, position):
        # type: (Vector) -> None
        """Set position vector"""
        self.position = position.floor()

    def get_position(self):
        # type: () -> Vector
        """Return position vector"""
        return self.position

    def set_image(self, image_path):
        # type: (str) -> GIFImage
        """Set image path"""
        if image_path not in self.images_cache:
            Drawable.images_cache[image_path] = GIFImage(image_path)
        self.image = Drawable.images_cache[image_path]
        return self.image

    def get_image(self):
        # type: () -> GIFImage
        """Return image"""
        return self.image

    def get_size(self):
        # type: () -> Vector
        """Return size vector of image"""
        return Vector(self.image.get_size())

    def get_image_rect(self):
        # type: () -> (GIFImage, Vector)
        """Return image and tuple of x and y positions"""
        return self.image, self.position

    def draw(self):
        # type: () -> None
        self.image.render(self.position)


class MultiDrawable(Drawable):
    def __init__(self, image_paths, position=None):
        self.images = image_paths
        super(MultiDrawable, self).__init__(self.images[0], position)

    def set_image(self, image_index):
        # type: (int) -> None
        self.image = GIFImage(self.images[image_index])
