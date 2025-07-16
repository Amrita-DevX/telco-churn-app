def add_custom_features(df):
    services = ['PhoneService', 'MultipleLines', 'OnlineSecurity',
                'OnlineBackup', 'DeviceProtection', 'TechSupport',
                'StreamingTV', 'StreamingMovies']
    
    df['NumServices'] = df[services].apply(lambda x: sum(x == 'Yes'), axis=1)
    df['HighMonthlyCharges'] = df['MonthlyCharges'].apply(lambda x: 1 if x > 80 else 0)
    df['IsSeniorDependent'] = df.apply(lambda x: 'Yes' if x['SeniorCitizen'] == 'Yes' and x['Dependents'] == 'Yes' else 'No', axis=1)
    df['PricePerService'] = df['MonthlyCharges'] / (df['NumServices'] + 1)
    
    return df