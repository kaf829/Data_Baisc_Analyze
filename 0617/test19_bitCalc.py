import numpy as np
import cv2

# 📌 이미지 파일을 컬러(BGR)로 읽어옴
src = cv2.imread('./images/analysis.jpg')

# 📌 컬러 이미지를 그레이스케일(흑백)로 변환
# 컬러(BGR) -> 단일 채널(gray) : 밝기 정보만 유지
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# 📌 그레이스케일 이미지를 이진화 (threshold 적용)
# 픽셀 값이 127 이상이면 255(흰색), 이하면 0(검정)으로 변환
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# 📌 gray와 binary의 비트 AND 연산
# 두 이미지 픽셀 값이 둘 다 0이 아니면 해당 위치 값 유지, 아니면 0
_and = cv2.bitwise_and(gray, binary)

# 📌 gray와 binary의 비트 OR 연산
# 두 이미지 중 하나라도 0이 아니면 해당 위치 값 유지
_or = cv2.bitwise_or(gray, binary)

# 📌 gray와 binary의 비트 XOR 연산
# 두 이미지 픽셀 값이 서로 다르면 해당 위치 값 유지, 같으면 0
_xor = cv2.bitwise_xor(gray, binary)

# 📌 gray의 비트 NOT 연산 (반전)
# 0 → 255, 255 → 0 (흑백 반전)
_not = cv2.bitwise_not(gray)

# 📌 상단 row : (검은이미지 | gray | binary | 검은이미지)
# np.zeros_like(gray): gray와 같은 크기의 검은 이미지 생성
src_row = np.concatenate((np.zeros_like(gray), gray, binary, np.zeros_like(gray)), axis=1)

# 📌 하단 row : (AND | OR | XOR | NOT)
dst_row = np.concatenate((_and, _or, _xor, _not), axis=1)

# 📌 상단 row와 하단 row를 세로로 이어붙임
dst = np.concatenate((src_row, dst_row), axis=0)

# 📌 dst 전체 이미지를 0.2배 크기로 축소 (너무 크면 화면에 안 들어가기 때문에 축소)
dst_re = cv2.resize(dst, dsize=(0,0), fx=0.2, fy=0.2, interpolation=cv2.INTER_LINEAR)

# 📌 결과 이미지 출력
cv2.imshow("dst", dst_re)

# 📌 키보드 입력 기다림 (아무 키 누르면 종료)
cv2.waitKey(0)

# 📌 모든 OpenCV 창 닫기
cv2.destroyAllWindows()
