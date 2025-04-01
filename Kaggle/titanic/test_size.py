from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

test_sizes = [0.1 , 0.2 , 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
for test_size in test_sizes:
    train = pd.read_csv("./data/train.csv")
    train["Sex"].dropna(inplace=True)
    train["Sex"].value_counts()
    li = LabelEncoder()
    x_dataset = li.fit_transform(train["Sex"])
    train["Survived"].dropna(inplace=True)
    train["Survived"].value_counts()
    x_train,x_test,y_train,y_test = train_test_split(x_dataset,train['Survived'],test_size=0.1)
    rfc = RandomForestClassifier()
    x_train = np.array(x_train).reshape(-1,1)
    y_train = np.array(y_train).reshape(-1,1)
    x_test = np.array(x_test).reshape(-1,1)
    y_test = np.array(y_test).reshape(1,-1)
    rfc.fit(x_train,y_train)
    print("train_dataset")
    print(rfc.score(x_train,y_train))
    print("test_dataset")
    print(rfc.score(x_test,y_test))
    real_test = pd.read_csv("./data/test.csv")
    real_x = real_test['Sex'].copy()
    PassengerId = real_test["PassengerId"]
    x_test = li.fit_transform(real_x)
    x_test = np.array(x_test).reshape(-1,1)
    result = rfc.predict(x_test)
    result = result.tolist()
    result_pd = pd.DataFrame(result, columns=["Survived"], index=None)
    result_pd_pd = pd.DataFrame(result, columns=["PassengerId"], index=None)
    result_pd = pd.concat([PassengerId, result_pd], axis=1)

    result_pd.to_csv(f"test_size_{test_size}_result.csv", index=False)