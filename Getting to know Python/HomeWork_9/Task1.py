ndf = pd.read_csv('sample_data/california_housing_train.csv')
ndf[(ndf['population'] > 0) & (ndf['population'] < 500)]['median_house_value'].mean()