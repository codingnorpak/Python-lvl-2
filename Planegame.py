import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Define the vertices of a simple plane model
vertices = [
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (0, 0, 1)  # Tip of the plane
]

edges = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (0, 4),
    (1, 4),
    (2, 4),
    (3, 4)
]

def draw_plane():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -10)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            glTranslatef(-0.1, 0, 0)
        if keys[pygame.K_RIGHT]:
            glTranslatef(0.1, 0, 0)
        if keys[pygame.K_UP]:
            glTranslatef(0, 0.1, 0)
        if keys[pygame.K_DOWN]:
            glTranslatef(0, -0.1, 0)

        glRotatef(1, 3, 1, 1)  # Rotate the plane for effect

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_plane()
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
