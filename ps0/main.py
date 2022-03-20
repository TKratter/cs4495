from scipy.ndimage.interpolation import shift
from utils.io_utils import save_image, load_image

from config.ps0_constants import img_1_paths, img_2_paths, SIGMA

from utils.image_utils import Channels, swap_red_and_blue_channels, get_monochrome_image, \
    replace_image_1_center_with_image_2_center, normalize_image, add_gaussian_noise_to_chanel

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

    # 4-a
    print(f"""question 4-a:
    image min: {green_image_1.min()}, image max: {green_image_1.max()} 
    image mean: {green_image_1.mean()}, image std: {green_image_1.std()}""")

    # 4-b
    save_image(normalize_image(image_1) * 10 + image_1.mean(), img_1_paths.ps0_4_b)

    # 4-c
    shifted_green_image_1 = shift(green_image_1, shift=(0, 2), cval=0)
    save_image(shifted_green_image_1, img_1_paths.ps0_4_c)

    # 4-d
    diff_green_image_1 = green_image_1 - shifted_green_image_1
    save_image(diff_green_image_1, img_1_paths.ps0_4_d)

    # 5-a
    noised_green_image_1 = add_gaussian_noise_to_chanel(image_1, Channels.GREEN, sigma=SIGMA)
    save_image(noised_green_image_1, img_1_paths.ps0_5_a)

    # 5-b

    noised_blue_image_1 = add_gaussian_noise_to_chanel(image_1, Channels.BLUE, sigma=SIGMA)
    save_image(noised_blue_image_1, img_1_paths.ps0_5_b)

    # 5-c
    # todo: check that
    print(f"""question 5-c:
        it seems as if blue is more visible, It could be beacuse of the scaling of each channel""")
