import cv2
import numpy as np

# 📌 YOLO 네트워크 불러오기: 학습된 가중치와 네트워크 구조
YOLO_net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")

# 📌 클래스 이름 읽기 (예: person, dog, car 등)
classes = []
with open("yolo.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]  # 각 줄의 클래스명 읽어 리스트로 저장

# 📌 YOLO의 레이어 이름과 출력 레이어 가져오기
layer_names = YOLO_net.getLayerNames()  # 전체 레이어 이름 리스트
# 출력 레이어만 추출 (YOLO는 마지막 3개 레이어에서 결과 출력)
output_layers = [layer_names[i - 1] for i in YOLO_net.getUnconnectedOutLayers().flatten()]

print("********************************")
print(output_layers)  # 출력 레이어 이름 출력 (디버그용)
print("********************************")

# 📌 클래스별 색상 지정 (랜덤 색상)
colors = np.random.uniform(0, 255, size=(len(classes), 3))

# 📌 입력 이미지 읽기
img = cv2.imread("yolo_dog.png")
# (fx=1, fy=1은 크기 변화 없음 — 이 줄은 사실상 의미 없음)
img = cv2.resize(img, None, fx=1, fy=1)
height, width, channels = img.shape  # 이미지 크기 정보

# 📌 YOLO 입력용 blob 생성 (이미지 크기 416x416, 스케일링 0.00392, BGR->RGB 변환, 크롭 X) sclaefactor는 0부터 1까지 넣고 각 픽셀에 대해 곱한값
blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), swapRB=True, crop=False)

# 📌 blob을 네트워크 입력으로 설정
YOLO_net.setInput(blob)

# 📌 네트워크 순방향 실행 (추론) → output_layers 에 해당하는 출력값 가져옴
outs = YOLO_net.forward(output_layers)

# 📌 탐지 결과 저장용 리스트
class_ids = []     # 탐지된 객체의 클래스 ID
confidences = []   # 탐지된 객체의 confidence score
boxes = []         # 탐지된 객체의 바운딩 박스 [x, y, w, h]

# 📌 YOLO 출력 결과 해석
for out in outs:  # 여러 출력 레이어 순회
    for detection in out:  # 각 출력에서 detection 벡터 순회
        score = detection[5:]  # detection[0:4] = box, detection[5:] = class score
        class_id = np.argmax(score)  # 가장 높은 class score의 인덱스 (클래스 ID)
        confidence = score[class_id]  # 해당 클래스의 confidence 값

        # confidence가 0.5 이상일 때만 박스 처리
        if confidence > 0.5:
            # YOLO 출력은 비율 값이므로 실제 이미지 크기로 변환
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)

            # 바운딩 박스 좌상단 좌표 계산
            x = int(center_x - w / 2)
            y = int(center_y - h / 2)

            # 리스트에 값 추가
            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)

# 📌 NMS (Non-Maximum Suppression)로 중복 박스 제거 (겹치는 박스 중 가장 좋은 것만 남김)
indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

font = cv2.FONT_HERSHEY_PLAIN  # 텍스트 폰트

# 📌 NMS로 남은 박스만 시각화
for i in range(len(boxes)):
    # ⚠ 여기선 NMS 적용 안 된 모든 박스를 그림 (원래는 indices 기반으로 그려야 함)
    # indices 기반으로 그리면:
    # for i in indices.flatten():
    if i in indices:
        x, y, w, h = boxes[i]
        label = str(classes[class_ids[i]])  # 클래스명
        color = colors[i % len(colors)]  # 색상 (colors 배열 범위 초과 방지)

        # 바운딩 박스 그리기
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)

        # 클래스명 + confidence 표시
        cv2.putText(img, label, (x, y - 10), font, 3, color, 3)

# 📌 최종 이미지 출력
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
