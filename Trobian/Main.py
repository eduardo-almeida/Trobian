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
quit_game = False
while not quit_game:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit_game = True
        elif event.type == pg.MOUSEMOTION:
            #start_screen.motion(e.pos)
            e = 0
        elif event.type == pg.MOUSEBUTTONUP:
            if event.button == 1 or event.button == 3:
                #quit_game = start_screen.click(e.button, e.pos)
                Mouse_x1, Mouse_y1 = pg.mouse.get_pos()
                print(pg.mouse.get_pos())
                dx = Mouse_x2 - Mouse_x1
                dy = Mouse_y2 - Mouse_y1
                rads = atan2(-dy, dx)
                rads %= 2 * pi
                degs = degrees(rads)
                degs += 180
                print (degs)
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 or event.button == 3:
                Mouse_x2, Mouse_y2 = pg.mouse.get_pos()
                print(pg.mouse.get_pos())
                #start_screen.button_down(e.button, e.pos)
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                quit_game = True