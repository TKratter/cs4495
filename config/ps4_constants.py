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


img_storage = ImagePathStorage()
