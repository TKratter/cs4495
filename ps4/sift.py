from typing import Optional, List, Tuple

import cv2
import matplotlib.pyplot as plt
import numpy as np

from config.ps4_constants import window, ALPHA
from ps4.harris_corners import image_to_harris_values_matrix
from utils.image_utils import rgb_to_grayscale


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


def plot_matching_points_in_images(image1: np.ndarray, image2: np.ndarray, save_path: Optional[str] = None):
    get_matching_points_in_images(image1, image2, plot=True, save_path=save_path)


def get_matching_points_in_images(image1: np.ndarray, image2: np.ndarray, plot: bool = False,
                                  save_path: Optional[str] = None) -> List[Tuple[np.ndarray, np.ndarray]]:
    matches, points1, points2 = get_matches_and_points_from_images(image1, image2)
    # matches = sorted(matches, key=lambda x: x.distance)
    point_pairs = []
    for dmatch in matches:
        idx_1 = dmatch.queryIdx
        idx_2 = dmatch.trainIdx
        cv_point1 = points1[idx_1]
        cv_point2 = points2[idx_2]
        point1 = np.array(cv_point1.pt, dtype=int)
        point2 = np.array(cv_point2.pt, dtype=int)
        point_pairs.append((point1, point2))
    if plot:
        final_img = np.zeros_like(image1)
        plt.imshow(cv2.drawMatches(image1, points1, image2, points2, matches, final_img, 2))
        if save_path is None:
            plt.show()
        else:
            plt.savefig(save_path, bbox_inches='tight', pad_inches=0)

    return point_pairs


def get_matches_and_points_from_images(image1, image2):
    points1, descriptors1 = compute_sift_descriptors(image1)
    points2, descriptors2 = compute_sift_descriptors(image2)
    bfm = cv2.BFMatcher(crossCheck=True)
    matches = bfm.match(descriptors1, descriptors2)
    return matches, points1, points2


def compute_sift_descriptors(image: np.ndarray):
    sift = cv2.xfeatures2d.SIFT_create()
    points = get_cv2_keypoints_list_from_image(image)
    points, descriptors = sift.compute(image, points)
    return points, descriptors


def get_cv2_keypoints_list_from_image(image: np.ndarray) -> List[cv2.KeyPoint]:
    feature_angles, feature_locations = get_feature_angles_and_locations(image)
    feature_angles_and_locations = list(zip(np.degrees(feature_angles), *feature_locations))

    return [cv2.KeyPoint(x=float(j), y=float(i), size=16, octave=0) for theta, i, j in
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


def find_translation_consensus(image1: np.ndarray, image2: np.ndarray, plot: bool = False,
                               save_path: Optional[str] = None):
    point_pairs = get_matching_points_in_images(image1, image2)
    leading_pair, mean_translation, agreeing_points_indices = ransac_translation(point_pairs)

    matches, points1, points2 = get_matches_and_points_from_images(image1, image2)

    agreeing_matches = [match for i, match in enumerate(matches) if i in agreeing_points_indices]

    final_img = np.zeros_like(image1)
    plt.imshow(
        cv2.drawMatches(image1, points1, image2, points2, agreeing_matches, final_img, 2))
    plt.show()

    if plot:
        final_img = np.zeros_like(image1)
        plt.imshow(cv2.drawMatches(image1, points1, image2, points2, agreeing_matches, final_img, 2))

        if save_path is None:
            plt.show()
        else:
            plt.savefig(save_path, bbox_inches='tight', pad_inches=0)

    return point_pairs


def ransac_translation(point_pairs: List[Tuple[np.ndarray, np.ndarray]],
                       dist_threshold: float = 3) -> Tuple[Tuple[np.ndarray, np.ndarray], np.ndarray, List[int]]:
    trans_vectors = [p2 - p1 for p1, p2 in point_pairs]
    num_of_agreeing_translations = 0
    leading_pair = point_pairs[0]
    mean_translation = np.array([0, 0])
    agreeing_points = []
    agreeing_points_indices = []
    for i, translation in enumerate(trans_vectors):
        agreeing_translations = np.array([np.allclose(translation, t, atol=dist_threshold) for t in trans_vectors])
        if len(agreeing_translations[agreeing_translations]) > num_of_agreeing_translations:
            num_of_agreeing_translations = len(agreeing_translations[agreeing_translations])
            print(f'leading pair has {num_of_agreeing_translations} matches')
            leading_pair = point_pairs[i]
            agreeing_points = np.array(trans_vectors)[agreeing_translations]
            mean_translation = np.stack(agreeing_points, axis=-1).mean(axis=-1)
            agreeing_points_indices = np.argwhere(agreeing_translations).flatten().tolist()
    plt.scatter(*list(zip(*trans_vectors)), c='b')
    plt.scatter(*list(zip(*agreeing_points)), c='r')
    plt.show()
    return leading_pair, mean_translation, agreeing_points_indices
