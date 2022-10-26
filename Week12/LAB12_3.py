import csv

line_counter = 0
header = []
datalist = []
with open("G:/다른 컴퓨터/내 컴퓨터/Dongduk/4-1summer/Bigdata/DONGDUK_4_1_SUMMER/Week12/input.csv", "r") as file1:
#with open("C:/Dongduk/4-1summer/Bigdata/DONGDUK_4_1_SUMMER/Week12/input.csv", "r") as file1:
    csv_data = csv.reader(file1)

    for row in csv_data :
        if line_counter == 0:
            header = row
        else :
            datalist.append(row[0])
            datalist.append(int(row[2]) - int(row[1]) + 1)
        line_counter += 1
    print(datalist)


with open("q6_input.csv", "w") as file2 :
    for data in datalist :
        file2.write(","+str(data))
        
        




