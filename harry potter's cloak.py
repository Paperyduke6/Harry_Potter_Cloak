import cv2 # for image processing
import numpy as np # for mathematical calculations with images

img = cv2.VideoCapture(0)
background = cv2.imread('sample.jpg')

while img.isOpened():
    ret,live_frame = img.read()
    if ret:
        # converting RGB to HSV
        hsv_frame = cv2.cvtColor(live_frame, cv2.COLOR_BGR2HSV)
        # range for lower red
        l_red = np.array([0,120,70])
        u_red = np.array([10,255,255])
        mask1 = cv2.inRange(hsv_frame,l_red,u_red)
        # range for upper red
        l_red = np.array([170,120,70])
        u_red = np.array([180,255,255])
        mask2 = cv2.inRange(hsv_frame,l_red,u_red)
        # Code for blue colour
       # l_blue1= np.array([90,103,20])
       # u_blue1 = np.array([119,255,255])
        #mask1 = cv2.inRange((hsv_frame, l_blue1, u_blue1))

        #l_blue2 = np.array([180,98,20])
        #u_blue2 = np.array([170,255,255])
        #mask2 = cv2.inRange(hsv_frame, l_blue2, u_blue2)
        # Generating Red Mask
        red_mask = mask1+ mask2

        red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_OPEN, np.ones((3,3),np.uint8),iterations=10)
        red_mask = cv2.morphologyEx(red_mask,cv2.MORPH_DILATE,np.ones((3,3),np.uint8),iterations=1)

        # substituting Red colour portion from frame
        part1 = cv2.bitwise_and(background,background,mask=red_mask)

        # for area not under red mask
        red_free = cv2.bitwise_not(red_mask)

        #area not under cloak
        part2 = cv2.bitwise_and(live_frame,live_frame,mask=red_free)

        #output
        cv2.imshow("cloak",part1+part2 )
        if cv2.waitKey(5) == ord('q'):
            break
img.release()
cv2.destroyAllWindows()
