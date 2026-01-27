import cv2
img = cv2.imread("Rc2026.jpg")
resized = cv2.resize(img,(400,300))
gray = cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(img,(5,5),0)
edges = cv2.Canny(blur,100,200)

cv2.imshow("orginal",img)
cv2.imshow("gray",gray)
cv2.imshow("edges",edges)
cv2.imshow("blur",blur)
cv2.imshow("resized",resized)

cv2.waitKey(0)
cv2.destroyAllWindows(0)