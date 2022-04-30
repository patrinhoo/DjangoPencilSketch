import numpy as np
import cv2
from PIL import Image


def to_sketch(img):
    img = img.convert("RGB")

    img = np.asarray(img)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_invert = cv2.bitwise_not(img_gray)
    img_smoothing = cv2.GaussianBlur(
        img_invert, (21, 21), sigmaX=0, sigmaY=0)
    final_img = cv2.divide(img_gray, 255-img_smoothing, scale=256)

    sketch = Image.fromarray(final_img)

    return sketch
