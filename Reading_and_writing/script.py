import pandas as pd

input_file = 'dataset_Facebook.csv' 
output_file = 'average_lifetime_reach.csv'

df = pd.read_csv(input_file, delimiter=';')
df_filtered = df[['Type', 'Lifetime Post Total Reach']]
average_reach = df_filtered.groupby('Type')['Lifetime Post Total Reach'].mean().reset_index()

average_reach.to_csv(output_file, index=False)
