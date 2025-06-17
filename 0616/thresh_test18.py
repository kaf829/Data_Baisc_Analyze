import matplotlib.pyplot as plt
import numpy as np
import cv2

img = cv2.imread("images/gray_gradient.jpg", cv2.IMREAD_GRAYSCALE)
thresh_np = np.zeros_like(img)
thresh_np[img > 127] = 255

ret ,thresh_cv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
print(ret)

imgs ={'Original': img, "Numpy API": thresh_np, "cv2.threshold": thresh_cv}
for i, (key, value) in enumerate(imgs.items()):
    plt.subplot(1,3,i+1)
    plt.title(key)
    plt.imshow(value, cmap = 'gray')
    plt.xticks([])
    plt.yticks([])

plt.show()