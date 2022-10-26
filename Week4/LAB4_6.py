Korean = [49, 80, 20, 100, 80]
Math = [43, 60, 85, 30, 90]
English = [49, 82, 48, 50, 100]
Score = [Korean, Math, English]
Student = []

#print(Score)
#print(Score[0][0], Score[1][0], Score[2][0])
sum = 0

for i in range(5) :
    for j in range(3) :
        sum = sum + Score[j][i]
    Student.append(sum/3)
    sum = 0

print(Student)