import os
from typing import NamedTuple
import numpy as np

CWD = os.getcwd()

PS4_BASE_OUTPUT_PATH = CWD + '/output/'
PS4_BASE_INPUT_PATH = CWD + '/input/'
PS4_DEBUG_PATH = CWD + '/debug/'


class ImagePathStorage(NamedTuple):
    trans_a: str = PS4_BASE_INPUT_PATH + 'transA.jpg'
    sim_a: str = PS4_BASE_INPUT_PATH + 'simA.jpg'
    trans_b: str = PS4_BASE_INPUT_PATH + 'transB.jpg'
    sim_b: str = PS4_BASE_INPUT_PATH + 'simB.jpg'
    ps_1_a_1: str = PS4_BASE_OUTPUT_PATH + 'ps4-1-a-1.png'
    ps_1_a_2: str = PS4_BASE_OUTPUT_PATH + 'ps4-1-a-2.png'
    ps_1_b_1: str = PS4_BASE_OUTPUT_PATH + 'ps4-1-b-1.png'
    ps_1_b_2: str = PS4_BASE_OUTPUT_PATH + 'ps4-1-b-2.png'
    ps_1_b_3: str = PS4_BASE_OUTPUT_PATH + 'ps4-1-b-3.png'
    ps_1_b_4: str = PS4_BASE_OUTPUT_PATH + 'ps4-1-b-4.png'
    ps_1_c_1: str = PS4_BASE_OUTPUT_PATH + 'ps4-1-c-1.png'
    ps_1_c_2: str = PS4_BASE_OUTPUT_PATH + 'ps4-1-c-2.png'
    ps_1_c_3: str = PS4_BASE_OUTPUT_PATH + 'ps4-1-c-3.png'
    ps_1_c_4: str = PS4_BASE_OUTPUT_PATH + 'ps4-1-c-4.png'
    ps_2_a_1: str = PS4_BASE_OUTPUT_PATH + 'ps4-2-a-1.png'
    ps_2_a_2: str = PS4_BASE_OUTPUT_PATH + 'ps4-2-a-2.png'
    ps_2_b_1: str = PS4_BASE_OUTPUT_PATH + 'ps4-2-b-1.png'
    ps_2_b_2: str = PS4_BASE_OUTPUT_PATH + 'ps4-2-b-2.png'
    debug_input: str = PS4_DEBUG_PATH + 'red_star.png'
    debug_input_translated: str = PS4_DEBUG_PATH + 'red_star_translated.png'
    debug_image_angles: str = PS4_DEBUG_PATH + 'red_star_angles.png'
    debug_images_matched: str = PS4_DEBUG_PATH + 'red_star_matched.png'


THRESHOLD_VALUE = 90000
nms_RADIUS = 10
window = np.ones((3, 3)) / 9
# window = np.array([[1, 4, 1],
#                    [4, 6, 4],
#                    [1, 4, 1]]) / 24
ALPHA = 0.04

img_storage = ImagePathStorage()
