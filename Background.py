# library for image processing
import cv2
#Video capture object
img = cv2.VideoCapture(0)

# Capturing background
while img.isOpened():
    #capturing using camera
    ret,image=img.read()
    if ret:
        cv2.imshow("Picture",image)
        if cv2.waitKey(5) == ord('q'):
            cv2.imwrite("sample.jpg",image)
            break
img.release()
cv2.destroyAllWindows()