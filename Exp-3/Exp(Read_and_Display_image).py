import cv2

img = cv2.imread("Rc2026.jpg")

cv2.imshow("Original image",img)

cv2.waitkey(0)
cv2.destroyAllWinows()
