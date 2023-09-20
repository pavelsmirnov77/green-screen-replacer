import cv2
import numpy as np

bg_img = cv2.imread('content/background.jpg')

height, width = bg_img.shape[0:2]

video = cv2.VideoCapture(0)

while True:
    _, frame = video.read()

    frame = cv2.resize(frame, (width, height))

    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_hsv = np.array([35, 50, 50])  # Нижний порог для зеленого цвета в HSV
    higher_hsv = np.array([85, 255, 255])  # Верхний порог для зеленого цвета в HSV
    mask = cv2.inRange(frame_hsv, lower_hsv, higher_hsv)

    # Заменяем зеленый фон на фоновое изображение
    result = cv2.bitwise_and(frame, frame, mask=cv2.bitwise_not(mask))
    result += cv2.bitwise_and(bg_img, bg_img, mask=mask)

    cv2.imshow('Result', result)

    if cv2.waitKey(25) == 27:
        break

video.release()
cv2.destroyAllWindows()
