import os
from typing import NamedTuple

CWD = os.getcwd()

PS2_BASE_OUTPUT_PATH = CWD + '/output/'
PS2_BASE_INPUT_PATH = CWD + '/input/'


TPL_ROWS = 11
TPL_COLS = 11


class ImagePathStorage(NamedTuple):
    ps_1_a_1: str = PS2_BASE_OUTPUT_PATH + 'ps2-1-a-1.png'
    ps_1_a_2: str = PS2_BASE_OUTPUT_PATH + 'ps2-1-a-2.png'


img_storage = ImagePathStorage()