import cv2  # OpenCV 라이브러리 불러오기 (영상 처리용)

# 📌 1. 원본 이미지 읽기 (컬러 모드)
src = cv2.imread("./images/cat.jpg", cv2.IMREAD_COLOR)

for ksize in (3,5,7,11):
    dst  = cv2.GaussianBlur(src, (ksize,ksize), 0)
    desc = "Mean {}x{}".format(ksize,ksize)
    cv2.putText(dst,desc, (10,30),cv2.FONT_HERSHEY_SIMPLEX, 1.0,255,1, cv2.LINE_AA)
    cv2.imshow("dst",dst)
    cv2.waitKey()

cv2.destroyAllWindows()
