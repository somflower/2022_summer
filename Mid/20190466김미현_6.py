f1 = open("input.txt", "r", encoding= "UTF-8")
f2 = open("output.txt", "w", encoding= "UTF-8")
numlist = []

contents = f1.read()

word = contents.split(", ")
for i in word :
    if i.isdigit() :
        numlist.append(i)
    else :
        f2.write(i)

n1 = numlist[1]-numlist[0]
n2 = numlist[3]-numlist[2]
n3 = numlist[5]-numlist[4]

if n1 > n2 :
    max = n1
elif n2 > n1:
    max = n2
if n3 > max :
    max = n3

print("�����Ⱓ�� ���� �� ����� <%s>�̴�", )
print("%s�� �����Ⱓ�� <%d��>�̴�" % max)


f1.close()
f2.close()