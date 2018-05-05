#coding=utf-8
from sklearn.ensemble import RandomForestClassifier


#学历 0:大专 2:硕士 1:本科
#有否相亲 0:N 1:Y
data_table = [["年龄", "身高", "年收入", '学历', '有否相亲'],
              [25, 179, 15, '大专', 'N'],
              [33, 190, 19, '大专', 'Y'],
              [28, 180, 18, '硕士', 'Y'],
              [25, 178, 18, '硕士', 'Y'],
              [46, 100, 100, '硕士', 'N'],
              [40, 170, 170, '本科', 'N'],
              [34, 174, 20, 'master', 'Y'],
              [36, 181, 55, '本科', 'N'],
              [35, 170, 25, 'master', 'Y'],
              [30, 180, 35, '本科', 'Y'],
              [28, 174, 30, '本科', 'N'],
              [29, 176, 36, '本科', 'Y'],
              ]
X = [
    [25, 179, 15, 0],
    [33, 190, 19, 0],
    [28, 180, 18, 2],
    [25, 178, 18, 2],
    [46, 100, 100, 2],
    [40, 170, 170, 1],
    [34, 174, 20, 2],
    [36, 181, 55, 1],
    [35, 170, 25, 2],
    [30, 180, 35, 1],
    [28, 174, 30, 1],
    [29, 176, 36, 1],
]
y = [0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1]
clf = RandomForestClassifier()
clf.fit(X, y)
p = [[28, 180, 18, 2]]
print clf.predict(p)
