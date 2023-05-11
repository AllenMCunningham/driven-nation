import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def get_wheel_position(relative_x, relative_y, point, normal_vector):
    """
    Get the wheel z positions in 3D space
    """
    z1 = point[2] - (normal_vector[0]*(relative_x - point[0]) + normal_vector[1]*(relative_y - point[1])) / normal_vector[2]
    return z1

class wheel_position:
    """
    A class to represent a wheel position relative to the primary sensor.
    x is horizontal to the direction of travel forward.
    y is parallel to the direction of travel forward.
    """
    def __init__(self, driver_front_x, driver_front_y, driver_rear_x, driver_rear_y, passenger_front_x, passenger_front_y, passenger_rear_x, passenger_rear_y):
        self.driver_front_x = driver_front_x
        self.driver_front_y = driver_front_y
        self.driver_rear_x = driver_rear_x
        self.driver_rear_y = driver_rear_y
        self.passenger_front_x = passenger_front_x
        self.passenger_front_y = passenger_front_y
        self.passenger_rear_x = passenger_rear_x
        self.passenger_rear_y = passenger_rear_y
        
    def find_z_position(self, point, normal_vector):
        """
        Find the z position of all wheels given the plane
        """
        self.driver_front_z = get_wheel_position(self.driver_front_x, self.driver_front_y, point, normal_vector)
        self.driver_rear_z = get_wheel_position(self.driver_rear_x, self.driver_rear_y, point, normal_vector)
        self.passenger_front_z = get_wheel_position(self.passenger_front_x, self.passenger_front_y, point, normal_vector)
        self.passenger_rear_z = get_wheel_position(self.passenger_rear_x, self.passenger_rear_y, point, normal_vector)
        
        self.set_wheel_coordinates()

    def set_wheel_coordinates(self):
        self.driver_front_coordinates = [self.driver_front_x, self.driver_front_y, self.driver_front_z]
        self.driver_rear_coordinates = [self.driver_rear_x, self.driver_rear_y, self.driver_rear_z]
        self.passenger_front_coordinates = [self.passenger_front_x, self.passenger_front_y, self.passenger_front_z]
        self.passenger_rear_coordinates = [self.passenger_rear_x, self.passenger_rear_y, self.passenger_rear_z]

    def plot_wheels(self, ax, color='green'):
        ax.scatter(self.driver_front_x, 
                    self.driver_front_y, 
                    self.driver_front_z,
                    color=color)
        ax.scatter(self.driver_rear_x,
                    self.driver_rear_y,
                    self.driver_rear_z,
                    color=color)
        ax.scatter(self.passenger_front_x,
                    self.passenger_front_y,
                    self.passenger_front_z,
                    color=color)
        ax.scatter(self.passenger_rear_x,
                    self.passenger_rear_y,
                    self.passenger_rear_z,
                    color=color)
        
# sample points that define the vehicle plane
points = [[100, 100, 10],
           [0, 0, 10],
           [100, 70, 10]]
points2 = [[100, 100, 10.25],
            [0, 0, 9.5],
            [100, 70, 9.5]]
points3 = [[100, 100, 8],
            [0, 0, 8],
            [100, 70, 8]]

def find_z_on_plane(xx,yy,x0, y0):
    """
    Find the z value on a plane
    """
    z0 = (xx * x0 + yy * y0)
    return z0

def define_plane_by_points(points):
    """
    Define a plane in 3D space by 3 points.
    Return a point and a normal vector 
    and xx, yy, z plane coordinates.
    """
    # extract the individual coordinates of each point 
    # into separate variables using multiple assignment.
    p0, p1, p2 = points
    x0, y0, z0 = p0
    x1, y1, z1 = p1
    x2, y2, z2 = p2

    # calculate two vectors, u and v, 
    # using the differences between the coordinates 
    # of the points.
    ux, uy, uz = u = [x1-x0, y1-y0, z1-z0]
    vx, vy, vz = v = [x2-x0, y2-y0, z2-z0]

    # Using these vectors calculate the 
    # cross product of u and v to get 
    # a normal vector to the plane.
    u_cross_v = [uy*vz-uz*vy, uz*vx-ux*vz, ux*vy-uy*vx]
    point  = np.array(p0)
    normal = np.array(u_cross_v)

    # The equation of the plane is given by the dot product
    #  of the normal vector with a point on the plane, 
    # set equal to a constant value (which is found by 
    # solving for d).
    d = -point.dot(normal)
    xx, yy = np.meshgrid(range(200), range(200))

    # create a grid of x and y values using 
    # the meshgrid function and calculates 
    # the corresponding z values for each 
    # point on the grid using the equation of the plane. 
    z = (-normal[0] * xx - normal[1] * yy - d) * 1. / normal[2]
    return point, normal, xx, yy, z

if __name__ == "__main__":
    # plot the plane xx,yy,z in a 3D graph
    fig = plt.figure()

    # Add an axes
    ax = fig.add_subplot(111,projection='3d')
    
    wheelPositions = wheel_position(driver_front_x=-10,
                            driver_front_y=-10,
                            driver_rear_x=100,
                            driver_rear_y=-10,
                            passenger_front_x=-10,
                            passenger_front_y=60,
                            passenger_rear_x=100,
                            passenger_rear_y=60)

    p1, n1, xx1, yy1, z1 = define_plane_by_points(points)
    wheelPositions.find_z_position(p1, n1)
    wheelPositions.plot_wheels(ax, color='blue')
    
    p2, n2, xx2, yy2, z2 = define_plane_by_points(points2)
    wheelPositions.find_z_position(p2, n2)
    wheelPositions.plot_wheels(ax, color='red')
    
    p3, n3, xx3, yy3, z3 = define_plane_by_points(points3)
    wheelPositions.find_z_position(p3, n3)
    wheelPositions.plot_wheels(ax, color='green')
    
    ax.plot_surface(xx1, yy1, z1, alpha=0.2, color='blue')
    ax.plot_surface(xx2, yy2, z2, alpha=0.2, color='red')
    ax.plot_surface(xx3, yy3, z3, alpha=0.2, color='green')
    # and plot the point 
    # ax.scatter(p0 , p1 , p2,  color='green')
    # plt3d = plt.figure().gca(projection='3d')
    # plt3d.plot_surface(xx, yy, z)
    # plt.show()