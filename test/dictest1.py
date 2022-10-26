country_code = {'America': 1, 'Korea': 82, 'China': 86}
country_code['Japan'] = 81

print(country_code)
print("Key =", country_code.keys())
print(list(country_code.keys()))
print("value =", country_code.values())
print(list(country_code.values()))

for k, v in country_code.items() :
    print(k, v)

print(country_code['Korea'])
print(country_code)
print(country_code.pop('Korea'))
print(country_code)

#print(country_code['Korea'])#pop으로 제거해서 에러뜸
print(country_code.get('Korea', '못 찾았다'))#에러 지우려면 get사용, 기본값 None

country_code.clear()
print(country_code)

