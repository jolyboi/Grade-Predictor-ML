from src.data_loader import load_math_data, load_por_data
from src.features import preprocess_features
from src.model import train_and_evaluate
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split



df = load_por_data()
# print(df.head())
# print(df.info())

X, y = preprocess_features(df)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# print(X)
# print(y.head())

model, mse, r2, predictions = train_and_evaluate(X_train, y_train, X_test, y_test, degree=2)

print(mse)
print(r2)


