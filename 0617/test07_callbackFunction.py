import cv2

# ROI 선택을 위한 상태 변수
isDragging = False  # 마우스 드래그 상태 여부
x0, y0, w, h = -1, -1, -1, -1  # ROI 좌표와 크기 초기화
blue, red = (255, 0, 0), (0, 0, 255)  # 사각형 색 (파랑, 빨강)

# 마우스 이벤트 콜백 함수
def onMouse(event, x, y, flags, params):
    global isDragging, x0, y0, img
    if event == cv2.EVENT_LBUTTONDOWN:
        # 마우스 왼쪽 버튼 클릭 시 드래그 시작
        isDragging = True
        x0 = x
        y0 = y

    elif event == cv2.EVENT_MOUSEMOVE:
        if isDragging:
            # 드래그 중일 때 사각형 그리며 시각적으로 표시
            img_draw = img.copy()
            cv2.rectangle(img_draw, (x0, y0), (x, y), blue, 2)
            cv2.imshow('img', img_draw)

    elif event == cv2.EVENT_LBUTTONUP:
        if isDragging:
            # 드래그 종료
            isDragging = False
            w = x - x0
            h = y - y0
            print(f"x:{x0} , y:{y0}, w : {w}, h :{h}")

            if w > 0 and h > 0:
                # 올바른 ROI (좌상단 -> 우하단)일 경우
                img_draw = img.copy()
                cv2.rectangle(img_draw, (x0, y0), (x, y), red, 2)
                cv2.imshow('img', img_draw)

                # ROI 추출
                roi = img[y0:y0 + h, x0:x0 + w]
                cv2.imshow('cropped', roi)
                cv2.moveWindow('cropped', 0, 0)
                cv2.imwrite('./images/cropped222.jpg', roi)
            else:
                # 잘못된 ROI (좌상단에서 우하단이 아닌 경우)
                cv2.imshow('img', img)
                print("좌측 상단에서 우측 하단으로 영역을 드래그 하세요")

# 이미지 읽기
img = cv2.imread("./images/sunset.jpg")

# 원본 이미지 표시
cv2.imshow('img', img)

# 'img' 창에서 마우스 콜백 설정
cv2.setMouseCallback('img', onMouse)

# 키 입력 대기
cv2.waitKey(0)

# 모든 창 닫기
cv2.destroyAllWindows()
