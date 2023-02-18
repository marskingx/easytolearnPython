import xml
#  打開同一個檔案
products = []
with open('products.csv', 'r', encoding='utf-8') as f:
    for line in f:
        if '商品,價格' in line:
            continue  # 如果遇到商品,價格這個字串的時候就跳到下一個迴圈
        name, price = line.strip().split(',')
        products.append([name, price])  # 把p放入products
print(products)

# 讓使用者輸入
while True:
    name = input('請輸入商品名稱：')
    if name == 'q':
        break
    price = input('請輸入商品價格：')
    price = int(price)
    products.append([name, price])  # 把p放入products

# 印出購買記錄
for p in products:
    print(p[0], '價格是', p[1])

# 寫入檔案中並儲存
with open('products.csv', 'w', encoding='utf-8') as f:
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')