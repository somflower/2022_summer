students = ["신짱구", "김철수", "유리", "맹구"]
score1 = [100, 90, 60, 90]
score2 = [90, 98, 70, 80]
score3 = [97, 89, 60, 91]

total = list(sum(i) for i in zip(score1, score2, score3))
average = list(sum(i)/3 for i in zip(score1, score2, score3))
PorF = list("합격" if sum(i)/3 >= 80 else "불합격" for i in zip(score1, score2, score3))

for i in range(4) :
    print("(",students[i], total[i], average[i], PorF[i], ")")

