import cv2

# 비교 대상 도형 이미지 (타겟 도형)
target = cv2.imread("images/4star.jpg")
# 여러 도형이 있는 이미지
shapes = cv2.imread("images/shapestomatch.jpg")

# 타겟 이미지를 그레이스케일로 변환
targetGray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
# 비교 대상 이미지도 그레이스케일로 변환
shapeGray = cv2.cvtColor(shapes, cv2.COLOR_BGR2GRAY)

# 타겟 이미지 이진화 (127 임계값, 반전)
ret, targetTh = cv2.threshold(targetGray, 127, 255, cv2.THRESH_BINARY_INV)
# 비교 대상 이미지 이진화 (127 임계값, 반전)
ret, shapeTh = cv2.threshold(shapeGray, 127, 255, cv2.THRESH_BINARY_INV)

# 타겟 윤곽선 추출 (외곽선만)
cntrs_target, _ = cv2.findContours(targetTh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# 비교 대상 이미지 윤곽선 추출 (외곽선만)
cntrs_shape, _ = cv2.findContours(shapeTh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 매칭 결과를 저장할 리스트
matchs = []

# 비교 대상 윤곽선들과 타겟 윤곽선을 하나씩 매칭
for contr in cntrs_shape:
    # 타겟 윤곽선과 현재 윤곽선의 유사도 계산 (값이 작을수록 유사함)
    match = cv2.matchShapes(cntrs_target[0], contr, cv2.CONTOURS_MATCH_I2, 0.0)

    # 매칭 값과 해당 윤곽선 저장
    matchs.append((match, contr))

    # 매칭 점수를 이미지에 표시 (윤곽선 첫 좌표 위치)
    cv2.putText(shapes, '%.2f' % match, tuple(contr[0][0]), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 1)

# 매칭 점수 기준 오름차순 정렬 (가장 유사한 것이 첫 번째)
matchs.sort(key=lambda x: x[0])

# 가장 유사한 윤곽선을 초록색으로 그림
cv2.drawContours(shapes, [matchs[0][1]], -1, (0, 255, 0), 3)

# 타겟 이미지 표시
cv2.imshow('target', target)
# 매칭 결과 이미지 표시
cv2.imshow('shape', shapes)

# 키 입력 대기
cv2.waitKey()
# 모든 창 닫기
cv2.destroyAllWindows()
