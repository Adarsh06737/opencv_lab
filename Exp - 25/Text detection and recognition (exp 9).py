import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img_path = r"E:\Open Cv  (11239A003)\Exp - 25\Rc2026.jpg"

img = cv2.imread(img_path)

if img is None:
    print("Error: Image not found or path is incorrect")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

text = pytesseract.image_to_string(thresh)

print("Detected Text:")
print(text)

cv2.imshow("Original Image", img)
cv2.imshow("Processed Image", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
