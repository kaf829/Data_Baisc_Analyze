import cv2
import numpy as np

src = cv2.imread("./images/pencils.jpg")
number1 = np.ones_like(src) * 127
number2 = np.ones_like(src) * 2

add = cv2.add(src, number1)
sub = cv2.subtract(src, number1)
mul = cv2.multiply(src, number2)
div = cv2.divide(src, number2)

src = np.concatenate((src,src,src,src) , axis= 1)
number = np.concatenate((number1,number1,number1,number1), axis=1)
dst = np.concatenate((add,sub,mul,div), axis=1)


dst = np.concatenate((src, number, dst), axis = 0)
dst_re = cv2.resize(dst, dsize=(0,0), fx = 0.2 , fy = 0.2, interpolation=cv2.INTER_LINEAR)
cv2.imshow("dst", dst_re)
cv2.waitKey(0)
cv2.destroyAllWindows()
