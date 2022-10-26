#pandas 
import pandas as pd

data = [80, 90, 100]
sr1 = pd.Series(data)
print(type(sr1))
print(sr1)

data = [10, 20, 30]
sr2 = pd.Series(data)

seri_hap = pd.concat([sr1, sr2], ignore_index=True, axis = 1)#인덱스 무시해서 붙이기
print(seri_hap)