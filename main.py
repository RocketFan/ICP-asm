import numpy as np
import utils
import matplotlib.pyplot as plt

from icp import ICP

if __name__ == "__main__":
    R = utils.get_2D_R(np.radians(60))
    T = utils.get_2D_T(0, 0)
    func = utils.get_2D_func([0.00003, 0.0002, 0, 0.001, 1])

    pc_1 = np.array([[x, func(x), 1] for x in range(-40, 25, 1)])
    pc_2 = np.dot(np.dot(pc_1, R.transpose()), T.transpose())
    icp = ICP(pc_1[:, :2], pc_2[:, :2])

    for i in range(0, 100):
        icp.match_point_to_point()
        icp.solve_SVD()
        icp.visualize_2D_results()

        print(i)

    plt.show()