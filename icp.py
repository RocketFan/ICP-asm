import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import utils

from mpl_toolkits.mplot3d import Axes3D

sns.set_theme(style="darkgrid")


class ICP:
    def __init__(self, pc_true, pc_moved):
        self.pc_true = np.array(pc_true)
        self.pc_moved = np.array(pc_moved)
        self.pc_match = []
        self.dim = self.pc_true.shape[1]
        fig = plt.figure()
        self.ax = Axes3D(fig)

    def match_point_to_point(self):
        self.pc_match = []

        for p in self.pc_moved:
            p_match = min(
                self.pc_true, key=lambda k: np.linalg.norm(p - k))
            self.pc_match.append(p_match)

    def solve_SVD(self):
        pc_moved_mean = np.mean(self.pc_moved, axis=0)
        pc_match_mean = np.mean(self.pc_match, axis=0)

        H = np.zeros((self.dim, self.dim))

        for p_moved, p_match in zip(self.pc_moved, self.pc_match):
            H += np.outer((p_match - pc_match_mean), (p_moved - pc_moved_mean))

        U, D, V = np.linalg.svd(H)
        R = np.dot(V, U.transpose())
        R[1, :] = [-R[0, 1], R[0, 0]]  # Prevent from reflection matrix
        t = pc_match_mean - np.dot(pc_moved_mean, R)
        T = utils.get_2D_T(t[0], t[1])

        pc_moved_rotated = np.dot(self.pc_moved, R)
        pc_moved_rotated = np.c_[pc_moved_rotated,
                                 np.ones(self.pc_moved.shape[0])]
        self.pc_moved = np.dot(pc_moved_rotated, T.transpose())[:, :2]

    def visualize_2D_results(self):
        plt.clf()
        sns.scatterplot(x=self.pc_true[:, 0], y=self.pc_true[:, 1])
        sns.scatterplot(x=self.pc_moved[:, 0], y=self.pc_moved[:, 1])

        for p_moved, p_match in zip(self.pc_moved, self.pc_match):
            sns.lineplot(x=[p_moved[0], p_match[0]], y=[p_moved[1], p_match[1]])

        # plt.axis('equal')
        plt.pause(0.0001)