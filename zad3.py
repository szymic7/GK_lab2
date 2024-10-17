import sys
import random
from glfw.GLFW import *
from OpenGL.GL import *

def startup():
    update_viewport(None, 400, 400)
    glClearColor(1.0, 1.0, 1.0, 1.0)

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
    #print("Red: ", red, "\nGreen: ", green, "\nBlue: ", blue)


# Zadanie 3
def renderDeformedRect(x, y, a, b, d = 0.0):
    glClear(GL_COLOR_BUFFER_BIT)

    # Drawing a first triangle - upper one
    glBegin(GL_TRIANGLES)
    glColor3f(red, green, blue)
    glVertex2f(x, y)
    glVertex2f(x, y+b*(1+d))
    glVertex2f(x+a*(1+d), y)
    glEnd()

    # Drawing a second triangle - lower one
    glBegin(GL_TRIANGLES)
    glVertex2f(x, y+b*(1+d))
    glVertex2f(x+a*(1+d), y)
    glVertex2f(x+a*(1+d), y+b*(1+d))
    glEnd()

    glFlush()


def update_viewport(window, width, height):
    if width == 0:
        width = 1
    if height == 0:
        height = 1
    aspect_ratio = width / height

    glMatrixMode(GL_PROJECTION)
    glViewport(0, 0, width, height)
    glLoadIdentity()

    if width <= height:
        glOrtho(-100.0, 100.0, -100.0 / aspect_ratio, 100.0 / aspect_ratio,
                1.0, -1.0)
    else:
        glOrtho(-100.0 * aspect_ratio, 100.0 * aspect_ratio, -100.0, 100.0,
                1.0, -1.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():
    randomColor()

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
        renderDeformedRect(-50, -50, 100, 50, -0.2)
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()