from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def train_and_evaluate(X_train, y_train, X_test, y_test, degree=2):
    # Create a pipeline to apply polynomial features then linear regression
    model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
    
    # Fit model on X and y
    model.fit(X_train, y_train)
    
    # Predict on the same data (for now)
    predictions = model.predict(X_test)
    
    # Calculate metrics
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    
    return model, mse, r2, predictions 