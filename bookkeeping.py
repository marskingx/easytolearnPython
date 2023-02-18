products = []
while True:
    name = input('請輸入商品名稱：')
    if name == 'q':
        break
    price = input('請輸入商品價格：')
    products.append([name, price])  # 把p放入products

print(products[1][1])

for p in products:
    print(p[0], '價格是', p[1])