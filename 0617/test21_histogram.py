import cv2
import numpy as np

# 📌 이미지 읽기 (컬러)
src = cv2.imread("./images/road.jpg")

# 📌 그레이스케일 변환 (BGR -> Gray)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# 📌 히스토그램 그릴 캔버스 생성 (높이: gray 높이, 너비: 256)
result = np.zeros((src.shape[0], 256), dtype=np.uint8)
print(result.shape[0])
# 📌 히스토그램 계산
# gray 픽셀 값(0~255)의 빈도를 계산
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

# 📌 히스토그램 값 정규화 (높이값에 맞게 스케일 조정)
cv2.normalize(hist, hist, 0, result.shape[0], cv2.NORM_MINMAX)

# 📌 히스토그램 그리기 (각 x에 대해 세로 선 그림)
for x, y in enumerate(hist):
    cv2.line(
        result,
        (x, result.shape[0]),
        (x, result.shape[0] - int(y)),
        255
    )

# 📌 원본 gray 이미지와 히스토그램 이미지를 좌우로 붙임
dst = np.hstack([gray, result])

# 📌 크기 축소 (너무 크면 보기 불편하므로 0.5배 축소)
dst_re = cv2.resize(dst, dsize=(0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

# 📌 출력
cv2.imshow("dst", dst_re)
cv2.waitKey(0)
cv2.destroyAllWindows()
