from ps2.disparity_ssd import disparity_by_callable, get_patch_corners, _create_valid_patch, _create_valid_strip, \
    find_nearest
from typing import Tuple, Optional, Callable

import numpy as np

import cv2
from config.ps2_constants import TPL_COLS, TPL_ROWS


def disparity_ncorr(left_mat: np.ndarray, right_mat: np.ndarray,
                    max_distance_from_reference: Optional[int] = None) -> np.ndarray:
    """Compute disparity map D(y, x) such that: L(y, x) = R(y, x + D(y, x))
    
    Params:
    L: Grayscale left image
    R: Grayscale right image, same size as L

    Returns: Disparity map, same size as L, R
    """

    disparity_matrix = disparity_by_callable(match_func=calculate_ncorr_for_left_reference_point, left_mat=left_mat,
                                             right_mat=right_mat,
                                             max_distance_from_reference=max_distance_from_reference)

    return disparity_matrix


def calculate_ncorr_for_left_reference_point(left_reference_point: Tuple[int, int], left_mat: np.ndarray,
                                             right_mat: np.ndarray,
                                             max_distance_from_reference: Optional[int] = None) -> int:
    row_patch_start, row_patch_end, col_patch_start, col_patch_end = get_patch_corners(left_reference_point)
    left_patch = _create_valid_patch(row_patch_start, row_patch_end, col_patch_start, col_patch_end, left_mat)
    right_strip = _create_valid_strip(row_patch_start, row_patch_end, right_mat)
    normalized_ccor = cv2.matchTemplate(right_strip.astype('uint8'), left_patch.astype('uint8'),
                                        cv2.TM_CCORR_NORMED).flatten()
    if max_distance_from_reference is None:
        best_match_column = normalized_ccor.argmax()
    else:
        lower_col_limit = np.max((left_reference_point[1] - max_distance_from_reference - TPL_COLS, 0))
        upper_col_limit = np.min(
            (left_reference_point[1] + max_distance_from_reference + TPL_COLS, normalized_ccor.size))
        best_match_column = find_nearest(
            np.argwhere(normalized_ccor == normalized_ccor[lower_col_limit: upper_col_limit].max()),
            left_reference_point[1])
    return left_reference_point[1] - best_match_column
