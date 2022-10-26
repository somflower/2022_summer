score = []
p = 0
f = 0

num = int(input("수강 과목 수 입력 :"))

for i in range(num):
    print("score", i+1, ":", end = "")
    score.append(int(input()))

for i in score:
    if(i >= 80):
        p = p + 1
    else:
        f = f + 1
print("--------------------")
print("합격과목 수 :", p)
print("불합격과목 수 :", f)