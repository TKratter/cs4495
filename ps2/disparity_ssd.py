from typing import Tuple

import numpy as np
from tqdm import tqdm

from config.ps2_constants import TPL_COLS, TPL_ROWS


def disparity_ssd(left_mat: np.ndarray, right_mat: np.ndarray) -> np.ndarray:
    """Compute disparity map D(y, x) such that: L(y, x) = R(y, x + D(y, x))
    
    Params:
    L: Grayscale left image
    R: Grayscale right image, same size as L

    Returns: Disparity map, same size as L, R
    """

    row_size, col_size = left_mat.shape

    disparity_matrix = np.zeros((row_size, col_size))

    for r in tqdm(range(row_size)):
        for c in range(col_size):
            disparity_matrix[r, c] = calculate_disparity_for_left_reference_point(left_reference_point=(r, c),
                                                                                  left_mat=left_mat,
                                                                                  right_mat=right_mat)

    return disparity_matrix


def calculate_disparity_for_left_reference_point(left_reference_point: Tuple[int, int], left_mat: np.ndarray,
                                                 right_mat: np.ndarray) -> int:
    row_patch_start, row_patch_end, col_patch_start, col_patch_end = get_patch_corners(left_reference_point)
    left_patch = _create_valid_patch(row_patch_start, row_patch_end, col_patch_start, col_patch_end, left_mat)
    right_strip = _create_valid_strip(row_patch_start, row_patch_end, right_mat)
    sliding_window_view = create_sliding_window_view(strip=right_strip)
    squared_differences = (sliding_window_view - left_patch[:, :, np.newaxis]) ** 2
    ssd_array = squared_differences.sum(axis=(0, 1))
    best_match_column = ssd_array.argmin()

    return left_reference_point[1] - best_match_column


def create_sliding_window_view(strip: np.ndarray) -> np.ndarray:
    zero_padded_strip = np.hstack([np.zeros((TPL_ROWS, int(np.floor(TPL_COLS / 2)))),
                                   strip,
                                   np.zeros((TPL_ROWS, int(np.floor(TPL_COLS / 2))))])
    sliding_window_view = np.lib.stride_tricks.sliding_window_view(zero_padded_strip, window_shape=TPL_COLS, axis=1)
    return np.swapaxes(sliding_window_view, 1, -1)


def calculate_ssd_for_reference_points(left_reference_point: Tuple[int, int], right_reference_point: Tuple[int, int],
                                       left_mat: np.ndarray, right_mat: np.ndarray) -> float:
    left_mat_patch = _create_valid_patch(*get_patch_corners(left_reference_point), mat=left_mat)
    right_mat_patch = _create_valid_patch(*get_patch_corners(right_reference_point), mat=right_mat)

    return ((left_mat_patch - right_mat_patch) ** 2).sum()


def get_patch_corners(reference_point: Tuple[int, int]):
    row_patch_start = int(reference_point[0] - np.floor(TPL_ROWS / 2))
    row_patch_end = int(reference_point[0] + np.floor(TPL_ROWS / 2) + 1)
    col_patch_start = int(reference_point[1] - np.floor(TPL_COLS / 2))
    col_patch_end = int(reference_point[1] + np.floor(TPL_COLS / 2) + 1)
    return row_patch_start, row_patch_end, col_patch_start, col_patch_end


def _create_valid_patch(row_start: int, row_end: int, col_start: int, col_end: int, mat: np.ndarray) -> np.ndarray:
    row_num, col_num = mat.shape

    patch = np.zeros((TPL_ROWS, TPL_COLS))

    valid_row_start, valid_row_end, valid_col_start, valid_col_end = get_valid_rows_and_columns_indices(
        row_start=row_start, row_end=row_end, col_start=col_start, col_end=col_end, row_num=row_num, col_num=col_num)
    patch_row_start = valid_row_start - row_start
    patch_col_start = valid_col_start - col_start
    patch_row_end = TPL_ROWS - (row_end - valid_row_end)
    patch_col_end = TPL_COLS - (col_end - valid_col_end)
    patch[patch_row_start: patch_row_end, patch_col_start: patch_col_end] = mat[valid_row_start: valid_row_end,
                                                                                valid_col_start: valid_col_end]

    return patch


def get_valid_rows_and_columns_indices(row_start: int, row_end: int, col_start: int, col_end: int, col_num: int,
                                       row_num: int) -> Tuple[int, int, int, int]:
    valid_row_start = int(np.max((row_start, 0)))
    valid_col_start = int(np.max((col_start, 0)))
    valid_row_end = int(np.min((row_end, row_num)))
    valid_col_end = int(np.min((col_end, col_num)))

    return valid_row_start, valid_row_end, valid_col_start, valid_col_end


def _create_valid_strip(row_start: int, row_end: int, mat: np.ndarray):
    dummy_value = 0
    row_num, col_num = mat.shape
    strip = np.zeros((TPL_ROWS, col_num))
    col_start = col_end = dummy_value

    valid_row_start, valid_row_end, _, _ = get_valid_rows_and_columns_indices(
        row_start=row_start, row_end=row_end, col_start=col_start, col_end=col_end, row_num=row_num, col_num=col_num)

    patch_row_start = valid_row_start - row_start
    patch_row_end = TPL_ROWS - (row_end - valid_row_end)
    strip[patch_row_start: patch_row_end, :] = mat[valid_row_start: valid_row_end, :]
    return strip
