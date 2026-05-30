from deepface import DeepFace
import cv2

reference_image = "face_recognition/known_faces/karthik.jpg"

cap = cv2.VideoCapture(0)

print("Press V to verify")
print("Press Q to quit")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Face Lock System", frame)

    key = cv2.waitKey(1)

    if key == ord('v'):
        cv2.imwrite("temp.jpg", frame)

        try:
            result = DeepFace.verify(
                img1_path=reference_image,
                img2_path="temp.jpg",
                enforce_detection=False
            )

            if result["verified"]:
                print("\n✅ ACCESS GRANTED")
            else:
                print("\n❌ ACCESS DENIED")

        except Exception as e:
            print("Error:", e)

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()