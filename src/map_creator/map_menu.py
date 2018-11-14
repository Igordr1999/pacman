# -*- coding:utf8 -*-
import sys
import pygame
from datetime import datetime

background_color = (255, 255, 255)  # white
ELEMENT_SIZE = (24, 24)

path_to_map = "../../resrc/maps/new_maps/"

path_to_b = "../../resrc/field_images/walls/b.gif"
path_to_bl = "../../resrc/field_images/walls/bl.gif"
path_to_l = "../../resrc/field_images/walls/l.gif"
path_to_r = "../../resrc/field_images/walls/r.gif"
path_to_rb = "../../resrc/field_images/walls/rb.gif"
path_to_rbl = "../../resrc/field_images/walls/rbl.gif"
path_to_rl = "../../resrc/field_images/walls/rl.gif"
path_to_t = "../../resrc/field_images/walls/t.gif"
path_to_tb = "../../resrc/field_images/walls/tb.gif"
path_to_tbl = "../../resrc/field_images/walls/tbl.gif"
path_to_tl = "../../resrc/field_images/walls/tl.gif"
path_to_tr = "../../resrc/field_images/walls/tr.gif"
path_to_trb = "../../resrc/field_images/walls/trb.gif"
path_to_trbl = "../../resrc/field_images/walls/trbl.gif"
path_to_trl = "../../resrc/field_images/walls/trl.gif"
path_to_d = "../../resrc/field_images/d.gif"
path_to_e = "../../resrc/field_images/e.gif"

pygame.font.init()

walls = ['b', 't', 'l', 'r', 'bl', 'rb', 'tl', 'tr', 'trl', 'rbl', 'trb', 'tbl', 'tb', 'rl', 'trbl']


class Map:
    def __init__(self, cell_size):
        self.element_array = ['oo', 'b', 't', 'l', 'r', 'bl', 'rb', 'tl', 'tr', 'trl', \
                              'rbl', 'trb', 'tbl', 'tb', 'rl', 'trbl', 'd', 'e']
        self.element_array_size = len(self.element_array)
        self.set_data()
        self.width = cell_size[0] * ELEMENT_SIZE[0]
        self.height = cell_size[1] * ELEMENT_SIZE[1]
        self.cell_width = cell_size[0]
        self.cell_height = cell_size[1]

        self.screen_size = (self.width, self.height)
        self.screen = pygame.display.set_mode(self.screen_size)

        self.field = self.read_map()
        self.output()

    def show_start_window(self):
        self.first_loop()

    def read_map(self):
        t_map = []
        for j in range(self.height):
            t_map.append(['oo' for i in range(self.width)])
        return t_map

    def draw(self):
        # print self.cell_height, self.cell_width, '\n', self.field
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                self.screen.blit(self.image_cell, self.get_rect(i, j))

                if self.field[i][j] == 'b':
                    self.screen.blit(self.image_b, self.get_rect(i, j))
                elif self.field[i][j] == 't':
                    self.screen.blit(self.image_t, self.get_rect(i, j))
                elif self.field[i][j] == 'l':
                    self.screen.blit(self.image_l, self.get_rect(i, j))
                elif self.field[i][j] == 'r':
                    self.screen.blit(self.image_r, self.get_rect(i, j))
                elif self.field[i][j] == 'bl':
                    self.screen.blit(self.image_bl, self.get_rect(i, j))
                elif self.field[i][j] == 'rb':
                    self.screen.blit(self.image_rb, self.get_rect(i, j))
                elif self.field[i][j] == 'tl':
                    self.screen.blit(self.image_tl, self.get_rect(i, j))
                elif self.field[i][j] == 'tr':
                    self.screen.blit(self.image_tr, self.get_rect(i, j))
                elif self.field[i][j] == 'trl':
                    self.screen.blit(self.image_trl, self.get_rect(i, j))
                elif self.field[i][j] == 'rbl':
                    self.screen.blit(self.image_rbl, self.get_rect(i, j))
                elif self.field[i][j] == 'trb':
                    self.screen.blit(self.image_trb, self.get_rect(i, j))
                elif self.field[i][j] == 'tbl':
                    self.screen.blit(self.image_tbl, self.get_rect(i, j))
                elif self.field[i][j] == 'tb':
                    self.screen.blit(self.image_tb, self.get_rect(i, j))
                elif self.field[i][j] == 'rl':
                    self.screen.blit(self.image_rl, self.get_rect(i, j))
                elif self.field[i][j] == 'trbl':
                    self.screen.blit(self.image_trbl, self.get_rect(i, j))
                elif self.field[i][j] == 'd':
                    self.screen.blit(self.image_door, self.get_rect(i, j))
                elif self.field[i][j] == 'e':
                    self.screen.blit(self.image_energizer, self.get_rect(i, j))
                elif self.field[i][j] == 'oo':
                    self.screen.blit(self.seed_image, self.get_rect(i, j))

    def output(self):
        self.screen.fill(background_color)
        self.draw()
        pygame.display.update()

    def get_rect(self, i, j):
        return pygame.Rect((j * ELEMENT_SIZE[0], i * ELEMENT_SIZE[1]), ELEMENT_SIZE)

    # def get_seed_rect(self, i, j):
    #     return pygame.Rect(((j + 0) * ELEMENT_SIZE[0], (i + 0) * ELEMENT_SIZE[1]), ELEMENT_SIZE)

    def set_data(self):
        self.image_cell = pygame.image.load('../../resrc/field_images/g.gif')
        self.image_b = pygame.image.load(path_to_b)
        self.image_t = pygame.image.load(path_to_t)
        self.image_l = pygame.image.load(path_to_l)
        self.image_r = pygame.image.load(path_to_r)
        self.image_bl = pygame.image.load(path_to_bl)
        self.image_rb = pygame.image.load(path_to_rb)
        self.image_tl = pygame.image.load(path_to_tl)
        self.image_tr = pygame.image.load(path_to_tr)
        self.image_trl = pygame.image.load(path_to_trl)
        self.image_rbl = pygame.image.load(path_to_rbl)
        self.image_trb = pygame.image.load(path_to_trb)
        self.image_tbl = pygame.image.load(path_to_tbl)
        self.image_tb = pygame.image.load(path_to_tb)
        self.image_rl = pygame.image.load(path_to_rl)
        self.image_trbl = pygame.image.load(path_to_trbl)

        self.image_door = pygame.image.load(path_to_d)
        self.image_energizer = pygame.image.load(path_to_e)
        self.seed_image = pygame.image.load('../../resrc/field_images/s.gif')
        self.image_active_cell = pygame.image.load('../../resrc/field_images/active.gif')

    def get_cell(self, position):  # Метод получения кооринат клетки по координатам точки
        h_coordinate = int(position[1]) // ELEMENT_SIZE[1]
        w_coordinate = int(position[0]) // ELEMENT_SIZE[0]
        return [h_coordinate, w_coordinate]

    def first_loop(self):

        exit = False
        cell = [0] * 2
        while not exit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        if cell[1] + 1 < self.height: cell[1] += 1; exit = self.second_loop(cell)
                    elif event.key == pygame.K_LEFT:
                        if cell[1] - 1 >= 0: cell[1] -= 1; exit = self.second_loop(cell)
                    elif event.key == pygame.K_UP:
                        if cell[0] + 1 < self.width: cell[0] -= 1; exit = self.second_loop(cell)
                    elif event.key == pygame.K_DOWN:
                        if cell[0] - 1 >= 0: cell[0] += 1; exit = self.second_loop(cell)


                elif event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    cell = self.get_cell(position)
                    exit = self.second_loop(cell)

        self.save_new_map()

    def second_loop(self, cell):
        self.screen.fill(background_color)
        self.draw()
        self.screen.blit(self.image_active_cell, self.get_rect(cell[0], cell[1]))
        pygame.display.update()

        current_index = 1
        cell_ready = False
        exit = False

        while not exit and not cell_ready:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_UP:
                        current_index = (current_index + 1) % self.element_array_size
                        self.field[int(cell[0])][int(cell[1])] = self.element_array[current_index]
                        self.screen.fill(background_color)
                        self.draw()
                        pygame.display.update()

                    elif event.key == pygame.K_LEFT or event.key == pygame.K_DOWN:
                        current_index = (current_index - 1 + self.element_array_size) \
                                        % self.element_array_size
                        self.field[int(cell[0])][int(cell[1])] = self.element_array[current_index]
                        self.screen.fill(background_color)
                        self.draw()
                        pygame.display.update()

                    elif event.key == pygame.K_BACKSPACE:
                        current_index = 0
                        self.field[cell[0]][cell[1]] = '00'
                        self.screen.fill(background_color)
                        self.draw()
                        pygame.display.update()
                        cell_ready = True
                        break

                    elif event.key == pygame.K_RETURN:
                        cell_ready = True
                        break

                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    cell = self.get_cell(position)
                    self.screen.fill(background_color)
                    self.draw()
                    self.screen.blit(self.image_active_cell, self.get_rect(cell[0], cell[1]))
                    pygame.display.update()
                    current_index = 0
        return exit

    def save_new_map(self):
        date = self.get_time_string()
        new_map = open(path_to_map + 'map' + date + '.txt', 'w')
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                if self.field[i][j] in walls:
                    new_map.write('w')
                elif self.field[i][j] == '00':
                    new_map.write('0')
                elif self.field[i][j] == 'oo':
                    new_map.write('s')
                elif self.field[i][j] == 'd':
                    new_map.write('d')
                elif self.field[i][j] == 'e':
                    new_map.write('e')
            new_map.write('\n')
        new_map.close()

    def get_time_string(self):
        now = datetime.now()
        return datetime.strftime(datetime.now(), "%H:%M:%S")