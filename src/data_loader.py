import pandas as pd 

# Math Grades
def load_math_data(path='data/student-mat.csv'):
    # Read the CSV file 
    df = pd.read_csv(path, sep=';')
    return df 

# Portugese Grades
def load_por_data(path='data/student-por.csv'):
    # Read the CSV file 
    df = pd.read_csv(path, sep=';')
    return df 