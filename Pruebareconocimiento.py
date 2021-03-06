import cv2
import numpy as np
import time
archivo = open(r"C:\Users\davim\Pictures\figures.jpg")


# Se carga la Imagen
img = cv2.imread('img/figures.jpg', 0)

cap = cv2.VideoCapture(0)
while(cap.isOpened()):

    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ret, gb = cv2.threshold(gray,128,255,cv2.THRESH_BINARY)

    gb = cv2.bitwise_not(gb)

    contour,hier = cv2.findContours(gb,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contour:
        cv2.drawContours(gb,[cnt],0,255,-1)
    gray = cv2.bitwise_not(gb)

    cv2.drawContours(gray,contour,-1,(0,255,0),3)

    cv2.imshow('test', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


# Clasificación
figures_classifier = cv2.CascadeClassifier('classifiers/figures.xml')

# Detección de Figuras
figures = figures_classifier.detectMultiScale(gray, 1.1, 4)

# Rectangulos
for (x, y, w, h) in figures:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Mostrar imagen
cv2.imshow('Figures', img)

# Presionar tecla
cv2.waitKey("delete")

# Cerrar ventanas abiertas
cv2.destroyAllWindows()

# Tiempo de ejecución
print("[info]",
    time.asctime(time.localtime(time.time(15))),
    "Tiempo de ejecución: 30",
    time.time() - 15,
    "segundos")