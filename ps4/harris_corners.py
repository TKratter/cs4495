import numpy as np

from config.ps4_constants import THRESHOLD_VALUE, nms_RADIUS
from utils.image_utils import directioned_gradient_image, Directions, rgb_to_grayscale
from scipy import signal
from tqdm import tqdm
import numba
import scipy.ndimage.filters as filters


def image_to_harris_values_matrix(image: np.ndarray, window: np.ndarray, alpha: float,
                                  threshold: bool = False, nms: bool = False) -> np.ndarray:
    if len(image.shape) == 3:
        image = rgb_to_grayscale(image)
    i_x = directioned_gradient_image(image, Directions.X)
    i_y = directioned_gradient_image(image, Directions.Y)
    i_xx = i_x * i_x
    i_yy = i_y * i_y
    i_xy = i_x * i_y

    i_xx_conv = signal.convolve(i_xx, window, mode='same')
    i_yy_conv = signal.convolve(i_yy, window, mode='same')
    i_xy_conv = signal.convolve(i_xy, window, mode='same')

    harris_matrixes = np.stack((np.stack((i_xx_conv, i_xy_conv), axis=-1), np.stack((i_xy_conv, i_yy_conv), axis=-1)),
                               axis=-1)

    harris_values = harris_matrixes_to_values_matrix(harris_matrixes=harris_matrixes, alpha=alpha)
    if threshold:
        harris_values[harris_values < THRESHOLD_VALUE] = 0

    if nms:
        harris_values = non_maximal_suppression(harris_values)

    return harris_values


@numba.njit
def harris_matrixes_to_values_matrix(harris_matrixes: np.ndarray, alpha: float) -> np.ndarray:
    height, width, _, _ = harris_matrixes.shape

    values_matrix = np.zeros((height, width))

    for x in range(height):
        for y in range(width):
            values_matrix[x, y] = moment_matrix_to_harris_value(matrix=harris_matrixes[x, y, :, :], alpha=alpha)
    return values_matrix


@numba.njit
def moment_matrix_to_harris_value(matrix: np.ndarray, alpha: float) -> float:
    eigen_values, _ = np.linalg.eig(matrix)

    lambda1, lambda2 = eigen_values

    return lambda1 * lambda2 - alpha * (lambda1 + lambda2) ** 2


def non_maximal_suppression(harris_values: np.ndarray, radius: int = nms_RADIUS) -> np.ndarray:
    local_maxima_indices = np.argwhere((harris_values * 1.01 - filters.maximum_filter(harris_values, size=radius)) > 0)
    local_maxima_indices = list(zip(*local_maxima_indices))
    new_harris_values = np.zeros(harris_values.shape)
    new_harris_values[local_maxima_indices] = harris_values[local_maxima_indices]
    return new_harris_values
