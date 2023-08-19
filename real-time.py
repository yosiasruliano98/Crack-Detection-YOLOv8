from ultralytics import YOLO
import cv2
import time

model = YOLO('runs/detect/train22/weights/best.pt')

cam = cv2.VideoCapture(0)
if not cam.isOpened():
    raise ("No Camera")

while True:
    ret, image = cam.read()
    if not ret:
        break

    _time_mulai = time.time()
    result = model.predict(image, show=True)

    print("waktu",time.time(),_time_mulai)

    _key = cv2.waitKey(1)
    if _key == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()