import cv2  # OpenCV 라이브러리 (영상 처리 및 입출력 기능 제공)
import matplotlib.pyplot as plt  # Matplotlib 라이브러리 (이미지 시각화용)

# 📌 이미지 출력 함수 (Matplotlib 사용)
def img_show(title='image', img=None, figsize=(8, 5)):
    plt.figure(figsize=figsize)  # 출력 크기 설정

    # title이 리스트면 그대로 titles로 사용, 아니면 동일한 제목을 리스트로 생성
    if type(title) == list:
        titles = title
    else:
        titles = []
        for i in range(len(img)):
            titles.append(title)

    # 이미지 개수만큼 반복
    for i in range(len(img)):
        # 흑백 이미지일 경우 RGB로 변환
        if len(img[i].shape) <= 2:
            #이미지 색상 공간을 변환하는데 사용
            #src: 입력이미지
            #code: 변환하려는 색상 공간을 지정하는 플래그
            #dst: 출력
            rgbImg = cv2.cvtColor(img[i], cv2.COLOR_GRAY2RGB)
        else:
            # 컬러(BGR) 이미지를 RGB로 변환 (Matplotlib은 RGB 포맷 사용)
            rgbImg = cv2.cvtColor(img[i], cv2.COLOR_BGR2RGB)

        # 서브플롯으로 이미지 출력
        plt.subplot(1, len(img), i + 1)  # 한 행에 여러 이미지 출력
        plt.imshow(rgbImg)               # 변환된 이미지 출력
        plt.title(titles[i])             # 제목 표시
        plt.xticks([]), plt.yticks([])   # 축 눈금 제거

    plt.show()  # 이미지 표시

# 📌 원본 이미지 파일 읽기
src = cv2.imread("./images/cat.jpg", cv2.IMREAD_COLOR)  # 컬러 이미지로 읽기

# 이미지의 세로 크기(height), 가로 크기(width), 채널 수(channel) 가져오기
height, width, channel = src.shape

# 중심 (width/2, height/2)를 기준으로 90도 회전, 크기(scale)는 1배
matrix = cv2.getRotationMatrix2D((width / 2, height / 2), 90, 1)

# 크기 (width, height)로 출력 이미지의 크기를 지정 warpAffined 얘가 실제로 변환시키는 함수
dst = cv2.warpAffine(src, matrix, (width, height))

cv2.imshow('src', src)  # 원본 이미지 창
cv2.imshow('dst', dst)  # 회전된 이미지 창

img_show(['Original', 'rotate_90'], [src, dst])

# 키 입력 대기 (아무 키나 누를 때까지)
cv2.waitKey()

# 모든 OpenCV 창 닫기
cv2.destroyAllWindows()
