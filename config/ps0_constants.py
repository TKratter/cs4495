import os
from typing import NamedTuple

CWD = os.getcwd()

PS0_BASE_OUTPUT_PATH = CWD + '/outputs/'
PS0_BASE_INPUT_PATH = CWD + '/inputs/'


class Image1PathsStorage(NamedTuple):
    input_path: str = PS0_BASE_INPUT_PATH + 'wide.png'
    ps0_1_a: str = PS0_BASE_OUTPUT_PATH + 'ps0-1-a-1.png'
    ps0_2_a: str = PS0_BASE_OUTPUT_PATH + 'ps0-2-a-1.png'
    ps0_2_b: str = PS0_BASE_OUTPUT_PATH + 'ps0-2-b-1.png'
    ps0_2_c: str = PS0_BASE_OUTPUT_PATH + 'ps0-2-c-1.png'
    ps0_3: str = PS0_BASE_OUTPUT_PATH + 'ps0-3-a-1.png'
    ps0_4_b: str = PS0_BASE_OUTPUT_PATH + 'ps0-4-b-1.png'
    ps0_4_c: str = PS0_BASE_OUTPUT_PATH + 'ps0-4-c-1.png'
    ps0_4_d: str = PS0_BASE_OUTPUT_PATH + 'ps0-4-d-1.png'
    ps0_5_a: str = PS0_BASE_OUTPUT_PATH + 'ps0-5-a-1.png'
    ps0_5_b: str = PS0_BASE_OUTPUT_PATH + 'ps0-5-b-1.png'


class Image2PathsStorage(NamedTuple):
    input_path: str = PS0_BASE_INPUT_PATH + 'tall.png'
    ps0_1_a: str = PS0_BASE_OUTPUT_PATH + 'ps0-1-a-2.png'


img_1_paths = Image1PathsStorage()
img_2_paths = Image2PathsStorage()

SIGMA = 10