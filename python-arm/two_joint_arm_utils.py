from math import cos, sin, acos, atan2
import numpy as np
import matplotlib.pyplot as plt


class TwoLinkArm:
    def __init__(self, joint_angles=None):
        if joint_angles is None:
            joint_angles = [0, 0]
        self.joint_angles = joint_angles
        self.shoulder = np.array([0, 0])
        self.link_lengths = [1, 1]
        self.elbow = [0, 0]
        self.wrist = [0, 0]

    def inverse_kinematics(self, x, y):
        len0 = self.link_lengths[0]
        len1 = self.link_lengths[1]
        angle1 = acos((x**2 + y**2 - len0**2 - len1**2)/(2*len0*len1))
        angle0 = atan2(y, x) - atan2(len1*sin(angle1), len0 + len1*cos(angle1))

        return angle0, angle1

    def move_end_to(self, x, y):
        self.update_joints(self.inverse_kinematics(x, y))

    def update_joints(self, joint_angles):
        self.joint_angles = joint_angles
        self.forward_kinematics()

    def forward_kinematics(self):
        theta0 = self.joint_angles[0]
        theta1 = self.joint_angles[1]
        l0 = self.link_lengths[0]
        l1 = self.link_lengths[1]
        self.elbow = self.shoulder + np.array([l0*cos(theta0), l0*sin(theta0)])
        self.wrist = self.elbow + np.array([l1*cos(theta0 + theta1), l1*sin(theta0 + theta1)])

    def get_wrist(self) -> list:
        return self.wrist

    def plot(self):
        plt.plot([self.shoulder[0], self.elbow[0]],
                 [self.shoulder[1], self.elbow[1]],
                 'r-')
        plt.plot([self.elbow[0], self.wrist[0]],
                 [self.elbow[1], self.wrist[1]],
                 'r-')
        plt.plot(self.shoulder[0], self.shoulder[1], 'ko')
        plt.plot(self.elbow[0], self.elbow[1], 'ko')
        plt.plot(self.wrist[0], self.wrist[1], 'ko')


def transform_points(points, theta, origin):
    T = np.array([[cos(theta), -sin(theta), origin[0]],
                  [sin(theta),  cos(theta), origin[1]],
                  [0, 0, 1]])
    return np.matmul(T, np.array(points))
