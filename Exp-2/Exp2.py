import cv2
import numpy as np

img = cv2.imread("Rc2026.jpg",0)
_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
kernel = np.ones((5,5), np.uint8)
erosion = cv2.erode(binary, kernel, iterations=1)
dilation = cv2.dilate(binary, kernel, iterations=1)
opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
cv2.imshow("Original Image", img)
cv2.imshow("Binary Image", binary)
cv2.imshow("Erosion", erosion)
cv2.imshow("Dilation", dilation)
cv2.imshow("Opening", opening)
cv2.imshow("Closing", closing)
cv2.waitKey(0)
cv2.destroyAllWindows()