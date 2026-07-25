# Advanced-EDA-Feature-Engineering
An internship project at Decodelable

<br>
Project Overview <br>
This project focuses on performing Exploratory Data Analysis (EDA), Data Cleaning, Outlier Detection and Feature Engineering on the Titanic dataset.

The main goal is to understand the dataset, handle missing and inconsistent data, identify and remove outliners, and create meaning ful new features that can be used for further Machine Learning and Data Science tasks.
<br>
Objectives <br>
The main objectives of this project are : 
o Load and inspect the Titanic dataset.
o Understand the structure and characteristics of the data.
o Identify missing values.
o Handle missing values appropriately.
o check for duplicate records.
o Detect outlier using the IQR (Interquartile Range) method.
o Remove extreme outliers from the Fare column.
o Create new meaningful features.
o Save the cleaned dataset as a CSV.
<br>

Technologies and Libraries used <br>
The project is developed using Python.
<br>
Libraries <br>
o Pandas - Data manipulation and analysis
o NumPY - Numerical operation and feature creation
o Matplotlib - Data visualization
o Seaborn - Statistical visualization
<br>

Installation<br>
Install the required libraries using : <br>
pip install pandas numpy matplotlib seaborn
<br>
Dataset <br>
The project uses the Titanic Dataset, Which contains information about passengers who travelled on the Titanic.
<br>

Some important colimns include <br>
Column            Description<br>
PassengerId        Unique ID of each passenger <br>
Survived           Whether the passenger survived <br>
Pclass             Passenger class <br>
Name               Passenger's name <br>
sex                Gender of the passenger <br>
Age                Age of the passenger <br>
SibSp              Number of sibling/ spouses abord<br>
Parch              Number of parents/ children aboard <br>
Ticket             Ticket number <br>
Fare               Cabin number <br>
Embarked           Port where the passenger boarded <br>
<br>
Project workflow <br>
1. Load the Dataset <br>
The Titanic dataset is loaded using Pandas : <br>
After loading the dataset, the first 10 records are displayed to understand its structure.
<br>
<br>
2. Explore the Dataset <br>
Several Pandas function are used for initial exploration : <br>
data.head(10)<br>
data.shape <br>
data.columns <br>
data.info() <br>
data.describe() <br>
data.dtypes <br>
these help us understand : <br>
o Number of rows and columns <br>
o Column names <br>
o Data types <br>
o Statistical information <br>
o Overall structure of the dataset <br>
<br>
<br>
3. Check Missing Values <br>
Missing values are identified using : <br>
data.isnull().sum() <br>
the missing values were handled as follows : <br>
Age = missing values in Age are replaces with the median : <br>
data["Age"] = data["Age"].fillna(data["Age"].median())<br>
Meadian is used because it is less affected by extreme values than the mean.
<br>
Embarked =  missing values in embarked are replced with the mode : <br>
data["Embarked"] = data["Embarked"].fillna(data["Embarked"].mode()[0]) <br>
Cabin = the cabin column is removed because it contain a large number of missing values : <br>
data.drop("Cabin",axis = 1, inplace = True)
<br>
<br>
4. Check Duplicate Values <br>
Duplicate records are checked using : <br>
daata.duplicatee().sum()<br>
This helps ensure that duplicate rows do not affect the analysis. <br>
<br>
5. Outlier Detection <br>
Bosplots are creted for numerical columns such as : <br>
o Age <br>
o Fare <br>
o SibSp <br>
o Parch <br>

6. Detect Outliers Using IQR <br>
The Interquartile raange (IQR) method is used to detect ouliers . <br>
the foemula : <br>
IQR = Q3 - Q1 <br>
Lower Bound = Q1 - 1.5 * IQR <br>
Upper Bound = Q3 + 1.5 * IQR <br>
<br>
Afunction was created to identify the number of outliers :<br>
def detect_outlier_iqr(column) : <br>
  Q1 = column.quantile(0.25)
  Q3 = column.quantile(0.75)
  IQR = Q3-Q1
   lower_bound = Q1 - 1.5 * IQR <br>
   upper_bound = Q3 + 1.5 * IQR <br>

   outliers = column [
     (column < lower_bound) |
     (column > upper_bound)
   ]
   <br>
   print(f'{column} : {len(outliers)}')
   <br>
   The function is applied to  : <br>
   Age <br>
   Fare<br>
   SibSp<br>
   Parch<br>
   <br>

Remove Fare Outliers <br>
Afer detecting outliers, extreme values fro the Fare column are removed using the IQR <br>
Q1 = data["Fare"].quantile(0.25)<br>
Q3 = data["Fare"].quantile(0.75)<br>

IQR = Q3 - Q1<br>
lower_bound = Q1 - 1.5 * IQR <br>
upper_bound = Q3 + 1.5 * IQR <br>
data = data[ 
  (data["Fare"] >= lower_bound) & 
  (data["Fare"] <= upper_bound)
  ]<br>
  <br>

Feature Engineering <br>
Feature engineering is the process of creating new useful variables from existing data.<br>

Three new features were created.<br>
FamilySize <br>

FamilySize represents the total number of family members travelling with the passenger.<br>

data["FamilySize"] = data["SibSp"] + data["Parch"] + 1<br>

The +1 represents the passenger themselves.
<br>
IsAlone
<br>
The IsAlone feature identifies whether a passenger was travelling alone.
<br>
data["IsAlone"] = np.where(
    data["FamilySize"] == 1,
    1,
    0
).astype(int)
<br>
Interpretation:
<br>
1 → Passenger was travelling alone
0 → Passenger was not travelling alone
<br>
Title
<br>
The Title feature attempts to extract a passenger's title from their name.
<br>
Examples of titles include:
<br>
Mr
Mrs
Miss
Dr
<br>
The feature is created using:
<br>
data["Title"] = data["Name"].str.extract(
    r'([A-Za-z]+)\.',
    expand=False
)
<br>
<br>
Save the Cleaned Dataset
<br>
After cleaning and feature engineering, the final dataset is saved as:
<br>
data.to_csv(
    "cleaned_titanic_dataset.csv",
    index=False
)
<br>
The cleaned dataset can now be used for further analysis or machine learning.
<br>
Final Dataset
<br>
The final dataset contains the original useful features along with newly engineered features:
<br>
FamilySize<br>
IsAlone<br>
Title<br>
<br>
The final shape of the dataset is also displayed using:
<br>
print(data.shape)
<br>
<br>

Project Structure
<br>
A recommended project structure is:
<br>
Advanced EDA & Feature Engineering/
│
├── Titanic-Dataset.csv
├── main.py
├── cleaned_titanic_dataset.csv
└── README.md
<br>
<br>

How to Run the Project
<br>
1. Clone or download the project<br>

Place the project folder on your computer.<br>
2. Install the required libraries<br
pip install pandas numpy matplotlib seaborn<br>
3. Make sure the dataset is available<br>

Place: <br>

Titanic-Dataset.csv <br>

inside the project folder. <br>

4. Run the Python program<br>
python main.py<br>

The program will:<br>

o Load the Titanic dataset.<br>
o Display dataset information.<br>
o Check missing values and duplicates.<br>
o Handle missing data.<br>
o Detect outliers.<br>
o Remove Fare outliers.<br>
o Create new features.<br>
o Display visualizations.<br>
o Save the cleaned dataset.<br>
<br>
<br>
Author : Kanta Chaudhary
