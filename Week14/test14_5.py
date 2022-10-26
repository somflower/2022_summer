from asyncio import as_completed
import pandas as pd
import matplotlib.pyplot as plt

q6 = pd.read_csv("C:/Dongduk/4-1summer/Bigdata/DONGDUK_4_1_SUMMER/Week12/input.csv", encoding='cp949')
print(q6)
print(q6['이름'])
data = q6['퇴직년도']-q6['입사년도'] + 1
q6['재직기간'] = data
print(q6)

print(q6.shape)
r, c = q6.shape
print(r)

print(q6.iloc[0][2])
print(q6.loc[0]['퇴직년도'])
print(q6.loc[: , ['이름', '재직기간']])
print(q6.groupby('퇴직년도')['입사년도'].max())
print(q6.groupby('퇴직년도')['입사년도'].unique())

x = q6['이름']
y = q6['재직기간']
plt.plot(x,y, 'sm')
plt.xlabel('이름')
plt.ylabel('년도')
plt.show()



