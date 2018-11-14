# -*- coding: utf-8 -*-
import pygame

from painter import Painter
from input import Input
from menu import MainMenu
from game import Game


class PygameWrapper(object):
    """Wrapper class for pygame"""

    def __init__(self):
        pygame.init()
        self.exit = False
        self.framerate = 60
        self.clock = None
        self.delta_time = 0
        self.tabs = {}
        self.add_tab('game', Game(self))
        self.add_tab('mainmenu', MainMenu(self))
        self.current_tab = self.get_tab('mainmenu')
        self.current_tab.start()
        self.screen = pygame.display.set_mode(self.current_tab.get_size().floor().get())
        Painter.init(self.screen)

    def update_delta_time(self):
        self.delta_time = self.clock.tick(self.framerate) / 1000.0

    def get_delta_time(self):
        return self.delta_time

    def start(self):
        """start main loop"""
        self.clock = pygame.time.Clock()
        while not Input.exit:
            Painter.fill_screen()
            self.update_delta_time()
            Input.update()

            self.current_tab.update()
            self.current_tab.draw()

            pygame.display.update()

    def add_tab(self, tab_name, tab_obj):
        self.tabs[tab_name] = tab_obj

    def get_tab(self, tab_name):
        return self.tabs.get(tab_name)

    def set_current_tab(self, tab_name):
        self.current_tab = self.tabs.get(tab_name)
        self.current_tab.start()
        self.screen = pygame.display.set_mode(self.current_tab.get_size().floor().get())
        Painter.init(self.screen)

    def get_current_tab(self):
        return self.current_tab

    def quit(self):
        Input.exit = True
