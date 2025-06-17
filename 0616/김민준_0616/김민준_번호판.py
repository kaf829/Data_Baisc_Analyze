import cv2
import matplotlib.pyplot as plt

blk_size = 9
C = 5

img = cv2.imread('images/number.jpg', cv2.IMREAD_GRAYSCALE)

_, t_137 = cv2.threshold(img, 88    , 255, cv2.THRESH_BINARY)

ret, t_otsu = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print('otsu threshold:', ret)

th2 = cv2.adaptiveThreshold(
    img, 255,
    cv2.ADAPTIVE_THRESH_MEAN_C,
    cv2.THRESH_BINARY,
    blk_size, C
)

th3 = cv2.adaptiveThreshold(
    img, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    blk_size, C
)

imgs = {
    'Original': img,
    't: 137': t_137,
    'Otsu: %d' % ret: t_otsu,
    'Adapted_Mean': th2,
    'Adapted_Gaussian': th3
}

plt.figure(figsize=(12, 8))

for i, (k, v) in enumerate(imgs.items()):
    plt.subplot(2, 3, i + 1)
    plt.title(k)
    plt.imshow(v, cmap='gray')
    plt.xticks([])
    plt.yticks([])

plt.show()
