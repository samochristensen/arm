import matplotlib.pyplot as plt
from two_joint_arm_utils import TwoLinkArm
from random import randrange

arm = TwoLinkArm()
results = []
N = 20000
plt.figure(1)

for _ in range(N):
    theta0 = randrange(180)
    theta1 = randrange(180)
    arm.update_joints([theta0, theta1])
    arm.forward_kinematics()
    end_effector: list = arm.get_wrist()
    results.append(end_effector)
    plt.plot(end_effector[0], end_effector[1], 'ro', markersize=0.5)

plt.plot([0], [0], 'ko', markersize=0.75)
plt.grid(True)
plt.axis("square")
plt.show()
