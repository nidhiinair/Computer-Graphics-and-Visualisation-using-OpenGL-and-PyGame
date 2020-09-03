import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def point(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def line(x1, y1, x2, y2):
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()


def main():
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 100, 0.0, 100, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    # glTranslatef(0, 0, -5)

    (x1, y1) = 70, 80
    (x2, y2) = 10, 10
    if (abs(x2 - x1) >= abs(y2 - y1)):
        length = abs(x2 - x1)
    else:
        length = abs(y2 - y1)

    xincr = (x2 - x1) / length
    yincr = (y2 - y1) / length

    x = x1 + 0.5
    y = y1 + 0.5
    i = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        if i <= length:
            point(x, y)
            x = x + xincr
            y = y + yincr
            i = i + 1
        line(x1, y1, x, y)
        point(x1, y1)
        point(x2, y2)
        pygame.display.flip()
        pygame.time.wait(50)


main()
