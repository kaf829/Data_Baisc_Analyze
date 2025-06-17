import cv2  # OpenCV 라이브러리 불러오기 (컴퓨터 비전 관련 기능 제공)

# 📌 1. 비디오 캡처 장치 열기 (여기서 0은 기본 연결된 카메라를 의미)
capture = cv2.VideoCapture(0)

# 📌 2. 캡처 해상도 설정 (프레임의 가로 크기 지정)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # 프레임 가로 크기를 640픽셀로 설정

# 📌 3. 캡처 해상도 설정 (프레임의 세로 크기 지정)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # 프레임 세로 크기를 480픽셀로 설정

# 📌 4. 루프를 돌며 프레임을 읽고 화면에 출력
while cv2.waitKey(33) < 0:
    # 33ms마다 키 입력을 기다림 (30 FPS 정도의 속도로 화면 갱신)
    # 아무 키가 눌리기 전까지 루프가 계속 실행됨

    ret, frame = capture.read()
    # 현재 카메라로부터 프레임을 읽어옴
    # ret: 프레임 읽기 성공 여부 (True / False)
    # frame: 읽어온 영상 (이미지 데이터)

    cv2.imshow("VideoFrame", frame)
    # 읽어온 프레임을 'VideoFrame'이라는 이름의 윈도우 창에 출력

# 📌 5. 루프가 끝나면 (키 입력 등으로 빠져나오면) 자원 해제
capture.release()
# 카메라 장치를 해제하여 다른 프로그램에서 카메라를 사용할 수 있도록 함

cv2.destroyAllWindows()
# 모든 OpenCV 윈도우 창을 닫음 (프로그램 종료 시 필요)
