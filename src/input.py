# -*- coding: utf-8 -*-
import pygame

from vector import (Vector, Direction)


class Input(object):
    exit = False

    # Keyboard variables
    key_dict = {pygame.K_UP: Direction.UP,
                pygame.K_w: Direction.UP,
                pygame.K_DOWN: Direction.DOWN,
                pygame.K_s: Direction.DOWN,
                pygame.K_LEFT: Direction.LEFT,
                pygame.K_a: Direction.LEFT,
                pygame.K_RIGHT: Direction.RIGHT,
                pygame.K_d: Direction.RIGHT}
    key_direction = Direction.ZERO

    # Mouse variables
    mouse_position = Vector()
    mouse_mode = 0

    # 0 - default
    # 1 - pressed
    # 2 - released

    @staticmethod
    def reset():
        Input.key_direction = Direction.ZERO
        Input.mouse_mode = 0
        Input.mouse_position = Vector()

    @staticmethod
    def update():
        Input.mouse_update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Input.exit = True
            elif event.type == pygame.MOUSEMOTION:
                Input.set_mouse_position(pygame.mouse.get_pos())
            elif event.type == pygame.MOUSEBUTTONDOWN:
                Input.on_mouse_down()
            elif event.type == pygame.MOUSEBUTTONUP:
                Input.on_mouse_up()
            elif event.type == pygame.KEYDOWN:
                if event.key in Input.key_dict:
                    Input.set_key_direction(Input.key_dict.get(event.key))

    @staticmethod
    def set_mouse_position(position):
        Input.mouse_position = Vector(position)

    @staticmethod
    def get_mouse_position():
        return Input.mouse_position

    @staticmethod
    def on_mouse_down():
        Input.mouse_mode = 1

    @staticmethod
    def on_mouse_up():
        Input.mouse_mode = 2

    @staticmethod
    def get_mouse_mode():
        return Input.mouse_mode

    @staticmethod
    def mouse_update():
        if Input.mouse_mode == 2:
            Input.mouse_mode = 0

    @staticmethod
    def set_key_direction(direction):
        Input.key_direction = direction

    @staticmethod
    def quit():
        Input.exit = True
