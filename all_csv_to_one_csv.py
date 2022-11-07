import os, glob
import pandas as pd

path = "F:/Arrhythmia Detection/Data"
csv_list = [209]
all_files = []

for i in csv_list:
    all_files = all_files + glob.glob(os.path.join(path, str(i) + ".csv"))
print(all_files)

all_df = []
for f in all_files:
    df = pd.read_csv(f)
    all_df.append(df)

merged_df = pd.concat(all_df)

normal = merged_df.iloc[:, 1]
print(normal)
#merged_df.drop(df.columns[[0, 2]], axis = 1, inplace = True)
#print (merged_df)
normal.to_csv("apc_ecg.csv")
