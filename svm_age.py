# encoding=utf-8
from sklearn import svm

X = [[34], [33], [32], [31], [30], [30], [25], [22], [18]]
y = [1, 0, 0, 1, 1, 0, 1, 0, 1]

clf=svm.SVC(kernel="rbf").fit(X, y)

p = [[32.5]]
print(clf.predict([[35]]))