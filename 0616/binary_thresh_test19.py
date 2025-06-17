import cv2  # OpenCV 라이브러리: 이미지 처리 기능 제공
import matplotlib.pyplot as plt  # matplotlib: 이미지 시각화용 라이브러리

# 📌 1. 이미지를 그레이스케일로 읽기
img = cv2.imread("images/scaned_paper.jpg", cv2.IMREAD_GRAYSCALE)
# 파일 'scaned_paper.jpg' 를 흑백(그레이스케일) 이미지로 읽어옴

# 📌 2. 임계값 130을 기준으로 이진화 (thresholding)
_, t_130 = cv2.threshold(img, 130, 255, cv2.THRESH_BINARY)
# 픽셀 값 > 130 → 255 (흰색)
# 픽셀 값 <= 130 → 0 (검정)
# _ : threshold 값 (130 그대로 반환, 사용 안 함)
# t_130 : 이진화된 결과 이미지

# 📌 3. Otsu's method로 자동 임계값 계산 + 이진화
t, t_otsu = cv2.threshold(img, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# Otsu 알고리즘이 최적 threshold 값을 자동 계산
# t : Otsu가 찾아낸 최적 임계값
# t_otsu : Otsu 방법으로 이진화된 결과 이미지

# 📌 4. Otsu가 계산한 임계값 출력
print('otsu threshold', t)
# 콘솔에 최적 threshold 값 출력 (예: otsu threshold 127.0)

# 📌 5. 이미지 딕셔너리 생성 (제목: 이미지)
imgs = {
    'Orginal': img,  # 원본 그레이스케일 이미지
    't: 130': t_130,  # 임계값 130 이진화 이미지
    'otsu: %d' % t: t_otsu  # Otsu threshold 값 + Otsu 이진화 이미지
}

# 📌 6. 출력용 figure 생성 (크기 지정)
plt.figure(figsize=(12, 5))
# 출력 이미지 크기를 12x5 인치로 설정

# 📌 7. 이미지들을 하나씩 subplot에 출력
for i, (key, value) in enumerate(imgs.items()):
    # imgs 딕셔너리를 순회 (key: 제목, value: 이미지)

    plt.subplot(1, 3, i + 1)
    # 1행 3열 subplot 중 i+1 번째 위치에 그리기

    plt.title(key)
    # 제목 설정 (Orginal, t: 130, otsu: xxx)

    plt.imshow(value, cmap='gray')
    # 그레이스케일 컬러맵으로 이미지 출력

    plt.xticks([])
    plt.yticks([])
    # x, y 축 눈금 제거 (깔끔한 이미지 출력)

# 📌 8. 화면에 이미지 출력
plt.show()
# 전체 subplot 출력
