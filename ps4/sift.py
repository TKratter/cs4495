from typing import Optional, List, Tuple

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import scipy
from scipy import stats
import pandas as pd
import cv2
import itertools

from config.ps4_constants import window, ALPHA
from ps4.harris_corners import image_to_harris_values_matrix
from utils.image_utils import directioned_gradient_image, Directions, normalize_image, rgb_to_grayscale


def plot_angle_for_interest_points(image: np.ndarray, save_path: Optional[str] = None):
    feature_angles, feature_locations = get_feature_angles_and_locations(image)
    magnitude = 30
    plt.figure()
    plt.imshow(image)
    plt.quiver(*feature_locations[::-1], magnitude * np.cos(feature_angles[::-1]),
               magnitude * np.sin(feature_angles[::-1]),
               units='dots', minshaft=1, width=2, scale=2, headwidth=1, headlength=2)
    plt.axis('off')
    if save_path is None:
        plt.show()
    else:
        plt.savefig(save_path, bbox_inches='tight', pad_inches=0)


def plot_matching_points_in_images(image1: np.ndarray, image2: np.ndarray, save_path: Optional[str] = None,
                                   **sift_params):
    point_pairs = get_matching_points_in_images(image1, image2, **sift_params)
    joined_image = np.hstack((image1, image2))
    plt.figure()
    plt.imshow(joined_image)
    height2, width2, _ = image2.shape
    p2_shift = np.array([0, width2])
    for p1, p2 in point_pairs:
        x1, y1 = p1
        x2, y2 = p2 + p2_shift
        plt.plot([y1, y2], [x1, x2], color='r', linewidth=0.2)
    plt.axis('off')
    if save_path is None:
        plt.show(bbox_inches='tight')
    else:
        plt.savefig(save_path, bbox_inches='tight', pad_inches=0)


def get_matching_points_in_images(image1: np.ndarray, image2: np.ndarray, topk_matches=40, **sift_params) -> List[
    Tuple[np.ndarray, np.ndarray]]:
    points1, descriptors1 = compute_sift_descriptors(image1, **sift_params)
    points2, descriptors2 = compute_sift_descriptors(image2, **sift_params)
    bfm = cv2.BFMatcher(crossCheck=True)
    matches = bfm.match(descriptors1, descriptors2)
    matches = sorted(matches, key=lambda x: x.distance)
    point_pairs = []
    top_matches = matches[:topk_matches]
    for dmatch in top_matches:
        idx_1 = dmatch.queryIdx
        idx_2 = dmatch.trainIdx
        cv_point1 = points1[idx_1]
        cv_point2 = points2[idx_2]
        point1 = np.array(cv_point1.pt, dtype=int)
        point2 = np.array(cv_point2.pt, dtype=int)
        point_pairs.append((point1, point2))
    debug = True
    if debug:
        final_img = np.zeros_like(image1)
        plt.imshow(cv2.drawMatches(image1, points1, image2, points2, matches[:topk_matches], final_img, 2))
        plt.show()
    return point_pairs


def compute_sift_descriptors(image: np.ndarray, **sift_params):
    sift = cv2.xfeatures2d.SIFT_create(**sift_params)
    points = get_cv2_keypoints_list_from_image(image)
    points, descriptors = sift.compute(image, points)
    return points, descriptors


def get_cv2_keypoints_list_from_image(image: np.ndarray) -> List[cv2.KeyPoint]:
    feature_angles, feature_locations = get_feature_angles_and_locations(image)
    feature_angles_and_locations = list(zip(np.degrees(feature_angles), *feature_locations))

    return [cv2.KeyPoint(x=float(y), y=float(x), size=16, octave=0) for theta, x, y in
            feature_angles_and_locations]


def get_feature_angles_and_locations(image: np.ndarray):
    harris_values = image_to_harris_values_matrix(image=image, window=window, alpha=ALPHA, threshold=True, nms=True)
    feature_locations = list(zip(*np.argwhere(harris_values > 0)))
    angles = compute_angles(image)
    feature_angles = angles[feature_locations]
    return feature_angles, feature_locations


def compute_angles(image: np.ndarray) -> np.ndarray:
    dx, dy = np.gradient(rgb_to_grayscale(image))
    angles = np.arctan2(dx, dy)
    return angles


def find_translation_consensus(image1: np.ndarray, image2: np.ndarray, **sift_params):
    point_pairs = get_matching_points_in_images(image1, image2, **sift_params)

    (p1, p2), mean_translation = ransac_translation(point_pairs)
    height2, width2, _ = image2.shape
    p2_shift = np.array([0, width2])
    x1, y1 = p1
    x2, y2 = p2 + p2_shift
    joined_image = np.hstack((image1, image2))
    plt.figure()
    plt.imshow(joined_image)
    x2_mean, y2_mean = p2 + p2_shift + mean_translation
    height2, width2, _ = image2.shape
    p2_shift = np.array([0, width2])
    plt.plot([y1, y2], [x1, x2], color='r', label='best translation')
    plt.plot([y1, y2_mean], [x1, x2_mean], color='b', label='mean translation')
    plt.legend()
    plt.axis('off')

    plt.show(bbox_inches='tight')


def ransac_translation(point_pairs: List[Tuple[np.ndarray, np.ndarray]], dist_threshold: float = 3) -> Tuple[Tuple[
                                                                                                                 np.ndarray, np.ndarray], np.ndarray]:
    trans_vectors = [p2 - p1 for p1, p2 in point_pairs]
    num_of_agreeing_translations = 0
    leading_pair = point_pairs[0]
    mean_translation = np.array([0, 0])
    for i, translation in enumerate(trans_vectors):
        agreeing_translations = np.array([np.allclose(translation, t, atol=dist_threshold) for t in trans_vectors])
        if len(agreeing_translations[agreeing_translations]) > num_of_agreeing_translations:
            num_of_agreeing_translations = len(agreeing_translations[agreeing_translations])
            print(f'leading pair has {num_of_agreeing_translations} matches')
            leading_pair = point_pairs[i]
            mean_translation = np.stack(np.array(trans_vectors)[agreeing_translations], axis=-1).mean(axis=-1)
            agreeing_points = np.array(trans_vectors)[agreeing_translations]
    plt.scatter(*list(zip(*trans_vectors)), c='b')
    plt.scatter(*list(zip(*agreeing_points)), c='r')
    plt.show()
    return leading_pair, mean_translation
