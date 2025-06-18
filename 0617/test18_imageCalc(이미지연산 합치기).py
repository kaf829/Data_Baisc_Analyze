import cv2
import matplotlib.pyplot as plt

# 이미지 로드
img1 = cv2.imread('images/wing_wall.jpg')
img2 = cv2.imread('images/yate.jpg')

# 이미지 크기 맞추기 (필요시)
if img1.shape != img2.shape:
    img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

# 단순 numpy 덧셈 (overflow 발생)
img3 = img1 + img2

# OpenCV add (saturate)
img4 = cv2.add(img1, img2)

# 출력
imgs = {'img1': img1, 'img2': img2, 'img1 + img2': img3, 'cv.add(img1, img2)': img4}

plt.figure(figsize=(10,8))

for i, (k, v) in enumerate(imgs.items()):
    plt.subplot(2, 2, i + 1)
    plt.imshow(cv2.cvtColor(v, cv2.COLOR_BGR2RGB))  # BGR -> RGB
    plt.title(k)
    plt.xticks([]); plt.yticks([])

plt.tight_layout()
plt.show()
