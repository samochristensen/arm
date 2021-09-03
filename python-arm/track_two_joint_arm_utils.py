from math import cos, sin
import numpy as np


class TrackTwoLinkArm:
    def __init__(self):
        self.joint_angles = [0, 0]
        self.link_length = [1, 1]
        self.track_position = [0, 0]
        self.elbow = [0, 0]
        self.wrist = [0, 0]

    def forward_kinematics(self):
        theta0: float = self.joint_angles[0]
        theta1: float = self.joint_angles[1]
        l0 = self.link_length[0]
        l1 = self.link_length[1]
        self.elbow = self.track_position + np.array([l0 * cos(theta0), l0 * sin(theta0)])
        self.wrist = self.elbow + np.array([l1 * cos(theta0 + theta1), l1 * sin(theta0 + theta1)])

    def set_joints(self, joint_angles):
        self.joint_angles = joint_angles
        self.forward_kinematics()

    def set_track(self, track_position):
        self.track_position = track_position

    def set_links_length(self, link_length: list):
        self.link_length = link_length

    def get_end_effector(self):
        return self.wrist
