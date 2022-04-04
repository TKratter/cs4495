# ps2
import os

import cv2

from config.ps2_constants import img_storage
from ps2.disparity_ncorr import disparity_ncorr
from ps2.disparity_ssd import disparity_ssd
from utils.image_utils import scale_image_to_range, rgb_to_grayscale, add_gaussian_noise
from utils.io_utils import save_image, load_image

# 1-a
# Read images
L = cv2.imread(os.path.join('input', 'pair0-L.png'), 0) * (1.0 / 255.0)  # grayscale, [0, 1]
R = cv2.imread(os.path.join('input', 'pair0-R.png'), 0) * (1.0 / 255.0)


# D_L = disparity_ssd(L, R)
# D_R = disparity_ssd(R, L)
#
# save_image(scale_image_to_range(D_L, (0, 200)), img_storage.ps_1_a_1)
# save_image(scale_image_to_range(D_L, (0, 200)), img_storage.ps_1_a_2)

# 2-a
left_image = rgb_to_grayscale(load_image(image_path=img_storage.pair_1_l))
right_image = rgb_to_grayscale(load_image(image_path=img_storage.pair_1_r))

# disparity_left = disparity_ssd(left_image, right_image, max_distance_from_reference=60)
# save_image(disparity_left, img_storage.ps_2_a_1)
# disparity_right = disparity_ssd(right_image, left_image, max_distance_from_reference=60)
# save_image(-disparity_right, img_storage.ps_2_a_2)

# 2-b

# 3-a
noised_right_image = add_gaussian_noise(right_image, sigma=20)
# noised_disparity_left = disparity_ssd(left_image, noised_right_image, max_distance_from_reference=60)
# save_image(noised_disparity_left, img_storage.ps_3_a_1)
# noised_disparity_right = disparity_ssd(noised_right_image, left_image, max_distance_from_reference=60)
# save_image(-noised_disparity_right, img_storage.ps_3_a_2)

# 3-b
# contrasted_right_image = right_image * 1.1
# contrasted_disparity_left = disparity_ssd(left_image, contrasted_right_image, max_distance_from_reference=60)
# save_image(contrasted_disparity_left, img_storage.ps_3_b_1)
# contrasted_disparity_right = disparity_ssd(contrasted_right_image, left_image, max_distance_from_reference=60)
# save_image(-contrasted_disparity_right, img_storage.ps_3_b_2)

# 4-a
# ncorr_disparity_left = disparity_ncorr(left_image, right_image, max_distance_from_reference=60)
# save_image(ncorr_disparity_left, img_storage.ps_4_a_1)
# ncorr_disparity_right = disparity_ncorr(right_image, left_image, max_distance_from_reference=60)
# save_image(-ncorr_disparity_right, img_storage.ps_4_a_2)

# 4-b
# ncorr_contrasted_disparity_left = disparity_ncorr(left_image, contrasted_right_image, max_distance_from_reference=60)
# save_image(ncorr_contrasted_disparity_left, img_storage.ps_4_b_1)
ncorr_noised_disparity_left = disparity_ssd(left_image, noised_right_image, max_distance_from_reference=60)
save_image(ncorr_noised_disparity_left, img_storage.ps_4_b_2)
