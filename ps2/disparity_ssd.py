import numpy as np
from config.ps2_constants import TPL_COLS, TPL_ROWS
from typing import Tuple


def disparity_ssd(left_mat: np.ndarray, right_mat: np.ndarray) -> np.ndarray:
    """Compute disparity map D(y, x) such that: L(y, x) = R(y, x + D(y, x))
    
    Params:
    L: Grayscale left image
    R: Grayscale right image, same size as L

    Returns: Disparity map, same size as L, R
    """

    row_size, col_size = left_mat.shape

    disparity_matrix = np.zeros((row_size, col_size))

    for r in range(row_size):
        for c in range(col_size):
            disparity_matrix[r, c] = 1 / (calculate_ssd_for_reference_point(reference_point=(r, c), left_mat=left_mat,
                                                                            right_mat=right_mat) + 0.01)

    return disparity_matrix


def calculate_ssd_for_reference_point(reference_point: Tuple[int, int], left_mat: np.ndarray,
                                      right_mat: np.ndarray) -> float:
    left_mat_patch = _create_valid_patch(row_start=0, row_end=TPL_ROWS, col_start=0, col_end=TPL_COLS,
                                         mat=left_mat)
    row_right_mat_patch_start = int(reference_point[0] - np.floor(TPL_ROWS / 2))
    row_right_mat_patch_end = int(reference_point[0] + np.floor(TPL_ROWS / 2) + 1)
    col_right_mat_patch_start = int(reference_point[1] - np.floor(TPL_COLS / 2))
    col_right_mat_patch_end = int(reference_point[1] + np.floor(TPL_COLS / 2) + 1)
    right_mat_patch = _create_valid_patch(row_start=row_right_mat_patch_start, row_end=row_right_mat_patch_end,
                                          col_start=col_right_mat_patch_start, col_end=col_right_mat_patch_end,
                                          mat=right_mat)

    return ((left_mat_patch - right_mat_patch) ** 2).sum()


def _create_valid_patch(row_start: int, row_end: int, col_start: int, col_end: int, mat: np.ndarray) -> np.ndarray:
    row_num, col_num = mat.shape

    patch = np.zeros((TPL_ROWS, TPL_COLS))

    valid_row_start = int(np.max((row_start, 0)))
    valid_col_start = int(np.max((col_start, 0)))
    patch_row_start = valid_row_start - row_start
    patch_col_start = valid_col_start - col_start

    valid_row_end = int(np.min((row_end, row_num)))
    valid_col_end = int(np.min((col_end, col_num)))
    patch_row_end = TPL_ROWS - (row_end - valid_row_end)
    patch_col_end = TPL_COLS - (col_end - valid_col_end)

    patch[patch_row_start: patch_row_end, patch_col_start: patch_col_end] = mat[valid_row_start: valid_row_end,
                                                                                valid_col_start: valid_col_end]

    return patch
