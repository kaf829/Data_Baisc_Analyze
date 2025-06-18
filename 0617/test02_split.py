import cv2

src = cv2.imread("./images/tomato.jpg", cv2.IMREAD_COLOR)
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
print(hsv)
h, s, v = cv2.split(hsv)

src = cv2.resize(src, dsize=(0,0), fx = 0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
hsv = cv2.resize(hsv, dsize=(0,0), fx = 0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
h = cv2.resize(h, dsize=(0,0), fx = 0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
s = cv2.resize(s, dsize=(0,0), fx = 0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
v = cv2.resize(v, dsize=(0,0), fx = 0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

cv2.imshow("src",src)
cv2.imshow("hsv",hsv)
cv2.imshow("h",h)
cv2.imshow("s",s)
cv2.imshow("v",v)

cv2.waitKey()
cv2.destroyAllWindows()
