import pandas as pd
import mysql.connector
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="customer_db"
)

# Read table into dataframe
query = "SELECT * FROM customer_activity"
df = pd.read_sql(query, conn)

print(df.head())

# Encode categorical columns
le_gender = LabelEncoder()
df["gender"] = le_gender.fit_transform(df["gender"])

le_category = LabelEncoder()
df["product_category"] = le_category.fit_transform(df["product_category"])

# Features and target
X = df.drop(["customer_id", "purchased"], axis=1)
y = df["purchased"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

# Save model
joblib.dump(model, "model/model.pkl")

print("Model saved successfully!")