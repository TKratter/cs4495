import numpy as np
import cv2


def load_image(image_path: str) -> np.ndarray:
    return cv2.imread(image_path)


def save_image(image: np.ndarray, path: str):
    cv2.imwrite(path, image)
