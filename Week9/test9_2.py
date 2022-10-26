print("===abs===")
print(abs(3))
print(abs(-3))
print(abs(-1.2))
#print(abs("A")) --> 숫자형만 가능
print()

print("===sum===")
#print(sum(1, 2)) --> 불가능
print(sum([1, 2, 3]))#리스트
print(sum((1, 2, 3)))#튜플
#print(sum({1 : 2, 2 : 4, 3 : 6})) --> 딕셔너리는 어떻게 나오는 지 모르겠음
print()

print("===pow===")
print(pow(2, 4))
print(pow(3, 3))
print()

print("===max===")
print(max([1, 2, 3]))
print(max("python"))
print()

print("===min===")
print(min([1, 2, 3]))
print(min("python"))
print()

print("===divmod===")#몫과 나머지 한번에 구하기,결과는 튜플로 나옴
print(divmod(7, 3))
print(divmod(6, 3))
print(divmod(1.3, 0.2))
print()

print("===round===")#소수점아래 ?자리에서 반올림, 기본값은 1
#0.5는 앞자리 수가 짝수면 내림, 홀수면 올림사용
print(round(10.5))
print(round(9.5))
print(round(11.5))
print(round(12.5))
print(round(5.678, 2))
print()

print("===int===")
print(int('3'))
print(int(3.4))
print(int('11', 2))
print(int('1A', 16))
print()

print("===float===")
print(float('3.14'))
print(float(4))
print(float(5.0))
print()

print("===str===")
print(str(3))
print(str('hi'))
print(str('hi'.upper()))
print()

print("===eval===")
print(eval('1 + 2'))
print(eval("'hi' + 'a'"))
print("hi" + "a")
x = 10
print(eval('x + 1'))
print()

print("===len===")
print(len("python"))
print(len([1, 2, 3]))#리스트
print(len((1, 'a')))#튜플
print(len({1 : 3}))#딕셔너리
print()

print("===sorted===")
s1 = sorted([3, 1, 2])#리스트
print(s1)
print(sorted(['a', 'c', 'b']))#리스트
s3 = sorted("zero")#str
print(s3)
s4 = sorted((3, 2, 1))#튜플
print(s4)
s5 = sorted((1, 3, 2), reverse = True)#거꾸로 정리
print(s5)
print()

print("===ord===")#아스키코드 구하기
print(ord("a"))
print(ord("0"))
print()

print("===chr===")#아스키코드를 알파벳으로
print(chr(97))
print(chr(48))
print()

print("===hex===")
print(hex(234))
print(hex(3))
print()

print("===oct===")
print(oct(34))
print(oct(12345))
print()

print("===isdigit===")#문자열에만 사용, 실수또한 False
print("hello".isdigit())
print("123".isdigit())
print("123abc".isdigit())
print("abc123".isdigit())
a = "3.14"
print(a.isdigit())
print()

print("===isalpha===")
print("hello".isalpha())
print("hello3".isalpha())
print("123abc".isalpha())
print()

print("===dir===")
print(dir([1, 2, 3]))#리스트
print(dir({'1' : 'a'}))#딕셔너리
print(dir((1, 2, 3)))#튜플
print()