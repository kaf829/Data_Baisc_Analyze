import cv2
import numpy as np

# 원본 이미지 읽기 (morph_hole.png 파일, 컬러 BGR 형식)
img = cv2.imread('images/morph_dot.png')

# 구조화 요소(커널) 생성
# 사각형(RECT) 형태 3x3 커널
k1 = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

# 십자가(CROSS) 형태 3x3 커널
k2 = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))

# 십자가(CROSS) 형태 3x3 커널 (여기선 의미 중복, 나중에 ELLIPSE로 바꾸는 것이 일반적)
k3 = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))

# 팽창 연산 (Dilation) 수행
# 사각형 커널로 팽창 (3회 반복)
rect = cv2.dilate(img, k1, iterations=3)

# ❗ 현재 cross와 ellipse도 k1을 사용 → 사실 k2, k3을 사용해야 의도대로 다른 커널을 적용
# 십자가 커널로 팽창 (3회 반복) → 코드상 k1 사용 중 (수정 필요)
cross = cv2.dilate(img, k1, iterations=3)

# 십자가 커널로 팽창 (3회 반복) → 코드상 k1 사용 중 (수정 필요)
ellipse = cv2.dilate(img, k1, iterations=3)

# 팽창 결과들을 원본과 함께 가로로 결합
# merged = [원본, rect 결과, cross 결과, ellipse 결과] 한 줄로 나열
merged = np.hstack((img, rect, cross, ellipse))

# 결과 이미지 출력
cv2.imshow("Dilation", merged)

# 키 입력 대기
cv2.waitKey(0)

# 모든 창 닫기
cv2.destroyAllWindows()
