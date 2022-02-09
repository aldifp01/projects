import pandas as pd
kolom = ['id', 'username', 'tweet']
df_windows = pd.read_csv('/home/stndb01/Documents/Data_Engineering/Proyek/windows 11.csv', names = kolom)
df_windows
df_windows.duplicated().value_counts()

df_windows.to_csv('/home/stndb01/Documents/Data_Engineering/Proyek/windows_11_e.csv')
