import cv2  # OpenCV 라이브러리 불러오기 (영상 처리 및 캡처 기능 제공)
import datetime  # 날짜 및 시간 처리를 위한 datetime 모듈

# 📌 1. 비디오 파일 열기
capture = cv2.VideoCapture("images/youquiz4.mp4")

# 📌 2. 영상 저장을 위한 코덱 설정 (XVID: 널리 호환되는 MPEG-4 계열 코덱)
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# 📌 3. 녹화 상태 플래그 (False: 녹화 중 아님, True: 녹화 중)
record = False

# 📌 4. 프레임을 반복적으로 읽으며 영상 재생 루프
while True:
    # 현재 재생 위치가 마지막 프레임이면 처음으로 되감기
    if capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT):
        capture.open('./images/youquiz4.mp4')

    # 비디오에서 프레임을 읽어오기
    ret, frame = capture.read()

    if not ret:
        # 프레임을 읽지 못했으면 메시지 출력 후 루프 종료
        print("프레임 읽기 실패")
        break

    # 프레임을 윈도우에 출력
    cv2.imshow("VideoFrame", frame)

    # 현재 시간 문자열 생성 (파일명에 사용)
    now = datetime.datetime.now().strftime("%d_%H-%M-%S")

    # 33ms 동안 키 입력 대기 (약 30 FPS 재생 속도)
    key = cv2.waitKey(33)
    print("Key => ", key)  # 입력된 키 값 출력

    # ESC 키(27) 입력 시 루프 종료
    if key == 27:
        break
    # '1' 키 (ASCII 코드 49) 입력 시 화면 캡처
    elif key == 49:
        print("캡처")
        cv2.imwrite("./capture/" + str(now) + ".png", frame)
    # '2' 키 (ASCII 코드 50) 입력 시 녹화 시작
    elif key == 50:
        if not record:
            print("녹화시작")
            record = True
            # VideoWriter 객체 생성 (저장 경로, 코덱, FPS, 프레임 크기)
            video = cv2.VideoWriter(
                "./capture/" + str(now) + ".avi",
                fourcc,
                20.0,
                (frame.shape[1], frame.shape[0])  # (width, height)
            )
    # '3' 키 (ASCII 코드 51) 입력 시 녹화 중지
    elif key == 51:
        if record:
            print("녹화중지")
            record = False
            video.release()  # VideoWriter 자원 해제

    # 녹화 중일 때 프레임을 파일에 저장
    if record:
        print("녹화중")
        video.write(frame)

# 📌 5. 루프 종료 시 자원 해제
capture.release()  # 비디오 파일 닫기
cv2.destroyAllWindows()  # 모든 OpenCV 창 닫기
