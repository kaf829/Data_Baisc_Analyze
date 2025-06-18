import cv2

src = cv2.imread("./images/tomato.jpg", cv2.IMREAD_COLOR)
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

# 빨강 범위
lower_red = cv2.inRange(hsv, (0, 100, 100), (5, 255, 255))
upper_red = cv2.inRange(hsv, (170, 100, 100), (179, 255, 255))

# 두 마스크 결합
added_red = cv2.addWeighted(lower_red, 1.0, upper_red, 1.0, 0.0)

# 빨강 부분 추출
red = cv2.bitwise_and(hsv, hsv, mask=added_red)

# HSV -> BGR 변환
red_bgr = cv2.cvtColor(red, cv2.COLOR_HSV2BGR)

# 크기 조정
red_bgr = cv2.resize(red_bgr, dsize=(0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
src = cv2.resize(src, dsize=(0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

# 출력
cv2.imshow("src", src)
cv2.imshow("red", red_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
