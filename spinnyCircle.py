"""Generate a circle"""

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
    # x^2 + y^2 = r^2

    # x = cos(theta) * radius
    # y = sin(theta) * radius

    cosA = math.cos(A)
    sinA = math.sin(A)

    theta = 0  # theta goes around pointing to the circumference
    while theta <= 2 * math.pi:

        phi = 0  # phi is the angle the that everything gets rotated by
        while phi <= 2 * math.pi:
            # precompute the sin and cos of theta
            cosTheta = math.cos(theta)
            sinTheta = math.sin(theta)

            # Get the coords of point on circle
            x = cosTheta * RADIUS
            y = sinTheta * RADIUS

            # Calculate the sin and cos of phi
            sin_phi = math.sin(math.radians(B))
            cos_phi = math.cos(math.radians(B))

            rot_x = round(x * cosA * cos_phi - y * cosA * sin_phi)
            rot_y = round(x * sinA * sin_phi + y * cosA * cos_phi)

            # rot_x = round(x * cos_phi - y * sin_phi)
            # rot_y = round(x * sin_phi + y * cos_phi)

            # Calculate the location of the point on screen
            px = int(rot_x + SCREEN_WIDTH / 2)
            py = int(rot_y + SCREEN_HEIGHT / 2)

            # px = int(x + SCREEN_WIDTH/2)
            # py = int(y + SCREEN_HEIGHT/2)

            if theta >= math.pi:
                output[px][py] = '@ '
            else:
                output[px][py] = colored('$ ', 'red')

            phi += 0.02
            # sleep(0.01)
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
        A += 0.05
        B += 1


if __name__ == '__main__':
    main()
