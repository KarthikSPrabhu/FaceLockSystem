import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Cannot access webcam")
        break

    cv2.imshow("Capture Face - Press S to Save", frame)

    key = cv2.waitKey(1)

    if key == ord('s'):
        cv2.imwrite("face_recognition/known_faces/karthik.jpg", frame)
        print("Face image saved!")
        break

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()