import cv2  # OpenCV 라이브러리 임포트 (영상 처리 기능 제공)

# 📌 1. 컬러 이미지 읽기
src = cv2.imread("./images/duck.jpg", cv2.IMREAD_COLOR)
# "./images/duck.jpg" 파일을 컬러(BGR) 모드로 읽어옴

# 📌 2. 컬러 이미지를 그레이스케일로 변환
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# 컬러(BGR) 이미지를 흑백(그레이스케일) 이미지로 변환
# threshold 적용은 일반적으로 그레이스케일에서 수행

# 📌 3. 이진화 처리
ret, dst = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
# 픽셀 값이 100을 넘으면 255(흰색), 100 이하이면 0(검정)으로 설정
# ret에는 실제 사용된 threshold 값 (Otsu 등 사용시 의미있음, 여기선 100)

# 📌 4. 이진화 이미지 크기 축소 (1/2 크기)
dst = cv2.resize(dst, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
# 이진화된 이미지를 가로, 세로 0.5배로 축소
# INTER_AREA 보간법은 축소에 적합 (이미지 품질 좋음)

# 📌 5. 원본 이미지 크기 축소 (1/2 크기)
src = cv2.resize(src, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
# src 이미지도 동일한 방식으로 크기 축소

# 📌 6. 결과 출력 (OpenCV 창)
cv2.imshow('src', src)
# 축소된 원본 컬러 이미지 출력

cv2.imshow('dst', dst)
# 축소되고 이진화된 이미지 출력

# 키 입력을 기다림 (아무 키 입력 시 종료)
cv2.waitKey()

# 모든 OpenCV 창 닫기
cv2.destroyAllWindows()
