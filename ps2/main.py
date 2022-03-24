# ps2
import os

import cv2

from config.ps2_constants import img_storage
from ps2.disparity_ssd import disparity_ssd
from utils.image_utils import scale_image_to_range, rgb_to_grayscale
from utils.io_utils import save_image, load_image

# 1-a
# Read images
L = cv2.imread(os.path.join('input', 'pair0-L.png'), 0) * (1.0 / 255.0)  # grayscale, [0, 1]
R = cv2.imread(os.path.join('input', 'pair0-R.png'), 0) * (1.0 / 255.0)


D_L = disparity_ssd(L, R)
D_R = disparity_ssd(R, L)

save_image(scale_image_to_range(D_L, (0, 200)), img_storage.ps_1_a_1)
save_image(scale_image_to_range(D_L, (0, 200)), img_storage.ps_1_a_2)

# 2-a
left_image = rgb_to_grayscale(load_image(image_path=img_storage.pair_1_l))
right_image = rgb_to_grayscale(load_image(image_path=img_storage.pair_1_r))

disparity_left = disparity_ssd(left_image, right_image)
disparity_right = disparity_ssd(right_image, left_image)

save_image(scale_image_to_range(disparity_left, (0, 200)), img_storage.ps_2_a_1)
save_image(scale_image_to_range(disparity_right, (0, 200)), img_storage.ps_2_a_2)
