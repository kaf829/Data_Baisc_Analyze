import cv2  # OpenCV 라이브러리 불러오기 (영상 처리용)

# 📌 1. 원본 이미지 읽기 (컬러 모드)
src = cv2.imread("./images/cat.jpg", cv2.IMREAD_COLOR)
# "./images/cat.jpg" 파일을 컬러(BGR) 이미지로 읽어옴

# 📌 2. 블러(GaussianBlur파라미터) 적용
# ==============GaussianBlur파라미터 설명=====================
# src: 입력 이미지 (그레이스케일 또는 컬러 BGR 이미지)
# ksize: 커널 크기 (width, height) 튜플
#        - 반드시 홀수여야 함 (예: (3,3), (5,5), (7,7))
#        - 커널 크기가 클수록 블러 효과가 강해짐
# sigmaX: X축(가로) 방향의 가우시안 표준편차 (흐림 강도)
#        - 0이면 OpenCV가 ksize 기반으로 자동 계산
# sigmaY: Y축(세로) 방향의 표준편차 (기본값 = sigmaX)
#        - None 또는 0이면 sigmaX 값과 동일
# borderType: 경계 처리 방법 (기본값: cv2.BORDER_DEFAULT)
#        - cv2.BORDER_CONSTANT: 경계를 일정 상수 값으로 채움
#        - cv2.BORDER_REPLICATE: 경계 픽셀을 반복
#        - cv2.BORDER_REFLECT: 경계 픽셀을 반사
#        - cv2.BORDER_REFLECT_101: 경계 제외 반사
#        - cv2.BORDER_DEFAULT: OpenCV 기본값 (BORDER_REFLECT_101)
#=========================================================
dst = cv2.GaussianBlur(
    src,               # 입력 이미지
    (9, 9),            # 커널 크기 (9x9 크기의 윈도우로 평균값 계산)
    0
)
# 각 픽셀 주변 9x9 영역의 평균값으로 해당 픽셀을 대체하여 블러 효과 생성

# 📌 3. 원본 이미지 출력
cv2.imshow("src", src)

# 📌 4. 블러 처리된 이미지 출력
cv2.imshow("dst", dst)

# 📌 5. 키 입력 대기 (아무 키 입력 시 창 닫기)
cv2.waitKey()

# 📌 6. 모든 OpenCV 창 닫기
cv2.destroyAllWindows()
