import cv2
import matplotlib.pyplot as plt

img = cv2.imread("./images/mountain.jpg")
cv2.imshow('img', img)

channels = cv2.split(img)
colors = ('b', 'g', 'r')
for (ch, color) in zip(channels, colors):
    hist = cv2.calcHist([ch], [0],None, [256], [0,256])
    plt.plot(hist, color =color)

plt.show()

