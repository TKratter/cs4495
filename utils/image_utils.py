from enum import Enum
from typing import Tuple, Union

import numpy as np
import cv2


class Channels(Enum):
    RED: int = 2
    GREEN: int = 1
    BLUE: int = 0


def swap_red_and_blue_channels(image: np.ndarray) -> np.ndarray:
    return image[:, :, ::-1]


def get_monochrome_image(image: np.ndarray, channel: Channels) -> np.ndarray:
    return image[:, :, channel.value]


def replace_image_1_center_with_image_2_center(image1: np.ndarray, image2: np.ndarray, center_size) -> np.ndarray:
    image1_height_center_indices, image1_width_center_indices = get_monochrome_image_center_xy_indices(image1,
                                                                                                       center_size)

    image2_height_center_indices, image2_width_center_indices = get_monochrome_image_center_xy_indices(image2,
                                                                                                       center_size)
    crop2 = image2[image2_height_center_indices[0]:image2_height_center_indices[-1],
            image2_width_center_indices[0]:image2_width_center_indices[-1]]
    image1_copy = image1.copy()
    image1_copy[image1_height_center_indices[0]:image1_height_center_indices[-1],
    image1_width_center_indices[0]:image1_width_center_indices[-1]] = crop2
    return image1_copy


def get_monochrome_image_center_xy_indices(image: np.ndarray, size: int = None) -> Union[
    Tuple[int, int], Tuple[np.ndarray, np.ndarray]]:
    if len(image.shape) != 2:
        raise ValueError(f'expected image to be monochrome, but got image of shape {image.shape}')
    image_height, image_width = image.shape
    if size is None:
        return np.ceil(image_height / 2), np.ceil(image_width / 2)
    else:
        height_indices = get_interval_from_center(np.ceil(image_height / 2), size=size)
        width_indices = get_interval_from_center(np.ceil(image_width / 2), size=size)
        return height_indices, width_indices


def get_interval_from_center(center: int, size: int) -> np.ndarray:
    start = center - np.floor(size / 2)
    return np.arange(start=start, stop=start + size).astype(int)


def normalize_image(image: np.ndarray) -> np.ndarray:
    return (image - image.mean()) / image.std()


def add_gaussian_noise_to_chanel(image: np.ndarray, channel: Channels, sigma=float) -> np.ndarray:
    image_height, image_width, _ = image.shape
    noise = (np.random.randn(image_height, image_width) * sigma).astype(np.uint8)
    image_copy = image.copy()
    image_copy[:, :, channel.value] += noise
    return image_copy


def scale_image_to_range(image: np.ndarray, range_: Tuple[Union[int, float], Union[int, float]]) -> np.ndarray:
    return ((image - image.min()) / image.ptp()) * (range_[1] - range_[0]) + range_[0]


def rgb_to_grayscale(image: np.ndarray) -> np.ndarray:
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
