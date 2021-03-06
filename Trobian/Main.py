import pygame as pg
from pygame.locals import *
from src.constants import *
import src.fonts as fonts
from math import atan2, degrees, pi


def show_fps(win, inner_clock, font):
    fps_text = font.render("FPS: " + str(round(inner_clock.get_fps())), True, (255, 255, 0))
    win.blit(fps_text, (2, 2))

print ("Ola 2")

pg.init()

# Load fonts
fonts.init_fonts()

# Window parameters
pg.display.set_caption("Trobian")

screen = pg.display.set_mode((400, 400))#,pg.FULLSCREEN, pg.RESIZABLE)
tela = pg.display.get_surface()
quit_game = False
pontos = [(40, 40) ]
pos = (0,0)
while not quit_game:

    tela.fill(BLUE)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit_game = True
        elif event.type == pg.MOUSEMOTION:
            e = 0
            pos = pg.mouse.get_pos()
        elif event.type == pg.MOUSEBUTTONUP:
            if event.button == 1 or event.button == 3:
                x =0
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 or event.button == 3:
                x = 0
                #pontos.append(pg.mouse.get_pos())
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                quit_game = True

    '''for i in pontos:
        move_x = pos[0] - i[0]
        move_y = pos[1] - i[1]
        x = int(i[0] + move_x * 0.1)  # Scale the vector to the desired length.
        y = i[1] + move_y * 0.1
        local = (x, y)
        pg.draw.circle(screen, GREEN, (x, y), 5)'''
    heading = pg.mouse.get_pos() - pos
    pos += heading * 0.1
    pg.display.flip()