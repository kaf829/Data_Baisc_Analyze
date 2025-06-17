import cv2

#자동차 번호판
img = cv2.imread('images/number.jpg', cv2.IMREAD_GRAYSCALE)

for t in range(50, 230, 10):
    _, bin_img = cv2.threshold(img, t, 255, cv2.THRESH_BINARY)
    cv2.imshow(f'Thresh {t}', bin_img)
    cv2.waitKey(1000)
cv2.destroyAllWindows()


#고양이
# img = cv2.imread('images/cat.jpg', cv2.IMREAD_GRAYSCALE)
#
# for t in range(50, 230, 10):
#     _, bin_img = cv2.threshold(img, t, 255, cv2.THRESH_BINARY)
#     cv2.imshow(f'Thresh {t}', bin_img)
#     cv2.waitKey(1000)
# cv2.destroyAllWindows()


# 신문
# img = cv2.imread('images/newspaper.jpg', cv2.IMREAD_GRAYSCALE)
#
# for t in range(50, 230, 10):
#     _, bin_img = cv2.threshold(img, t, 255, cv2.THRESH_BINARY)
#     cv2.imshow(f'Thresh {t}', bin_img)
#     cv2.waitKey(1000)
# cv2.destroyAllWindows()