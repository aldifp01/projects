import sqlite3 as s3
import pandas as pd
import os

# membuat koneksi ke database
conn = s3.connect('/home/stndb01/Documents/Data_Engineering/Proyek/windows11_data.db')

# Object cursor untuk menjalankan perintah SQL
cur = conn.cursor()

# load dataframe ke datamart
df_windows = pd.read_csv('/home/stndb01/Documents/Data_Engineering/Proyek/windows_11_t.csv')
df_windows.to_sql('windows11_table',conn,if_exists='replace',index=False)
os.remove("/home/stndb01/Documents/Data_Engineering/Proyek/windows_11_e.csv")
os.remove("/home/stndb01/Documents/Data_Engineering/Proyek/windows_11_t.csv")
