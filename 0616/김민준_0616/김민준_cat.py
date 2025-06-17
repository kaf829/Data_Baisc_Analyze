import cv2  # OpenCV 라이브러리 (이미지 처리용)
import matplotlib.pyplot as plt  # Matplotlib 라이브러리 (이미지 시각화용)

blk_size = 9
C = 5


img = cv2.imread('images/cat.jpg', cv2.IMREAD_GRAYSCALE)


_, t_190 = cv2.threshold(img, 190, 255, cv2.THRESH_BINARY)


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
    't: 190': t_190,
    'Otsu: %d' % ret: t_otsu,
    'Adapted_Mean': th2,
    'Adapted_Gaussian': th3
}


plt.figure(figsize=(12, 8))  

for i, (k, v) in enumerate(imgs.items()):
    plt.subplot(2, 3, i + 1)  # 2행 3열 배치
    plt.title(k)
    plt.imshow(v, cmap='gray')
    plt.xticks([])
    plt.yticks([])

plt.show()
