import pandas as pd
kolom = ['id', 'username', 'tweet']
df_windows = pd.read_csv('/home/stndb01/Documents/Data_Engineering/Proyek/windows_11_e.csv', names = kolom)
#df_windows.duplicated().value_counts()


df_windows.drop_duplicates(inplace=True, ignore_index=True)
df_windows
df_windows.to_csv('/home/stndb01/Documents/Data_Engineering/Proyek/windows_11_t.csv')
