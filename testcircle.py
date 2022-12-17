"""Generate a circle"""

# Initialize variables
import math
from time import sleep

RADIUS = 12.5
SCREEN_HEIGHT, SCREEN_WIDTH = 30, 30
output = []

A = 1

cosA = math.cos(A)
sinA = math.sin(A)


def reset_output():
    """make output array an empty 2d matrix with dimensions of the screen """
    for row in range(SCREEN_HEIGHT):
        _ = []
        charNum = 0
        for pix in range(SCREEN_WIDTH):
            _.append(' ')
        output.append(_)


def compute_frame():
    # x^2 + y^2 = r^2

    # x = cos(theta) * radius
    # y = sin(theta) * radius

    theta = 0  # theta is the angle
    while theta < 360:
        theta += 1

        # precompute the sin and cos of theta
        cosTheta = math.cos(theta)
        sinTheta = math.sin(theta)

        # Ge the coords of point on circle
        x = cosTheta * RADIUS
        y = sinTheta * RADIUS

        # Calculate the location of the point on screen
        px = int(x + SCREEN_WIDTH / 2)
        py = int(y + SCREEN_WIDTH / 2)

        print(f"x is {x} and y is {y}")
        print(f"px is {px} and py is {py}")

        output[px][py] = '@'

        render()
        sleep(0.01)

    # render()


def render():
    # print(output)
    print('\x1b[H')
    print('\x1b[2J')
    for row in range(SCREEN_HEIGHT):
        for colm in range(SCREEN_WIDTH):
            print(output[row][colm], end='')
        print()


def main():
    reset_output()
    compute_frame()


if __name__ == '__main__':
    main()
