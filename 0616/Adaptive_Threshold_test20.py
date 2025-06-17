import cv2  # OpenCV 라이브러리 (이미지 처리용)
import matplotlib.pyplot as plt  # Matplotlib 라이브러리 (이미지 시각화용)

# 📌 적응형 임계값에서 사용할 파라미터
blk_size = 9  # 블록 크기 (9x9 크기의 영역에서 임계값 계산)
C = 5         # 블록 평균 또는 가우시안에서 빼는 상수 (더 작게 조정)

# 📌 그레이스케일 이미지 읽기
img = cv2.imread('images/sudoku.jpg', cv2.IMREAD_GRAYSCALE)
# 'sudoku.jpg' 이미지를 그레이스케일로 읽음

# 📌 Otsu's method: 글로벌(전체 이미지 기준) 임계값 자동 계산 + 이진화
ret, th1 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# ret: Otsu가 찾은 최적 임계값
# th1: Otsu 이진화 결과

# 📌 적응형 이진화 (Mean 방식)
th2 = cv2.adaptiveThreshold(
    img, 255,
    cv2.ADAPTIVE_THRESH_MEAN_C,  # 블록 내 평균을 기준으로 임계값 계산
    cv2.THRESH_BINARY,           # 임계값 초과 → 255, 이하 → 0
    blk_size, C                  # 블록 크기와 C 상수
)

# 📌 적응형 이진화 (Gaussian 방식)
th3 = cv2.adaptiveThreshold(
    img, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,  # 블록 내 가우시안 가중치를 적용한 평균으로 임계값 계산
    cv2.THRESH_BINARY,               # 임계값 초과 → 255, 이하 → 0
    blk_size, C                      # 블록 크기와 C 상수
)

# 📌 출력용 이미지 딕셔너리 (제목: 이미지)
imgs = {
    'Original': img,                              # 원본 이미지
    "Golobal_Otsu:%d" % ret: th1,                 # Otsu 이진화 이미지
    "Adapted_Mean": th2,                          # Mean 적응형 이진화 이미지
    "Adated_Gaussian": th3                        # Gaussian 적응형 이진화 이미지
}

# 📌 subplot 으로 이미지 출력
for i, (k, v) in enumerate(imgs.items()):
    plt.subplot(2, 2, i + 1)    # 2행 2열 subplot, i+1 번째 위치
    plt.title(k)                # 제목 표시
    plt.imshow(v, 'gray')       # 그레이스케일로 출력
    plt.xticks([])              # x축 눈금 제거
    plt.yticks([])              # y축 눈금 제거

# 📌 최종 출력
plt.show()
