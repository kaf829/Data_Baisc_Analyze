import cv2
import numpy as np
img1 = cv2.imread("images/morph_hole.png", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("images/morph_dot.png", cv2.IMREAD_GRAYSCALE)


k = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))

opening = cv2.morphologyEx(img1, cv2.MORPH_OPEN, k)
closing = cv2.morphologyEx(img1, cv2.MORPH_CLOSE, k)

merged1= np.hstack((img1, opening))
merged2 =  np.hstack((img1, closing))

cv2.imshow('opening', merged1)
cv2.imshow("closing", merged2)

cv2.waitKey(0)
cv2.destroyAllWindows()