import cv2

src = cv2.imread("./images/bird.jpg", cv2.IMREAD_COLOR)
dst = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)

src = cv2.resize(src, None, fx =0.5, fy = 0.5, interpolation= cv2.INTER_AREA)
dst = cv2.resize(dst, None, fx =0.5, fy = 0.5, interpolation= cv2.INTER_AREA)


cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()