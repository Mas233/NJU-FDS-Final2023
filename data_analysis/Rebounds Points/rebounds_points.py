import pandas

# get dataframe
dataframes = []
for i in range(1, 31):
    path = '../../table_generation/tables/'+str(i)+'/PLAYERS.csv'
    df = pandas.read_csv(path)
    dataframes.append(df)

df = pandas.concat(dataframes)

# select columns
df = df[['Points', 'Rebounds']]
# clear invalid values
df = df.applymap(pandas.to_numeric, errors='coerce').dropna()
df = df[(df['Rebounds'] > 0) & (df['Points'] > 0)]

cov_matrix = df.cov()
corr_matrix = df.corr()

cov = cov_matrix.loc['Points','Rebounds']
corr = corr_matrix.loc['Points','Rebounds']

print("Between Points and Rebounds:\nCov:"+str(cov)+"\nCorr:"+str(corr))
