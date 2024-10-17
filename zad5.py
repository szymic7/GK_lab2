import sys
from glfw.GLFW import *
from OpenGL.GL import *
import random

def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glPointSize(2.0)

def shutdown():
    pass

# Global variables to store random RGB color
red = 0.0
green = 0.0
blue = 0.0

# Method to generate random RGB color
def randomColor():
    global red, green, blue
    red = random.random()
    green = random.random()
    blue = random.random()

def renderSierpinskiTriangle(x1, y1, x2, y2, x3, y3, level):
    if level == 0:
        glBegin(GL_TRIANGLES)
        glColor3f(red, green, blue)
        glVertex2f(x1, y1)
        glVertex2f(x2, y2)
        glVertex2f(x3, y3)
        glEnd()
    else:
        level -= 1

        midX12 = (x1 + x2) / 2
        midY12 = (y1 + y2) / 2
        midX23 = (x2 + x3) / 2
        midY23 = (y2 + y3) / 2
        midX13 = (x1 + x3) / 2
        midY13 = (y1 + y3) / 2

        renderSierpinskiTriangle(x1, y1, midX12, midY12, midX13, midY13, level)
        renderSierpinskiTriangle(midX12, midY12, x2, y2, midX23, midY23, level)
        renderSierpinskiTriangle(midX13, midY13, midX23, midY23, x3, y3, level)


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
    randomColor()
    while not glfwWindowShouldClose(window):
        glClear(GL_COLOR_BUFFER_BIT)
        renderSierpinskiTriangle(-100, -100, 100, -100, 0, 100, 7)
        glFlush()
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()