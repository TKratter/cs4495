import numpy as np
from utils.io_utils import save_image, load_image

from config.ps0_constants import img_1_paths, img_2_paths

from utils.image_utils import Channels, swap_red_and_blue_channels, get_monochrome_image, \
    replace_image_1_center_with_image_2_center

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

    # 2-c
    red_image_1 = get_monochrome_image(image_1, channel=Channels.RED)
    save_image(red_image_1, img_1_paths.ps0_2_c)

    # 2-d
    """
    ps0-2-b-1 seems to be a better monochrome image.
    I believe it is because Green colors are more dominant in the chosen image.
    """

    # 3
    monochrome_image_1 = green_image_1
    monochrome_image_2 = get_monochrome_image(image_2, channel=Channels.GREEN)
    replaced_center_image = replace_image_1_center_with_image_2_center(monochrome_image_1, monochrome_image_2,
                                                                       center_size=100)
    save_image(replaced_center_image, img_1_paths.ps0_3)
