from track_two_joint_arm_utils import TrackTwoLinkArm
from random import randrange
import matplotlib.pyplot as plt

arm = TrackTwoLinkArm()
arm.set_links_length([1, 3])
plt.figure(1)
N = 20000
results_x = []
results_y = []
results_track = []

for _ in range(N):
    theta0 = randrange(360)
    theta1 = randrange(360)
    track_position = randrange(1000)/1000 * 8

    arm.set_joints([theta0, theta1])
    arm.set_track([track_position, 0])

    arm.forward_kinematics()

    end_effector = arm.get_end_effector()
    results_x.append(end_effector[0])
    results_y.append(end_effector[1])
    results_track.append(track_position)

plt.plot([results_x], [results_y], 'ro', markersize=0.5)
plt.plot([results_track], [0], 'bo', markersize=0.75)
plt.plot([0], [0], 'ko', markersize=0.75)
plt.grid(True)
plt.show()
