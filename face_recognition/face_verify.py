from deepface import DeepFace
import cv2
import requests

REFERENCE_IMAGE = "face_recognition/known_faces/karthik.jpg"
ESP32_URL = "http://192.168.31.35/unlock"

cap = cv2.VideoCapture(0)

print("=================================")
print("Face Lock System Started")
print("Press V to Verify Face")
print("Press Q to Quit")
print("=================================")

while True:

    ret, frame = cap.read()

    if not ret:
        print("Camera Error")
        break

    cv2.imshow("Face Lock System", frame)

    key = cv2.waitKey(1)

    if key == ord('v'):

        print("\nVerifying Face...")

        cv2.imwrite("temp.jpg", frame)

        try:

            result = DeepFace.verify(
                img1_path=REFERENCE_IMAGE,
                img2_path="temp.jpg",
                enforce_detection=False
            )

            if result["verified"]:

                print("✅ ACCESS GRANTED")
                print("Sending Unlock Command...")

                response = requests.get(ESP32_URL)

                print("ESP32 Response:", response.text)

            else:

                print("❌ ACCESS DENIED")

        except Exception as e:

            print("Error:", e)

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()