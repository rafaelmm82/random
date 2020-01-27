from scipy import stats
import numpy as np


def curve_fit(series=None, start=None, end=None, step=None):
    """ It fits a curve in a new one using a linear approximation."""

    x_axis = series[:, 0].tolist()
    y_axis = series[:, 1]
    new_x_axis = np.linspace(start, end, step)
    new_y_values = np.zeros(step)
    last_index = len(x_axis) - 1

    for i in range(len(new_x_axis) - 1):

        x_near = min(x_axis, key=lambda x: abs(x - new_x_axis[i]))
        x_near_index = x_axis.index(x_near)

        if x_near_index <= 3:
            a, b, _, _, _ = stats.linregress(x_axis[:4], y_axis[:4])
        elif x_near_index == last_index:
            a, b, _, _, _ = stats.linregress(x_axis[-4:], y_axis[-4:])
        else:
            a, b, _, _, _ = stats.linregress(x_axis[x_near_index-2:x_near_index+2], y_axis[x_near_index-2:x_near_index+2])

        new_y_values[i] = a * new_x_axis[i] + b

    return np.array([new_x_axis, new_y_values])

