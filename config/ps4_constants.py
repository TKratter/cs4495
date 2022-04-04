import os
from typing import NamedTuple

CWD = os.getcwd()

PS4_BASE_OUTPUT_PATH = CWD + '/output/'
PS4_BASE_INPUT_PATH = CWD + '/input/'


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


THRESHOLD_VALUE = 30000
NMP_RADIUS = 5

img_storage = ImagePathStorage()
