import csv

rainfall_data = []
header = []
rownum = 0
sum = 0

with open("G:/다른 컴퓨터/내 컴퓨터/Dongduk/4-1summer/Bigdata/DONGDUK_4_1_SUMMER/Week12/rn_20220707131504.csv") as r_file:
    csv_data = csv.reader(r_file)
    for row in csv_data :
        #print(row)
        if rownum == 0 :
            header = row
        else: 
            rainfall_data.append(row[2])
        rownum += 1

for i in rainfall_data :
    sum = sum + float(i)

print(sum)
print(sum/len(rainfall_data))