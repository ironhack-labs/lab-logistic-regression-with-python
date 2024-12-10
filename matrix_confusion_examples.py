from sklearn.metrics import confusion_matrix
y_true = ["cat", "ant", "cat", "cat", "ant", "bird"]
y_pred = ["ant", "ant", "cat", "cat", "ant", "cat"]
confusion_matrix(y_true, y_pred, labels=["ant", "bird", "cat"])
print(confusion_matrix)

#Answer
"""
array([[2, 0, 0],
       [0, 0, 1],
       [1, 0, 2]])

"""