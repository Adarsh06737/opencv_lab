import cv2

img = cv2.imread("Rc2026.jpg")

height,width,channels = img.shape

datatype = img.dtype

print("Width : ",width)
print("Height : ",height)
print("Channels : ",channels)
print("Size : ",size)
print("Datatype : ",datatype)
