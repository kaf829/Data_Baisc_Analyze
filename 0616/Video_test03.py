import cv2  # OpenCV 라이브러리 불러오기 (영상 처리 및 카메라 제어용)

# 📌 1. 카메라 장치 열기 (0은 기본 카메라를 의미)
cap = cv2.VideoCapture(0)

# 📌 2. 카메라가 정상적으로 열렸는지 확인
if cap.isOpened():
    # 영상 파일을 저장할 경로와 이름
    file_path = 'images/record.avi'

    # 영상 저장용 FPS 설정 (초당 30 프레임)
    fps = 30.0

    # 영상 파일 코덱 지정 (DIVX: MPEG-4 기반 코덱)
    # 'DIVX' 코덱을 사용하여 압축 포맷 지정
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')

    # 카메라에서 가져오는 영상의 가로 크기
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

    # 카메라에서 가져오는 영상의 세로 크기
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

    # 영상 크기를 정수형 튜플로 지정
    size = (int(width), int(height))

    # VideoWriter 객체 생성 (지정한 파일명, 코덱, FPS, 크기)
    out = cv2.VideoWriter(file_path, fourcc, fps, size)

    # 📌 3. 영상 캡처 루프
    while True:
        # 카메라에서 한 프레임 읽기
        ret, frame = cap.read()

        if ret:
            # 프레임을 정상적으로 읽었다면 화면에 출력
            cv2.imshow('camera-recording', frame)

            # 읽은 프레임을 파일로 저장
            out.write(frame)

            # 1/FPS 시간 동안 키 입력 대기 (30 FPS면 약 33ms)
            if cv2.waitKey(int(1000 / fps)) != -1:
                # 아무 키나 눌리면 루프 종료
                break
        else:
            # 프레임 읽기에 실패하면 에러 출력하고 루프 종료
            print("no frame!")
            break

    # 📌 4. VideoWriter 자원 해제
    out.release()

else:
    # 카메라 열기에 실패하면 메시지 출력
    print("cann't open Camera")

# 📌 5. 카메라 장치 해제
cap.release()

# 📌 6. OpenCV에서 열린 모든 창 닫기
cv2.destroyAllWindows()
