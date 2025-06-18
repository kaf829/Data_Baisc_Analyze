import cv2

# 원본 이미지 읽기 (컬러 이미지)
src = cv2.imread("./images/convex.png")

# 출력용 이미지 복사본 생성 (src와 동일한 이미지로 초기화)
dst = src.copy()

# 원본 이미지를 그레이스케일로 변환
# convexHull, findContours 등은 그레이스케일 또는 이진 이미지에서 주로 처리
gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)

# 이진화 수행 (임계값: 150, 최대값: 255, 반전 이진화)
# gray > 150 -> 0, gray <= 150 -> 255
ret, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

# 이진화된 이미지에서 윤곽선 검출
# cv2.RETR_CCOMP: 외곽선 + 내부 윤곽선 계층 정보 생성
# cv2.CHAIN_APPROX_NONE: 윤곽선의 모든 점을 저장 (단순화하지 않음)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)

# 검출된 각 윤곽선에 대해
for i in contours:
    # 윤곽선의 convex hull (볼록 껍질) 계산
    # clockwise=True: 볼록 껍질의 점이 시계 방향으로 정렬됨
    hull = cv2.convexHull(i, clockwise=True)

    # 볼록 껍질을 dst 이미지 위에 빨간색 선 (두께 2)으로 그림
    # [hull]: drawContours는 리스트 형태로 contour 전달
    # 0: 전달된 리스트 중 첫번째 contour 사용
    cv2.drawContours(dst, [hull], 0, (0, 0, 255), 2)

# 결과 이미지 창에 출력
cv2.imshow('dst', dst)

# 키 입력 대기 (아무 키나 누르면 종료)
cv2.waitKey(0)

# 모든 창 닫기
cv2.destroyAllWindows()
