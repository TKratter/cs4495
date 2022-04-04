import os
from typing import NamedTuple

CWD = os.getcwd()

PS2_BASE_OUTPUT_PATH = CWD + '/output/'
PS2_BASE_INPUT_PATH = CWD + '/input/'

TPL_ROWS = 11
TPL_COLS = 11


class ImagePathStorage(NamedTuple):
    pair_1_l: str = PS2_BASE_INPUT_PATH + 'pair1-L.png'
    pair_1_r: str = PS2_BASE_INPUT_PATH + 'pair1-R.png'
    ps_1_a_1: str = PS2_BASE_OUTPUT_PATH + 'ps2-1-a-1.png'
    ps_1_a_2: str = PS2_BASE_OUTPUT_PATH + 'ps2-1-a-2.png'
    ps_2_a_1: str = PS2_BASE_OUTPUT_PATH + 'ps2-2-a-1.png'
    ps_2_a_2: str = PS2_BASE_OUTPUT_PATH + 'ps2-2-a-2.png'
    ps_3_a_1: str = PS2_BASE_OUTPUT_PATH + 'ps2-3-a-1.png'
    ps_3_a_2: str = PS2_BASE_OUTPUT_PATH + 'ps2-3-a-2.png'
    ps_3_b_1: str = PS2_BASE_OUTPUT_PATH + 'ps2-3-b-1.png'
    ps_3_b_2: str = PS2_BASE_OUTPUT_PATH + 'ps2-3-b-2.png'
    ps_4_a_1: str = PS2_BASE_OUTPUT_PATH + 'ps2-4-a-1.png'
    ps_4_a_2: str = PS2_BASE_OUTPUT_PATH + 'ps2-4-a-2.png'
    ps_4_b_1: str = PS2_BASE_OUTPUT_PATH + 'ps2-4-b-1.png'
    ps_4_b_2: str = PS2_BASE_OUTPUT_PATH + 'ps2-4-b-2.png'
    ps_4_b_3: str = PS2_BASE_OUTPUT_PATH + 'ps2-4-b-3.png'
    ps_4_b_4: str = PS2_BASE_OUTPUT_PATH + 'ps2-4-b-4.png'

img_storage = ImagePathStorage()
