import sys
from glfw.GLFW import *
from OpenGL.GL import *

def startup():
    update_viewport(None, 400, 400)
    glClearColor(1.0, 1.0, 1.0, 1.0)


def shutdown():
    pass


# Zadanie 1
def render(time):
    glClear(GL_COLOR_BUFFER_BIT)

    # Drawing a first triangle
    glBegin(GL_TRIANGLES)

    # 1st vertex - red
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(0.0, 0.0)

    # 2nd vertex - green
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(0.0, 50.0)

    # 3rd vertex - blue
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(50.0, 0.0)

    glEnd()

    # Drawing a second triangle
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 1.0, 0.0)
    glVertex2f(0.0, 0.0)
    glColor3f(1.0, 0.0, 1.0)
    glVertex2f(0.0, 50.0)
    glColor3f(0.0, 1.0, 1.0)
    glVertex2f(-50.0, 0.0)
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
        render(glfwGetTime())
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()