import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def point(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def pointOctal(x, y, xc, yc):
    glBegin(GL_POINTS)
    glVertex2f(xc + x, yc + y)
    glVertex2f(xc - x, yc + y)
    glVertex2f(xc + x, yc - y)
    glVertex2f(xc - x, yc - y)
    glVertex2f(yc + y, xc + x)
    glVertex2f(yc - y, xc + x)
    glVertex2f(yc + y, xc - x)
    glVertex2f(yc - y, xc - x)
    glEnd()


def drawCircle(points, xc, yc):
    glBegin(GL_LINES)
    for i in range(0, len(points)-1):
        glVertex2f(xc + points[i][0], yc + points[i][1])
        glVertex2f(xc + points[i + 1][0], yc + points[i + 1][1])
        glVertex2f(xc - points[i][0], yc + points[i][1])
        glVertex2f(xc - points[i + 1][0], yc + points[i + 1][1])
        glVertex2f(xc + points[i][0], yc - points[i][1])
        glVertex2f(xc + points[i + 1][0], yc - points[i + 1][1])
        glVertex2f(xc - points[i][0], yc - points[i][1])
        glVertex2f(xc - points[i + 1][0], yc - points[i + 1][1])

        glVertex2f(yc + points[i][1], xc + points[i][0])
        glVertex2f(yc + points[i + 1][1], xc + points[i + 1][0])
        glVertex2f(yc - points[i][1], xc + points[i][0])
        glVertex2f(yc - points[i + 1][1], xc + points[i + 1][0])
        glVertex2f(yc + points[i][1], xc - points[i][0])
        glVertex2f(yc + points[i + 1][1], xc - points[i + 1][0])
        glVertex2f(yc - points[i][1], xc - points[i][0])
        glVertex2f(yc - points[i + 1][1], xc - points[i + 1][0])


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

    (xc, yc) = 50, 50
    r = 30

    x = 0
    y = 30
    d = 3 - 2 * r

    pointsArray = [(x, y)]

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

        if d < 0:
            x += 1
            y = y
            d = d + 4 * x + 6
        else:
            x += 1
            y -= 1
            d = d + 4 * (x - y) + 10
        if x <= y:
            pointOctal(x, y, xc, yc)
            pointsArray.append((x, y))
        else:
            print(pointsArray)
            drawCircle(pointsArray, xc, yc)

        point(xc, yc)
        pygame.display.flip()
        pygame.time.wait(100)


main()