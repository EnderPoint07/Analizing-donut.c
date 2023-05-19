"""Generate a spinning circle"""

# Initialize variables
import math

from termcolor import colored

SCREEN_HEIGHT, SCREEN_WIDTH = 200, 200
R1 = 26
R2 = R1 / 2

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


def compute_circle(Rx, Ry, Rz):
    # First we precompute the sins and coses of the angles the object is gonna be rotated by
    cosRx = math.cos(Rx)
    sinRx = math.sin(Rx)

    sinRy = math.sin(Ry)
    cosRy = math.cos(Ry)

    sinRz = math.sin(Rz)
    cosRz = math.cos(Rz)

    theta = 0  # theta is used to calculate each point on the circle with angle theta relative to the center
    while theta <= 2 * math.pi:
        # precompute the sin and cos of theta
        costheta = math.cos(theta)
        sintheta = math.sin(theta)

        phi = 0
        while phi <= 2 * math.pi:
            cosphi = math.cos(phi)
            sinphi = math.sin(phi)

            # Magic formula for torus
            x = (R1 + R2 * costheta) * cosphi
            y = R1 * sintheta + R2 * sinphi
            z = R2 * cosphi
            # Now it's time to rotate each point that we have gotten around an axis

            # Calculate the location of the point on screen
            px = int(x + SCREEN_WIDTH / 2)
            py = int(y + SCREEN_HEIGHT / 2)

            if z >= 0:
                output[px][py] = '@ '
            else:
                output[px][py] = colored('$ ', 'red')

            phi += 0.07
        theta += 0.07
    render()


def render():
    print('\x1b[H')
    for row in range(SCREEN_HEIGHT):
        for colm in range(SCREEN_WIDTH):
            print(output[row][colm], end='')
        print()


def main():
    # The angles by which it will be rotated by on its respective axis
    x_axis = 0
    y_axis = 0
    z_axis = 0

    while True:
        reset_output()
        compute_circle(x_axis, y_axis, z_axis)
        x_axis += 0.01
        y_axis += 0
        z_axis += 0


if __name__ == '__main__':
    main()
