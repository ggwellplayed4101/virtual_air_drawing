import cv2
import mediapipe as mp

# Access MediaPipe's hand tracking module and visulaization module
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

# Create a instance of hand object
hands = mp_hands.Hands()


# Access webcam
cap = cv2.VideoCapture(0)

# Load a random image of a cat (with no hands)
cat_frame = cv2.imread('cat_image.jpeg')

while True:
    success, frame = cap.read()
    if not success:
        break
    
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results =  hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks,
                                   mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Webcam", frame)
    if cv2.waitKey(1) == ord('q'):
        break

# To free up resourcesnused by cv2 applications
cap.release()
cv2.destroyAllWindows()
