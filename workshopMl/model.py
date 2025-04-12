import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.preprocessing import LabelEncoder

# * load dataset
df = pd.read_csv("ObesityDataSet.csv")

print("Dataset dimensions:", df.shape)
print("\nFirst 5 rows:")
print(df.head())

# * show data types
print("\nData types:")
print(df.dtypes)

# * Show unique values per column
print("\nUnique values per categoric variable:")
for col in df.columns:
    if df[col].dtype == "object":
        print(f"{col}: {df[col].unique()}")


# * Create copy of dataset to change categorical columns string into int
data = df.copy()

# * Identify categorical columns
categorical_cols = data.select_dtypes(include='object').columns.tolist()
print("\nCategorical columns:", categorical_cols)
label_encoders = {}

# * Apply LabelEncoder to each categorical column
for col in categorical_cols:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    label_encoders[col] = le

