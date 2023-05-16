"""Generate a spinning circle"""

# Initialize variables
import math

from termcolor import colored

SCREEN_HEIGHT, SCREEN_WIDTH = 100, 100
RADIUS = SCREEN_WIDTH / 2 - 5
output = []


def reset_output():
    """make output array an empty 2d matrix with dimensions of the screen """
    output.clear()

    for row in range(SCREEN_HEIGHT):
        _ = []
        charNum = 0
        for pix in range(SCREEN_WIDTH):
            _.append('  ')
        output.append(_)


def compute_circle(A, B):
    # formula for circle -> x^2 + y^2 = r^2

    # equation for each point on the circle
    # x = cos(theta) * radius
    # y = sin(theta) * radius

    cosA = math.cos(A)
    sinA = math.sin(A)

    sin_B = math.sin(B)
    cos_B = math.cos(B)

    theta = 0  # theta is used to calculate each point on the circle with angle theta relative to the center
    while theta <= 2 * math.pi:
        # precompute the sin and cos of theta
        cosTheta = math.cos(theta)
        sinTheta = math.sin(theta)

        # Get the coords of point on circle
        x = cosTheta * RADIUS
        y = sinTheta * RADIUS

        # rot_x = round(x * cosA * cos_B - y * cosA * sin_B)
        # rot_y = round(x * sinA * sin_B + y * cosA * cos_B)

        rot_x = round(x * cos_B - y * sin_B)
        rot_y = round(x * sin_B + y * cos_B)

        # Calculate the location of the point on screen
        px = int(rot_x + SCREEN_WIDTH / 2)
        py = int(rot_y + SCREEN_HEIGHT / 2)

        # px = int(x + SCREEN_WIDTH/2)
        # py = int(y + SCREEN_HEIGHT/2)

        if theta >= math.pi:
            output[px][py] = '@ '
        else:
            output[px][py] = colored('$ ', 'red')

        theta += 0.07
    render()


def render():
    print('\x1b[H')
    for row in range(SCREEN_HEIGHT):
        for colm in range(SCREEN_WIDTH):
            print(output[row][colm], end='')
        print()


def main():
    A = 1
    B = 1

    while True:
        reset_output()
        compute_circle(A, B)
        A += 0.005
        B += 0.005


if __name__ == '__main__':
    main()
