import sys
from glfw.GLFW import *
from OpenGL.GL import *
import random

def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.0, 0.0, 0.0, 1.0)


def shutdown():
    pass


def renderRect(x, y, a, b):
    #glClear(GL_COLOR_BUFFER_BIT)

    # Drawing a first triangle - upper one
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 1.0, 0.0)
    glVertex2f(x, y)
    glVertex2f(x, y + b)
    glVertex2f(x + a, y)
    glEnd()

    # Drawing a second triangle - lower one
    glBegin(GL_TRIANGLES)
    glVertex2f(x, y + b)
    glVertex2f(x + a, y)
    glVertex2f(x + a, y + b)
    glEnd()

    #glFlush()

def renderCarpet(x, y, a, b, level):
    if level == 0:
        renderRect(x, y, a, b)
    else:
        level = level - 1
        width = a / 3.0
        height = b / 3.0

        for i in range(3):
            for j in range(3):
                if not (i == 1 and j == 1):
                    newY = y + i * height
                    newX = x + j * width
                    renderCarpet(newX, newY, width, height, level)

def update_viewport(window, width, height):
    if height == 0:
        height = 1
    if width == 0:
        width = 1
    aspectRatio = width / height

    glMatrixMode(GL_PROJECTION)
    glViewport(0, 0, width, height)
    glLoadIdentity()

    if width <= height:
        glOrtho(-100.0, 100.0, -100.0 / aspectRatio, 100.0 / aspectRatio,
                1.0, -1.0)
    else:
        glOrtho(-100.0 * aspectRatio, 100.0 * aspectRatio, -100.0, 100.0,
                1.0, -1.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():
    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(400, 400, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSwapInterval(1)

    startup()
    while not glfwWindowShouldClose(window):
        glClear(GL_COLOR_BUFFER_BIT)
        renderCarpet(-100, -50, 200, 100, 5)
        glFlush()
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()