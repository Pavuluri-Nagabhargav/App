import pandas as pd
import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder

# Load the dataset
file_path = 'path_to_your_file/copd_excel.xlsx'  # Update with your file path
copd_data = pd.read_excel(file_path)

# Preprocess the data (encode categorical variables if present)
le = LabelEncoder()
for column in copd_data.columns:
    if copd_data[column].dtype == 'object':
        copd_data[column] = le.fit_transform(copd_data[column])

# Splitting the data into features (X) and target (y)
X = copd_data.drop('COPDStage', axis=1)  # Update 'COPDStage' if the column name is different
y = copd_data['COPDStage']

# Splitting the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Building the LightGBM model
model = lgb.LGBMClassifier()
model.fit(X_train, y_train)

# Predicting and evaluating the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print("Classification Report:")
print(report)
