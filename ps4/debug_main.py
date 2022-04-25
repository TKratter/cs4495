import numpy as np

from ps4.sift import plot_angle_for_interest_points, get_matching_points_in_images, plot_matching_points_in_images, \
    find_translation_consensus
from utils.io_utils import load_image, save_image
from utils.image_utils import joined_image_gradients, translate_image
from config.ps4_constants import img_storage, window, ALPHA


debug_image = load_image(img_storage.debug_input)
#
debug_image_translated = translate_image(debug_image, 10, 10)

save_image(debug_image_translated, img_storage.debug_input_translated)


debug_image_translated = load_image(img_storage.debug_input_translated)

plot_angle_for_interest_points(debug_image, save_path=img_storage.debug_image_angles)

plot_matching_points_in_images(debug_image, debug_image_translated, save_path=img_storage.debug_images_matched)

find_translation_consensus(debug_image, debug_image_translated)

