import cv2
import numpy as np
from Tools.demo.sortvisu import interpolate  # ⚠️ 주의: 이 모듈이 꼭 필요한지 확인하세요. OpenCV에서는 필요 없습니다.

# 원본 이미지 읽기
img = cv2.imread("./images/cat.jpg")

# 이미지 축소 (1/2 크기)
smaller = cv2.pyrDown(img)

# 다시 확대 (원래 크기 근처로 복원)
bigger = cv2.pyrUp(smaller)

# 라플라시안 피라미드 계산 (원본 - 업샘플된 이미지)
laplacian = cv2.subtract(img, bigger)

# 라플라시안 피라미드로 복원 시도 (bigger + laplacian)
restored = bigger + laplacian

# 여러 이미지를 가로로 연결
merged = np.hstack([img, laplacian, bigger, restored])

# OpenCV의 resize로 크기 축소 (1/2 크기)
merged = cv2.resize(merged, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# 결과 출력
cv2.imshow("Laplacian Pyramid", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()
