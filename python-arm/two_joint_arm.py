from utils import TwoLinkArm
from time import sleep
import matplotlib.pyplot as plt

arm = TwoLinkArm()

theta0 = 0.5
theta1 = 1

arm.update_joints([theta0, theta1])
arm.forward_kinematics()
arm.get_wrist()

'''
arm.plot()
waypoints = [[0, 0], [-1, 0], [1.5, 0.1], [0.76, 0.4], [0.5, 0.5], [1, 1]]
for r in waypoints:
    arm.move_end_to(r[0], r[1])
    arm.plot()
    plt.xlim([-1.5, 1.5])
    plt.ylim([-1.5, 1.5])
    plt.grid("both")
    plt.show()
    sleep(2)
    '''
