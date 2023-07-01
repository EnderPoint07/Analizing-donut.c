"""Generate a spinning torus"""


# Initialize variables
import math

from termcolor import colored

R1 = 20
R2 = 10

screen_size = int(2 * (R1 + R2) + 1) # rule for this is x > (R1 + R2) + x/2 OR x = 2(R1 + R2) + 1 
# due to the offset i do while calculating px and py

SCREEN_HEIGHT, SCREEN_WIDTH = screen_size, screen_size

output = []
z_buffer = []



def reset_buffers():

    """make output array an empty 2d matrix and z_buffer a 2d 0 array with dimensions of the screen """

    output.clear()

    z_buffer.clear()


    for row in range(SCREEN_HEIGHT):

        _ = []

        __ = []

        for pix in range(SCREEN_WIDTH):

            _.append('  ')

            __.append(0)
            

        output.append(_)

        z_buffer.append(__)        


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
            
            min_z = -(R1 + R2)
            max_z = R1 + R2
            
            luminance = ((0 - 12) * ((rot_z - min_z)/(max_z - min_z))) + 12 # normalize z between 0 and 11 (the min and max index)
            # with greater z being smaller luminance using the function 
            # y\ =\ \left(b\ -\ a\right)\ \frac{x\ -\ x_{min}}{x_{max}\ -\ x_{min}}+a
            # with b = 0; a = 12; x_{min}=-\left(R_{1}\ +\ R_{2}\right); x_{max}=R_{1}\ +\ R_{2};
            # R2 = 10; R1 = 20; for testing purposes
            # Use desmos for drop in using of the function
        
            try:
                if luminance > z_buffer[px][py]:
                    z_buffer[px][py] = luminance
                    output[px][py] = colored(r' .,-~:;=!*#$@'[round(luminance)] + ' ', "red")
                    if z < 0: # i.e further from us
                        output[px][py] = colored(r' .,-~:;=!*#$@'[round(luminance)]) + ' '
            except Exception as e:
                print(rot_x, px,rot_y, py)          

                print(f"z = {rot_z}")
                print(f"lumin = {luminance}")
                raise e
            
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
        reset_buffers()
        compute_frame(x_axis, y_axis, z_axis)

        x_axis += 0.00

        y_axis += 0.01

        z_axis += 0.001



if __name__ == '__main__':
    main()

