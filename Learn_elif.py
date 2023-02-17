# else if 可以解讀成「另外如果」
age = input('請輸入年齡:')
age = int(age)
if age < 13:
    print('應該是國小生')
elif 13 <= age < 18:
    print('國高中')
elif 18 <= age < 22:
    print('大學生')
else:
    print('社會人士')