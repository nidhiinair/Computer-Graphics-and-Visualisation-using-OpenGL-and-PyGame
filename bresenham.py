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

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    if (x2 > x1):
        incrx = 1
    else:
        incrx = -1
    if (y2 > y1):
        incry = 1
    else:
        incry = -1

    x = x1
    y = y1
    i = 0

    if (dx > dy):
        e = 2 * dy - dx
        incr1 = 2 * (dy - dx)
        incr2 = 2 * dy

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

            if (i < dx):
                if (e >= 0):
                    y += incry
                    e += incr1
                else:
                    e += incr2
                x += incrx
                i += 1
            # else:
            #     point(x, y)
            #     e = 2 * dx - dy
            #     incr1 = 2 * (dx - dy)
            #     incr2 = 2 * dx
            #     while (i < dy):
            #         if (e >= 0):
            #             x += incrx
            #             e += incr1
            #         else:
            #             e += incr2
            #         y += incry
            #         point(x, y)
            #         line(x1, y1, x, y)
            #         i += 1

            line(x1, y1, x, y)
            point(x1, y1)
            point(x2, y2)
            pygame.display.flip()
            pygame.time.wait(50)
    else:
        e = 2 * dx - dy
        incr1 = 2 * (dx - dy)
        incr2 = 2 * dx

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

            if (i < dy):
                if (i < dy):
                    if (e >= 0):
                        x += incrx
                        e += incr1
                    else:
                        e += incr2
                    y += incry
                    point(x, y)
                    line(x1, y1, x, y)
                    i += 1
            line(x1, y1, x, y)
            point(x1, y1)
            point(x2, y2)
            pygame.display.flip()
            pygame.time.wait(50)



main()
