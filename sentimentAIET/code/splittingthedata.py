from sklearn.model_selection import train_test_split
import pandas as pd

data=pd.read_csv(r"C:\Users\rctuh\Desktop\sentimentAIET\dataset\tweets_data.csv")
#split the data into train and test set

train,test = train_test_split(data, test_size=0.30, random_state=0)
#save the data
train.to_csv(r"C:\Users\rctuh\Desktop\sentimentAIET\dataset\train.csv",index=False)
test.to_csv(r"C:\Users\rctuh\Desktop\sentimentAIET\dataset\test.csv",index=False)
print("The dataset has been successfully splitted")