"""Generate a spinning torus"""

# Initialize variables
import math

from termcolor import colored

SCREEN_HEIGHT, SCREEN_WIDTH = 200, 200
R1 = 50
R2 = 25

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


def compute_frame(Rx, Ry, Rz):
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

        phi = 0  # phi is used to calculate each point on the another circle perpendicular to the main with angle phi
        # with the origin being the calculated point from theta
        while phi <= 2 * math.pi:
            cosphi = math.cos(phi)
            sinphi = math.sin(phi)

            # Magic formula for torus
            x = (R1 + R2 * costheta) * cosphi
            y = (R1 + R2 * costheta) * sinphi
            z = R2 * sintheta

            # Now it's time to rotate each point that we have gotten around an axis by multiplying by the rotation
            # matrices

            # Rotation around x axis:
            # x' = x
            # y' = y * cos(Rx) - z * sin(Rx)
            # z' = y * sin(Rx) + z * cos(Rx)

            x_Rx = x
            y_Rx = y * cosRx - z * sinRx
            z_Rx = y * sinRx - z * cosRx

            # Rotation around y axis:
            # x'' = x' * cos(Ry) + z' * sin(Ry)
            # y'' = y'
            # z'' = -x' * sin(Ry) + z' * cos(Ry)

            x_Rxy = x_Rx * cosRy + z_Rx * sinRy
            y_Rxy = y_Rx
            z_Rxy = -x_Rx * sinRy + z_Rx * cosRy

            # Rotation around z axis:
            # x''' = x'' * cos(Rz) - y'' * sin(Rz)
            # y''' = x'' * sin(Rz) + y'' * cos(Rz)
            # z''' = z''

            rot_x = x_Rxy * cosRz - y_Rxy * sinRz
            rot_y = x_Rxy * sinRz + y_Rxy * cosRz
            rot_z = z_Rxy

            # Calculate the location of the point on screen
            px = int(rot_x + SCREEN_WIDTH / 2)
            py = int(rot_y + SCREEN_HEIGHT / 2)

            if rot_z >= 0:
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
        compute_frame(x_axis, y_axis, z_axis)
        x_axis += 0.03
        y_axis += 0.03
        z_axis += 0.03


if __name__ == '__main__':
    main()
