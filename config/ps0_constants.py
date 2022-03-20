from typing import NamedTuple
from enum import Enum
import os

CWD = os.getcwd()

PS0_BASE_OUTPUT_PATH = CWD + '/outputs/'
PS0_BASE_INPUT_PATH = CWD + '/inputs/'


class Image1PathsStorage(NamedTuple):
    input_path: str = PS0_BASE_INPUT_PATH + 'wide.png'
    ps0_1_a: str = PS0_BASE_OUTPUT_PATH + 'ps0-1-a-1.png'
    ps0_2_a: str = PS0_BASE_OUTPUT_PATH + 'ps0-2-a-1.png'
    ps0_2_b: str = PS0_BASE_OUTPUT_PATH + 'ps0-2-b-1.png'


class Image2PathsStorage(NamedTuple):
    input_path: str = PS0_BASE_INPUT_PATH + 'tall.png'
    ps0_1_a: str = PS0_BASE_OUTPUT_PATH + 'ps0-1-a-2.png'


class Channels(Enum):
    RED: int = 0
    GREEN: int = 1
    BLUE: int = 2

img_1_paths = Image1PathsStorage()
img_2_paths = Image2PathsStorage()