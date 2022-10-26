
class Basket(object) :
    def __init__(self, id):
        self.id = id
        #self.money = price * num
        #self.total = total
        #self.products = [name, price, num]

    def add(self, name, price, num) :
        self.name = name
        self.price = price
        self.num = num


    

ddwu = Basket("동덕", )    

market = {"소금빵" : 3000, "단팥빵":2500, "꽈배기":2000, "사이다":3300, "우유":2800}
print("구매가능한 상품: [소금빵(3000), 단팥빵(2500), 꽈배기(2000), 사이다(3300), 우유(2800)")
print("-"*40)

while True :
    name = input("구매할 상품명 입력: ")
    if name == "" :
        break
    num = int(input("구매 갯수 입력: "))

    for _ in range(5):
        if name == market.keys :
            price = market.values

    print(name, price, num)
    ddwu.add(name, price, num)






