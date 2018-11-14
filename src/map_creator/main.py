# -*- coding:utf8 -*-
from map_menu import Map
from input_menu import SizeInputForm


def start():
    size_menu = SizeInputForm()
    size_menu.show_start_window()

    map_menu = Map(size_menu.get_size())
    map_menu.show_start_window()

def main():
    start()

main()