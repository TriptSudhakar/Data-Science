import cv2

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    if ret == False: # image is not captured
        continue

    cv2.imshow("Video Frame",frame)
    cv2.imshow("Gray Frame",gray_frame)

    # Wait for user input - q , then you will stop the loop
    key_pressed = cv2.waitKey(1) & 0xFF 
    # OxFF is hexadecimal for 1111 1111
    # key_pressed returns a 32-bit number, so taking bitwise & gives 8-bit number
    # ord() will return a number from 0 -255 (8-bit)
    if key_pressed == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()