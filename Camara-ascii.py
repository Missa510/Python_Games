import curses
import cv2
import os
from curses import wrapper

# Variables
scale = 0.3
contrast = 2

def main(screen):
    # Preparando pantalla
    screen.clear()

    # Captura de camara
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise IOError("No se pudo abrir al programa :(")
    while True:
        # Captura de frames
        ret, frame = cap.read()

        # Reposicionando frames
        frame = cv2.resize(frame, None, fx = scale + 0.1, fy = scale + 0.1, interpolation = cv2.INTER_AREA)
        width = len(frame[0]) * 2

        # Convirtiendo la imagen a escala de grices
        gscale = []
        for i, b in enumerate(frame):
            for x, a in enumerate(b):
                sum = a[0] + a[1] + a[2]
                sum /= 3
                sum *= contrast
                sum =  int(sum)
                gscale.append(sum)
                gscale.append(sum)
        # Convertir la escala de grices a simbolos ASCII
        chars = ["@", "#", "%", "&", "$", "+", "=", "-", ":", ".", " "]
        chars.reverse()
        ascii_px = [ chars[pixel // 25] for pixel in gscale ]
        ascii_px = ''.join(ascii_px)
        ascii_frame = [ascii_px[index : index + width] for index in range(0, len(ascii_px), width)]
        for l, x in enumerate(ascii_frame):
            try:
                screen.addstr(l, 0, x)
            except:
                pass
        screen.refresh()
    cap.release()
    return

wrapper(main)