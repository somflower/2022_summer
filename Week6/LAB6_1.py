stock = {'커피': 15, '펜': 3, '종이컵': 20, '우유': 5, '콜라': 7, '라면': 20}
print("판매 전 재고:", stock)

name = input("판매한 물건을 입력하시오: ")

"""for k, v in stock.items() :
    print(k, v)"""

if stock.get(name) :#if name in stock:
    stock[name] = stock[name] - 1

print("판매 후 재고", stock)