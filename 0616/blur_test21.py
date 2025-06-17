import cv2  # OpenCV 라이브러리 불러오기 (영상 처리용)

# 📌 1. 원본 이미지 읽기 (컬러 모드)
src = cv2.imread("./images/cat.jpg", cv2.IMREAD_COLOR)
# "./images/cat.jpg" 파일을 컬러(BGR) 이미지로 읽어옴

# 📌 2. 블러(평균값 필터) 적용
dst = cv2.blur(
    src,               # 입력 이미지
    (9, 9),            # 커널 크기 (9x9 크기의 윈도우로 평균값 계산)
    anchor=(-1, -1),   # 앵커 위치 (-1, -1은 커널 중심을 자동으로 선택)
    borderType=cv2.BORDER_DEFAULT  # 경계 픽셀 처리 방법 (기본값: 반사 또는 복제)
)
# 각 픽셀 주변 9x9 영역의 평균값으로 해당 픽셀을 대체하여 블러 효과 생성

dst2 = cv2.blur(
    src,               # 입력 이미지
    (3, 3),            # 커널 크기 (9x9 크기의 윈도우로 평균값 계산)
    anchor=(-1, -1),   # 앵커 위치 (-1, -1은 커널 중심을 자동으로 선택)
    borderType=cv2.BORDER_DEFAULT  # 경계 픽셀 처리 방법 (기본값: 반사 또는 복제)
)

# 📌 3. 원본 이미지 출력
cv2.imshow("src", src)

# 📌 4. 블러 처리된 이미지 출력
cv2.imshow("dst", dst)

cv2.imshow("dst2", dst2)

# 📌 5. 키 입력 대기 (아무 키 입력 시 창 닫기)
cv2.waitKey()

# 📌 6. 모든 OpenCV 창 닫기
cv2.destroyAllWindows()
