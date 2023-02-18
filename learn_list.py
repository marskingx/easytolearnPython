# list 清單
a = ['toyota', 'honda']
print(a)
print(a[0])
print(a[1])
a.append('Audi')
print(a)
print(len(a))
print('Audi' in a)  # 用in來檢查清單內容東西
print('Benz' in a)

# for loop 把清單中的東西一個一個拿出來
cars = ['Toyota', 'Honda']
for car in cars:
    print(car)