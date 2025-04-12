import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.inspection import DecisionBoundaryDisplay


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

# Codificar la variable objetivo y guardarla en el diccionario
le_target = LabelEncoder()
data['NObeyesdad'] = le_target.fit_transform(data['NObeyesdad'])
label_encoders['NObeyesdad'] = le_target


# * Separate X values from Y
X = data.drop(columns='NObeyesdad')
y = data['NObeyesdad']

# * Separate into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# * Training multiclass logistic regression model
log_model = LogisticRegression(multi_class='multinomial', solver='lbfgs', max_iter=1000)
log_model.fit(X_train, y_train)

# * Predict test set
y_pred = log_model.predict(X_test)

# # * Evaluación
print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nMatriz de confusión:")
print(confusion_matrix(y_test, y_pred))

print("\nReporte de clasificación:")
target_names = label_encoders['NObeyesdad'].classes_
print(classification_report(y_test, y_pred, target_names=target_names))

# # Graficar con matplotlib
# plt.figure(figsize=(8, 6))
# scatter = plt.scatter(X_train['Gender'], X_train['Age'], c=y_train, cmap='tab10', edgecolors='k')
# plt.xlabel('Gender')
# plt.ylabel('Age')
# plt.title('Visualización simple de los datos de entrenamiento')

# # Añadir leyenda
# plt.legend(handles=scatter.legend_elements()[0], labels=le_target.classes_, title="Clase")

# plt.grid(True)
# plt.show()