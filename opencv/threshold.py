import cv2
import numpy as np
from matplotlib import pyplot as plt

img_bgr = cv2.imread('./image/S__26132483.jpg')
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
ret, img_binary = cv2.threshold(img_gray, 150,255,cv2.THRESH_BINARY)

cv2.imshow("img_binary", img_binary)
# pause
keycode = cv2.waitKey(0)
# ESC key to exit
if keycode == 27:         
    cv2.destroyAllWindows()

img_binary_reverse = cv2.bitwise_not(img_binary)

cv2.imshow("img_binary_reverse", img_binary_reverse)
# pause
keycode = cv2.waitKey(0)
# ESC key to exit
if keycode == 27:         
    cv2.destroyAllWindows()
