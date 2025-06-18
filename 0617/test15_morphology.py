import cv2
import numpy as np

# 원본 이미지 읽기 (컬러 BGR 이미지)
img = cv2.imread('images/morphological.png')

# 3x3 사각형(RECT) 구조화 요소(커널) 생성
# 이 커널은 형태학적 연산에서 사용됨
k = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

# 형태학적 그래디언트 연산 수행
# MORPH_GRADIENT = 팽창(dilate) - 침식(erode)
# 결과는 객체의 경계선 강조
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, k)

# 원본 이미지와 그래디언트 연산 결과를 수평으로 병합
# (두 이미지를 나란히 비교해 볼 수 있도록)
merged = np.hstack((img, gradient))

# 병합된 결과를 창에 출력
cv2.imshow('gradient', merged)

# 키 입력 대기 (아무 키나 입력 시 종료)
cv2.waitKey()

# 모든 OpenCV 창 닫기
cv2.destroyAllWindows()
