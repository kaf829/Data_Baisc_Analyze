import cv2
import numpy as np

# 이미지 로드 (BGR 컬러 이미지)
img = cv2.imread("./images/coffee.jpg")

# 이미지 그레이스케일 변환 (BGRA -> GRAY로 되어 있지만 보통 BGR로 변환해도 됨)
gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
print(gray.shape)  # 그레이 이미지 크기 출력

# Harris 코너 검출 (블록 크기: 2, 소벨 커널: 3, harris 계수: 0.04)
corner = cv2.cornerHarris(gray, 2, 3, 0.04)
print(corner.shape)  # 코너 응답값 맵 크기 출력

# 코너 강도가 전체 max의 10% 이상인 좌표 찾기
coord = np.where(corner > 0.1 * corner.max())
print(len(coord))  # 반환된 좌표 배열 개수 출력
print(coord)       # 좌표 데이터 출력

# (x, y) 형태로 좌표 스택 (np.where은 (y, x) 순서이므로 순서 변환)
coord = np.stack((coord[1], coord[0]), axis=1)
print(coord)  # (x, y) 형태 좌표 출력

# 검출된 좌표에 빨간색 원 표시
for x, y in coord:
    cv2.circle(img, (x, y), 5, (0, 0, 255), 1, cv2.LINE_AA)

# 코너 응답 맵을 0~255 범위로 정규화 후 8비트 변환
corner_norm = cv2.normalize(corner, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

# 그레이 corner_norm을 BGR로 변환 (이미지 병합 위해)
corner_norm = cv2.cvtColor(corner_norm, cv2.COLOR_GRAY2BGR)

# 코너 맵과 코너 표시된 원본 이미지 병합 (수평 결합)
merged = np.hstack((corner_norm, img))

# 병합된 이미지를 30% 크기로 축소
merged_re = cv2.resize(merged, dsize=(0, 0), fx=0.3, fy=0.3, interpolation=cv2.INTER_LINEAR)

# 결과 이미지 출력
cv2.imshow("Harris Corner", merged_re)

# 키 입력 대기 후 창 닫기
cv2.waitKey()
cv2.destroyAllWindows()
