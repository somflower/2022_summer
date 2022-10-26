import pandas as pd

data = [[1, 2, 3], [10, 20, 30]]
df = pd.DataFrame(data, index = ['신짱구', '김철수'], columns=['프논이', '교양1', '교양2'])
print(df)
print(df.values)
row_sum = df.sum(axis=0)
print(row_sum)
col_sum = df.sum(axis=1)
print(col_sum)


df['총점'] = col_sum
print(df)

sr1 = pd.Series(row_sum)
pd.concat([df,sr1])
"""print(df)
print(df.keys())
print(df['프논이'].mean())
print(df['교양2'].max())
score = df['프논이']
print(score[score>5])"""

names = ['신짱구', '김철수', '유리']
data = [90, 90, 90, 270]
sr1 = pd.Series(data, index = ['프논이', '교양1', '교양2', '총점'])
df = df.append(sr1, ignore_index=True)
df = df.set_index(keys = [names])
print(df)

#정렬
print(df.sort_index())
print(df.sort_values(by='총점', ascending=False))
