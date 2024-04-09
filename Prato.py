import math
from PIL import Image

import glfw
from OpenGL.GL import *
from OpenGL.raw.GLU import gluOrtho2D

def save_image(filename, width, height):
    glPixelStorei(GL_PACK_ALIGNMENT, 1)
    data = glReadPixels(0, 0, width, height, GL_RGB, GL_UNSIGNED_BYTE)
    image = Image.frombytes("RGB", (width, height), data)
    image = image.transpose(Image.FLIP_TOP_BOTTOM)  # Inverter a imagem para o formato PIL
    image.save(filename)
# Função de desenho OpenGL
def draw_circle(radius, center_x, center_y):
    glBegin(GL_LINE_LOOP)
    for i in range(360):
        angle = math.radians(i)
        x = radius * math.cos(angle) + center_x
        y = radius * math.sin(angle) + center_y
        glVertex2f(x, y)
    glEnd()

def main():
    if not glfw.init():
        raise Exception("glfw can not be initialized")

    width, height = 1280, 720
    window = glfw.create_window(width, height, "Prato", None, None)

    if not window:
        glfw.terminate()
        raise Exception("glfw window can not be created")

    glfw.set_window_pos(window, 400, 200)

    glfw.make_context_current(window)

    glClearColor(0, 0.1, 0.1, 1)
    glOrtho(0, width, 0, height, -1, 1)
    while not glfw.window_should_close(window):
        glfw.poll_events()

        glClear(GL_COLOR_BUFFER_BIT)

        glfw.poll_events()

        draw_circle(100, 640, 360)
        draw_circle(60, 640, 360)
        save_image("Prato.png", width, height)
        glfw.swap_buffers(window)
if __name__ == "__main__":
    main()