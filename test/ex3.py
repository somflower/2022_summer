#람다 예시
nums = [1, 2, 3, 4]

f = lambda x : x*x
for i in nums :
  print(f(i), end = " ")

  """for n in nums:
    print((lambda x : x**2)(n))"""