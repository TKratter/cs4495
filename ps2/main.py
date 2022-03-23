# ps2
import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
from ps2.disparity_ssd import disparity_ssd
from utils.io_utils import save_image
from config.ps2_constants import img_storage
# 1-a
# Read images
L = cv2.imread(os.path.join('input', 'pair0-L.png'), 0) * (1.0 / 255.0)  # grayscale, [0, 1]
R = cv2.imread(os.path.join('input', 'pair0-R.png'), 0) * (1.0 / 255.0)

# Compute disparity (using method disparity_ssd defined in disparity_ssd.py)

D_L = disparity_ssd(L, R)
D_R = disparity_ssd(R, L)

save_image(D_L, img_storage.ps_1_a_1)
save_image(D_R, img_storage.ps_1_a_2)


# TODO: Rest of your code here
