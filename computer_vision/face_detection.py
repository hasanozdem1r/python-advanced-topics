# import opencv
import cv2

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Reading the image as it is
img = cv2.imread("res/bear.jpg")

# Reading the image as a gray scale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Search the co-ordinates of the image

faces = faceCascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)
# detectMultiScale method to search for the face rectangle co-ordinates
# scaleFactor decreases the shape value by %5 until the face is found. Smaller the value, the greater is accuracy

for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
img = cv2.resize(img, (700, 900))
cv2.imshow("Hasan Ozdemir", img)

cv2.waitKey(0)  # wait until user press a key
cv2.destroyAllWindows()  # closes the window based on wait for key parameter
