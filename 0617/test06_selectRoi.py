import cv2

# 이미지 파일을 읽어옴 (컬러로 읽기)
img = cv2.imread('./images/sunset.jpg')

# ROI(Region of Interest)를 마우스로 선택 (창 이름: 'img', 두 번째 인자: 이미지, 세 번째 인자: 크기 고정 여부 False)
# x, y: ROI의 좌상단 좌표, w: 너비, h: 높이
x, y, w, h = cv2.selectROI('img', img, False)
print(x, y, w, h)  # 선택한 ROI의 좌표와 크기 출력

# 만약 선택된 ROI의 너비와 높이가 0이 아니면 (즉, 영역이 정상적으로 선택됐으면)
if w and h:
    # 이미지에서 ROI 부분만 잘라냄 (y: y+h, x: x+w)
    roi = img[y:y+h, x:x+w]

    # 잘라낸 ROI를 새 창에 표시
    cv2.imshow('cropped', roi)

    # 'cropped' 창을 화면 좌상단 (0,0) 위치로 이동
    cv2.moveWindow('cropped', 0, 0)

    # 잘라낸 ROI 이미지를 파일로 저장
    cv2.imwrite('./cropped2.jpg', roi)

# 키보드 입력 대기 (키 값 반환)
key = cv2.waitKey()
print(key)  # 눌린 키의 코드 출력

# 모든 OpenCV 창 닫기
cv2.destroyAllWindows()
