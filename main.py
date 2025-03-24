import cv2

# Access webcam
cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    if not success:
        break
    
    # Show the iamge in the frame
    cv2.imshow("Webcam", frame)

    # Close the application when q is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# To free up resourcesnused by cv2 applications
cap.release()
cv2.destroyAllWindows()
