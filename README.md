# Student Grade Predictor 🎓📊

A machine learning project that predicts a student's final grade (`G3`) using data from the UCI Student Performance dataset. The model is trained using features like prior grades, alcohol consumption, family support, and other behavioral and demographic factors.

## 📁 Project Structure

## 📌 Features Used

The most relevant features identified were:

- `failures`: number of past class failures
- `studytime`: weekly study time
- `absences`: number of absences
- `internet`: Internet access at home
- `famsup`: family educational support
- `schoolsup`: school-provided support
- `G2`: second-period grade (very predictive of `G3`)

Engineered features include:
- `total_alc`: Combined alcohol consumption (`Dalc + Walc`)
- `delinquency`: Composite score based on absences, alcohol, and going out

## ⚙️ Model

- **Type:** Regression
- **Algorithm Used:** Linear Regression (Polynomial features tested)
- **Libraries:** `scikit-learn`, `pandas`, `numpy`, `matplotlib`

## 📈 Performance

| Metric | Value |
|--------|-------|
| Test R² Score | ~0.81 |
| Test MSE      | Varies depending on test size, ~4.1 |

## 🧠 Key Insights

- `G2` alone provides high predictive power.
- Features like `total_alc`, `absences`, and `studytime` contribute marginally.
- Feature engineering helped slightly but wasn't as impactful as prior grades.
