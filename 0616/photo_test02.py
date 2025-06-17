import cv2  # OpenCV 라이브러리 불러오기 (영상 처리, 카메라 제어 기능 제공)

# 📌 1. 카메라 장치 열기 (0번은 기본 연결된 카메라를 의미)
cap = cv2.VideoCapture(0)

# 📌 2. 카메라가 정상적으로 열렸는지 확인
if cap.isOpened():
    # 카메라가 열렸으면 루프 시작
    while True:
        ret, frame = cap.read()
        # 카메라에서 프레임을 읽어옴
        # ret: 프레임 읽기 성공 여부 (True / False)
        # frame: 읽어온 프레임 (이미지 데이터)

        if ret:
            # 프레임을 성공적으로 읽었다면 화면에 출력
            cv2.imshow('camera', frame)

            # 1ms 동안 키보드 입력을 기다림
            if cv2.waitKey(1) != -1:
                # 키보드 입력이 감지되면 (아무 키나 누르면)
                # 현재 프레임을 'images/photo.jpg' 파일로 저장
                cv2.imwrite('images/photo.jpg', frame)
                # 루프 종료
                break
        else:
            # 프레임을 읽지 못한 경우
            print('no Frame!')
            break
else:
    # 카메라가 열리지 않은 경우
    print("no camera")

# 📌 3. 자원 해제 및 창 닫기
cap.release()  # 카메라 장치 해제
cv2.destroyAllWindows()  # 생성된 모든 OpenCV 윈도우 닫기
