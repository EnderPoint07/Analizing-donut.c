"""Generate a circle"""

# Initialize variables
import math

RADIUS = 12.5
SCREEN_HEIGHT, SCREEN_WIDTH = 30, 30
output = []


def reset_output():
    """make output array an empty 2d matrix with dimensions of the screen """
    for row in range(SCREEN_HEIGHT):
        _ = []
        charNum = 0
        for pix in range(SCREEN_WIDTH):
            _.append('  ')
        output.append(_)


def compute_frame():
    # x^2 + y^2 = r^2

    # x = cos(theta) * radius
    # y = sin(theta) * radius

    theta = 0  # theta goes around pointing to the circumference
    while theta <= 2 * math.pi:
        # precompute the sin and cos of theta
        cosTheta = math.cos(theta)
        sinTheta = math.sin(theta)

        # Get the coords of point on circle
        x = cosTheta * RADIUS
        y = sinTheta * RADIUS

        # Calculate the location of the point on screen
        px = int(x + SCREEN_WIDTH / 2)
        py = int(y + SCREEN_HEIGHT / 2)

        output[px][py] = '@ '

        theta += 0.07
    render()


def render():
    # print(output)
    print('\x1b[H')
    for row in range(SCREEN_HEIGHT):
        for colm in range(SCREEN_WIDTH):
            print(output[row][colm], end='')
        print()


def main():
    reset_output()
    compute_frame()


if __name__ == '__main__':
    main()
