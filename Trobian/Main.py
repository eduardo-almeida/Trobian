import pygame as pg


def show_fps(win, inner_clock, font):
    fps_text = font.render("FPS: " + str(round(inner_clock.get_fps())), True, (255, 255, 0))
    win.blit(fps_text, (2, 2))

print ("Ola 2")

pg.init()

# Window parameters
pg.display.set_caption("Trobian")
screen = pg.display.set_mode((800, 800))
quit_game = False
while not quit_game:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            quit_game = True
        elif e.type == pg.MOUSEMOTION:
            #start_screen.motion(e.pos)
            print("OK")
        elif e.type == pg.MOUSEBUTTONUP:
            if e.button == 1 or e.button == 3:
                #quit_game = start_screen.click(e.button, e.pos)
                print("OK")
        elif e.type == pg.MOUSEBUTTONDOWN:
            if e.button == 1 or e.button == 3:
                print("OK")
                #start_screen.button_down(e.button, e.pos)