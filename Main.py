import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Load the dataset
data = pd.read_csv(r'C:\Users\Dell\OneDrive\Desktop\Data_science\Advanced EDA & Feature Engineering\Titanic-Dataset.csv')
print("Dataset loaded successfully!")

#displaying the first  rows in the dataset
print(data.head(10))

#to check number of column and row in the dataset
print(data.shape)

#for column names in the dataset
print(data.columns)

 #to display the information about the dataset
print(data.info())

#statistical summary of the dataset
print(data.describe())

#to display the data types of each column in the dataset
print(data.dtypes)

#to check any missing values in the dataset
print(data.isnull().sum())

#to check any duplicate values in the dataset
print(data.duplicated().sum())

#filling missing values in the age column with the mean value of the column
data["Age"] = data["Age"].fillna(data["Age"].median())

#filling missing value in the embarked column with the mode value of the column
data["Embarked"] = data["Embarked"].fillna(data["Embarked"].mode()[0])

#to drop the cabin column as it has too many missing values
data.drop('Cabin', axis=1, inplace=True)

print("\n Missing values after handling : ")
print(data.isnull().sum())

#create a boxplot for numerical columns 
numercial_columns = ["Age","Fare","SibSp","Parch"]

for column in numercial_columns:
    plt.figure(figsize=(10,5))
    sns.boxplot(x=data[column])
    plt.title(f'Boxplot of {column}')
    plt.show()

#define the functions
def detect_outliers_iqr(column):
    Q1 = column.quantile(0.25)
    Q3 = column.quantile(0.75)

    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = column[(column < lower_bound)| (column > upper_bound)]

    print(f'{column}: {len(outliers)}')

#calling function here
detect_outliers_iqr(data["Age"])
detect_outliers_iqr(data["Fare"])
detect_outliers_iqr(data["SibSp"])
detect_outliers_iqr(data["Parch"])

#to remove fare outliers from the dataset
Q1  = data["Fare"].quantile(0.25)
Q3 = data["Fare"].quantile(0.75)

IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

data = data[
    (data["Fare"] >= lower_bound) &
    (data["Fare"] <= upper_bound)
]

print("\n Missing values after handling : ")
print(data.isnull().sum())

#verify with another boxplot
plt.figure(figsize=(10,5))
sns.boxplot(x=data["Fare"])
plt.title("Fare After Outlier Removed")
plt.show()

#feature 1 : familySize
#total  family members  traveling with the passenger
#+1 is added to unclude the passenger himself/herself
data["FamilySize"] = data["SibSp"] + data["Parch"] + 1

#feature 2 : Isalone
#if Family size is 1 then the passenger is traveling alone
# 1 = alone, 0 =not alone
data["IsAlone"] = np.where(data["FamilySize"] == 1,1,0).astype(int)

#feature 3 :title
#extract title (Mr, Mrs, Miss, etc) from the name column
data["Title"] = data["Name"].str.extract(r'([A-Za-z])\.',expand=False)

print("\n ===== New Features ==== ")
print(data[["FamilySize","IsAlone","Title"]].head(10))

#to save the cleaned dataset in csv file
data.to_csv("cleaned_titanic_dataset.csv",index=False)
print("\n Cleaned dataset saved successfully")

#to view the final dataset
print("\n final dataset preview")
print(data.head())
print("\n Final Dataset shape : ")
print(data.shape)