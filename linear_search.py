import pandas as pd
from time import time

df = pd.read_csv('dataset.csv')

matrix = df.values.tolist()

rows = len(matrix)
columns = len(matrix[0])

publication = input("Enter the publication : ")

start = time()
itsfound = False
for i in range(rows):
    for j in range(columns):
        if matrix[i][j] == publication:
            print(matrix[i])
            itsfound = True
            break

if itsfound == True:
    print(f'Waktu Eksekusi : {time() - start} detik')
else:
    print("Not found!")
    print("Waktu Eksekusi : 0.0 detik")
