import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import gluPerspective

pygame.init()

# Set up display
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

# Set up perspective
gluPerspective(45, (display[0] / display[1]), 0.1, 100.0)
glTranslatef(0.0, 0.0, -10)

# Function to draw a triangle
def draw_triangle():
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)  # Red
    glVertex3f(0.0, 2.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)  # Green
    glVertex3f(-2.0, -2.0, 0.0)
    glColor3f(0.0, 0.0, 1.0)  # Blue
    glVertex3f(2.0, -2.0, 0.0)
    glEnd()

# Function for translation
def translate(x, y, z):
    glTranslatef(x, y, z)

# Function for rotation
def rotate(angle, x, y, z):
    glRotatef(angle, x, y, z)

# Function for scaling
def scale(sx, sy, sz):
    glScalef(sx, sy, sz)

# Function to display the triangle with transformations
def display_triangle(frame_counter):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    draw_triangle()

    # Transformations
    # Uncomment section to view desired transformation

    # SECTION 1 (Translation)
    # if frame_counter < 300:
    #     translate(0.005, 0.005, 0.0)

    # SECTION 2 (Rotation)
    # rotate(5.0, 0.0, 0.0, 1.0)

    # SECTION 3 (Scaling)
    # if frame_counter < 200:
    #     scale(0.995, 0.995, 1.0)

    # SECTION 4 (Rotation and Scaling)
    # if frame_counter < 250:
    #     rotate(1.0, 0.0, 0.0, 1.0)
    # elif frame_counter < 350:
    #     scale(0.995, 0.995, 1.0)
    # elif frame_counter < 400:
    #     pass

    # SECTION 5 (Scaling and Rotation)
    # if frame_counter < 200:
    #     scale(0.995, 0.995, 1.0)
    # elif frame_counter < 250:
    #     pass
    # else:
    #     rotate(1.0, 0.0, 0.0, 1.0)

    # END OF SECTIONS

    pygame.display.flip()

# Enable depth testing
glEnable(GL_DEPTH_TEST)

# Main loop
frame_counter = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Display the triangle with transformations
    display_triangle(frame_counter)
    frame_counter += 1
    pygame.time.wait(10)
