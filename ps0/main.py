import numpy as np
from typing import Union
from utils.image_utils import save_image, load_image

from config.ps0_constants import img_1_paths, img_2_paths, Channels


def swap_red_and_blue_channels(image: np.ndarray) -> np.ndarray:
    return image[:, :, ::-1]


def get_monochrome_image(image: np.ndarray, channel: Channels) -> np.ndarray:
    return image[:, :, channel.value]


if __name__ == '__main__':
    # 1-a
    image_1 = load_image(img_1_paths.input_path)
    save_image(image_1, img_1_paths.ps0_1_a)
    image_2 = load_image(img_2_paths.input_path)
    save_image(image_2, img_2_paths.ps0_1_a)

    # 2-a
    swapped_channels_image_1 = swap_red_and_blue_channels(image_1)
    save_image(swapped_channels_image_1, img_1_paths.ps0_2_a)
    # 2-b
    green_image_1 = get_monochrome_image(image_1, channel=Channels.GREEN)
    save_image(green_image_1, img_1_paths.ps0_2_b)

