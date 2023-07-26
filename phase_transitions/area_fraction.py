import cv2
import numpy as np

img = cv2.imread('videos/test/19860031_frame0_1.png', 0)
print(img.shape)
print(img)
non_zero = np.count_nonzero(img)
print(non_zero)

img2 = cv2.imread('videos/test/19860033_frame0_0.png', 0)
print(img2.shape)
print(img2)
non_zero2 = np.count_nonzero(img2)
print(non_zero2)

print(non_zero/non_zero2)