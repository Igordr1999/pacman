# -*- coding:utf8 -*-
import pygame

class SizeInputForm:
    def __init__(self):
        self.window_size = (640, 480)
        self.screen = pygame.display.set_mode(self.window_size)

        self.input_width = []
        self.input_height = []

        self.first_form_is_active = True
        self.enter_pressed = False
        self.exit = False

        self.width = 0
        self.height = 0

        #self.show_start_window()

    def get_size(self):
        return self.width, self.height

    def display(self, message_1, message_2):
        head_font = pygame.font.Font(None, 35)
        font = pygame.font.Font(None, 25)

        background = (185, 198, 208)  # b9c6d0 # 185,198,208
        form = background
        frame = (0, 0, 0)
        text_color = (0, 0, 0)

        left_indent = self.screen.get_width() * 0.2
        width = self.screen.get_width() * 0.6
        fr_left_indent = self.screen.get_width() * 0.18
        fr_width = self.screen.get_width() * 0.64
        height = self.screen.get_height() * 0.1
        fr_height = self.screen.get_height() * 0.12
        top_indent_1 = self.screen.get_height() * 0.4
        fr_top_indent_1 = self.screen.get_height() * 0.38
        top_indent_2 = self.screen.get_height() * 0.6
        fr_top_indent_2 = self.screen.get_height() * 0.58

        header = "Enter map's width and height"
        head_left_indent = self.screen.get_width() * 0.2
        top_indent_head = self.screen.get_height() * 0.2

        self.screen.fill(background)

        pygame.draw.rect(self.screen, form, (left_indent, top_indent_1, width, height), 0)
        pygame.draw.rect(self.screen, frame, (fr_left_indent, fr_top_indent_1, fr_width, fr_height), 1)
        pygame.draw.rect(self.screen, form, (left_indent, top_indent_2, width, height), 0)
        pygame.draw.rect(self.screen, frame, (fr_left_indent, fr_top_indent_2, fr_width, fr_height), 1)

        self.screen.blit(head_font.render(header, 1, text_color), (head_left_indent, top_indent_head))
        self.screen.blit(font.render(message_1, 1, text_color), (left_indent, top_indent_1))
        self.screen.blit(font.render(message_2, 1, text_color), (left_indent, top_indent_2))

        pygame.display.flip()


    def show_start_window(self):
        string = ''
        self.display("Width: " + string.join(self.input_width), "Height: " + string.join(self.input_height))

        while not self.exit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit = True
                elif event.type == pygame.KEYDOWN:
                    self.handle_keydown(event.key)
                    self.display("Width: " + string.join(self.input_width), "Height: " + string.join(self.input_height))

        self.width, self.height = int(string.join(self.input_width)), int(string.join(self.input_height))

    def handle_keydown(self, key):
        if key == pygame.K_BACKSPACE:
            if self.first_form_is_active: self.input_width = self.input_width[0:-1]
            else: self.input_height = self.input_height[0:-1]
        elif key == pygame.K_RETURN:
            if self.enter_pressed == False:
                self.first_form_is_active = False
                self.enter_pressed = True
            else:
                self.exit = True
        elif 48 <= key <= 57:
            if self.first_form_is_active:
                self.input_width.append(chr(key))
            else:
                self.input_height.append(chr(key))