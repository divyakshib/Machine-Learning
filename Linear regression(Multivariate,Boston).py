from sklearn.model_selection import cross_val_score
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
boston=load_boston()
x=boston.data
y=boston.target
X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=0.1,random_state=1)
lr=LinearRegression(normalize=True)
lr.fit(X_train,Y_train)
print(lr.coef_)
print(lr.intercept_)
print(lr.score(X_train,Y_train))#accuracy
print(lr.score(X_test,Y_test))
scores=cross_val_score(lr,X_train,Y_train,cv=3)
print(scores.mean())