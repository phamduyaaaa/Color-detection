import numpy as np
import cv2
from PIL import Image
from util import get_limits

Camera = cv2.VideoCapture(1)
color = [255, 0, 0]

while True:
    ret, frame = Camera.read()

    hsv_Image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color = color)

    mask = cv2.inRange(hsv_Image,lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        cv2.rectangle(frame, (x1,y1),(x2,y2), (0,255,0), 5)
    print(bbox)
    cv2.imshow("Nhan dien mau sac", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
Camera.release()
cv2.destroyAllWindows()