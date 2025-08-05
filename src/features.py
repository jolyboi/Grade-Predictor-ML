def preprocess_features(df):
    # Select right features 
    features = [
        'failures', 'studytime',
        'schoolsup', 'famsup', 'absences',
        'internet', 'G2'
    ]
    
    # New engineered features 
    df['total_alc'] = df['Dalc'] + df['Walc']

    features += ['total_alc']
    
    target = 'G3'
    df = df[features + [target]].copy()

    binary_map = {
        'yes': 1, 'no': 0,
        'F': 0, 'M': 1
    }

    for col in ['schoolsup', 'famsup', 'internet']:
        df[col] = df[col].map(binary_map)

    X = df.drop(columns=[target])
    y = df[target]

    return X, y