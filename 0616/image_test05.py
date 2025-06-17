import cv2  # OpenCV 라이브러리 불러오기 (영상 처리 기능 제공)

# 📌 1. 비디오 파일 열기
capture = cv2.VideoCapture("images/youquiz4.mp4")

# 📌 2. 현재 프레임 번호 출력 (초기값: 0)
print(capture.get(cv2.CAP_PROP_POS_FRAMES))

# 📌 3. 전체 프레임 개수 출력
print(capture.get(cv2.CAP_PROP_FRAME_COUNT))

# 📌 4. 루프를 돌며 프레임 재생
while cv2.waitKey(33) < 0:
    # 약 30 FPS 속도로 프레임 재생 (33ms마다 키 입력을 확인)
    # 아무 키가 눌리면 루프 종료 (waitKey() >= 0)

    # 현재 재생 중인 프레임 위치가 마지막 프레임에 도달했는지 확인
    if capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT):
        # 마지막 프레임까지 재생되었으면 영상 처음으로 되감기
        capture.set(cv2.CAP_PROP_POS_FRAMES, 0)

    # 현재 프레임 읽기
    ret, frame = capture.read()

    if not ret:
        # 프레임을 읽지 못했을 경우 (파일 손상 or 끝)
        print("프레임을 읽을 수 없습니다.")
        break

    # 프레임을 화면에 출력
    cv2.imshow("wildlife", frame)

# 📌 5. 사용한 자원 해제
capture.release()  # 비디오 파일 닫기
cv2.destroyAllWindows()  # 생성된 모든 OpenCV 창 닫기
