import numpy as np

from ps4.sift import plot_angle_for_interest_points, get_matching_points_in_images, plot_matching_points_in_images, \
    find_translation_consensus
from utils.io_utils import load_image, save_image
from utils.image_utils import joined_image_gradients
from config.ps4_constants import img_storage, window, ALPHA
from harris_corners import image_to_harris_values_matrix
import time

# 1-a
trans_a = load_image(img_storage.trans_a)
# save_image(joined_image_gradients(trans_a), img_storage.ps_1_a_1)
#
sim_a = load_image(img_storage.sim_a)
# save_image(joined_image_gradients(sim_a), img_storage.ps_1_a_2)

# 1-b
trans_b = load_image(img_storage.trans_b)
sim_b = load_image(img_storage.sim_b)
# save_image(image_to_harris_values_matrix(image=trans_a, window=window, alpha=ALPHA), img_storage.ps_1_b_1)
# save_image(image_to_harris_values_matrix(image=trans_b, window=window, alpha=ALPHA), img_storage.ps_1_b_2)
# save_image(image_to_harris_values_matrix(image=sim_a, window=window, alpha=ALPHA), img_storage.ps_1_b_3)
# save_image(image_to_harris_values_matrix(image=sim_b, window=window, alpha=ALPHA), img_storage.ps_1_b_4)

# 1-c
# save_image(image_to_harris_values_matrix(image=trans_a, window=window, alpha=ALPHA, threshold=True, nms=True),
#            img_storage.ps_1_c_1)
# save_image(image_to_harris_values_matrix(image=trans_b, window=window, alpha=ALPHA, threshold=True, nms=True),
#            img_storage.ps_1_c_2)
# save_image(image_to_harris_values_matrix(image=sim_a, window=window, alpha=ALPHA, threshold=True, nms=True),
#            img_storage.ps_1_c_3)
# save_image(image_to_harris_values_matrix(image=sim_b, window=window, alpha=ALPHA, threshold=True, nms=True),
#            img_storage.ps_1_c_4)

# 2-a
# plot_angle_for_interest_points(trans_a, save_path=img_storage.ps_2_a_1)
# plot_angle_for_interest_points(sim_a, save_path=img_storage.ps_2_a_2)

# 2-b


plot_matching_points_in_images(trans_a, trans_b)
# plot_matching_points_in_images(trans_a, trans_b, save_path=img_storage.ps_2_b_1)
# plot_matching_points_in_images(sim_a, sim_b, save_path=img_storage.ps_2_b_2)

# 2-c
find_translation_consensus(trans_a, trans_b)
