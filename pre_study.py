import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.metics import accuracy_score

A = np.array([[1,2,3,],[4,5,6]])
B = np.array([[7,8],[9,10],[11,12]])

dot_product = np.dot(A,B)
print(dot_product)

A = np.array([[1,2],[3,4]])
transpose_mat = np.transpose(A)
print(transpose_mat)


iris = load_iris()