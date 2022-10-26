scores = []

scores.append(int(input("성적을 입력하시오: ")))
scores.append(int(input("성적을 입력하시오: ")))
scores.append(int(input("성적을 입력하시오: ")))
scores.append(int(input("성적을 입력하시오: ")))
scores.append(int(input("성적을 입력하시오: ")))

total = scores[0]+scores[1]+scores[2]+scores[3]+scores[4]

print(scores[:])
print("성적의 합 =", total)
print("평균 =", total/len(scores))