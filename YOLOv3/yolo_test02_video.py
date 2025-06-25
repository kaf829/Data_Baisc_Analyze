import cv2
import numpy as np

# 📌 영상 파일 열기
VideoSignal = cv2.VideoCapture(0)

# 📌 YOLOv3 가중치와 설정 파일 로드
YOLO_net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")

# 📌 클래스 이름 (예: person, car 등) 로드
classes = []
with open("yolo.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# 📌 YOLO 네트워크 레이어 이름 가져오기
layer_names = YOLO_net.getLayerNames()

# 📌 출력 레이어 이름 추출 (YOLO는 마지막 3개 레이어에서 출력 발생)
output_layers = [layer_names[i - 1] for i in YOLO_net.getUnconnectedOutLayers().flatten()]
print(output_layers)

# 📌 클래스별로 랜덤 색상 지정 (박스 색)
colors = np.random.uniform(0, 255, size=(len(classes), 3))

while True:
    # 📌 비디오 프레임 읽기
    ret, frame = VideoSignal.read()
    if not ret:
        break  # 영상 끝나면 종료

    # 📌 현재 프레임 크기 가져오기
    h, w, c = frame.shape

    # 📌 YOLO 입력용 blob 생성
    # 스케일 0.00392, 크기 416x416, BGR -> RGB 변환 (swapRB=True), crop X
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

    # 📌 YOLO 네트워크에 입력 데이터 설정
    YOLO_net.setInput(blob)

    # 📌 순방향 실행 → 출력 레이어에서 결과 추출
    outs = YOLO_net.forward(output_layers)

    # 📌 탐지 결과 초기화
    class_ids = []  # 클래스 ID 리스트
    confidences = []  # confidence score 리스트
    boxes = []  # 바운딩 박스 좌표 리스트

    # 📌 YOLO 출력 결과 해석
    for out in outs:
        for detection in out:
            score = detection[5:]  # 클래스별 확률 score 추출
            class_id = np.argmax(score)  # 가장 높은 확률의 클래스 ID
            confidence = score[class_id]  # 그 클래스의 확률 값
            if confidence > 0.5:  # confidence 임계값 이상일 때만 사용
                center_x = int(detection[0] * w)  # 중심 x 좌표 (이미지 크기 반영)
                center_y = int(detection[1] * h)  # 중심 y 좌표
                box_w = int(detection[2] * w)  # 박스 너비
                box_h = int(detection[3] * h)  # 박스 높이
                x = int(center_x - box_w / 2)  # 좌상단 x 좌표
                y = int(center_y - box_h / 2)  # 좌상단 y 좌표

                # 결과 저장
                boxes.append([x, y, box_w, box_h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # 📌 NMS (Non-Maximum Suppression)로 중복 박스 제거
    # confidence 0.5 이상, IoU 0.4 이상인 중복 박스 제거
    indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    font = cv2.FONT_HERSHEY_PLAIN  # 텍스트 폰트 지정

    # 📌 NMS 적용된 박스만 그리기
    for i in range(len(boxes)):
        if i in indices:  # NMS에서 선택된 박스만 처리
            x, y, w_box, h_box = boxes[i]
            label = str(classes[class_ids[i]])  # 클래스명
            color = colors[class_ids[i]]  # 클래스별 색상
            # 바운딩 박스 그리기
            cv2.rectangle(frame, (x, y), (x + w_box, y + h_box), color, 2)
            # 클래스명 + confidence 표시
            cv2.putText(frame, label, (x, y - 20), font, 0.5, color, 1)

    # 📌 탐지 결과 프레임 출력
    cv2.imshow("YOLO Video Detection", frame)

    # 📌 100ms 간 대기, 키 입력 시 루프 종료
    if cv2.waitKey(100) > 0:
        break

# 📌 자원 해제
VideoSignal.release()
cv2.destroyAllWindows()
