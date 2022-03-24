import os
from typing import NamedTuple

CWD = os.getcwd()

PS2_BASE_OUTPUT_PATH = CWD + '/output/'
PS2_BASE_INPUT_PATH = CWD + '/input/'


TPL_ROWS = 21
TPL_COLS = 21


class ImagePathStorage(NamedTuple):
    ps_1_a_1: str = PS2_BASE_OUTPUT_PATH + 'ps2-1-a-1.png'
    ps_1_a_2: str = PS2_BASE_OUTPUT_PATH + 'ps2-1-a-2.png'
    ps_2_a_1: str = PS2_BASE_OUTPUT_PATH + 'ps2-2-a-1.png'
    ps_2_a_2: str = PS2_BASE_OUTPUT_PATH + 'ps2-2-a-2.png'
    pair_1_l: str = PS2_BASE_INPUT_PATH + 'pair1-L.png'
    pair_1_r: str = PS2_BASE_INPUT_PATH + 'pair1-R.png'
img_storage = ImagePathStorage()