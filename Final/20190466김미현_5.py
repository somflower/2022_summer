import pandas as pd
import matplotlib.pyplot as plt

data = [[150, 45],[125, 30], [130, 28], [140, 48]]
df = pd.DataFrame(data, index = ["자두", "짱구", "유리", "맹구"], columns = ["키", "몸무게"])
calcBMI = df["몸무게"] / (df["키"]**2) * 10000
df["BMI"] = calcBMI.round(2)

if calcBMI >= 30 :
    value = "고도비만"
elif calcBMI >= 25 :
    value = "비만"
elif calcBMI >= 23 :
    value = "과체중"
elif calcBMI >= 18.5 :
    value = "정상"
else :
    value = "저체중"


df["비만도"] = value
print(df)

x = df[0]
y = df["BMI"]
plt.xlabel("이름")
plt.ylabel("BMI")
plt.show


