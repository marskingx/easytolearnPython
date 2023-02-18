# 讀取檔案
data = []  #  建麼空清單
count = 0  #宣告計數器
with open('reviews.txt', 'r') as f:  # 打開一個檔案，並且把這個檔案當做"f"
    for line in f:  # 用for迴圈來讀取這個檔案
        data.append(line)
        count += 1

sum_len = 0
for d in data:  # for loop 就是把清單中的東西一筆一筆的拿出來
    sum_len += len(d)
    print(sum_len)
print('平均長度是', sum_len / len(data))

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('總共有', len(new), '筆資料小於100個字')
print(new[0])
print(new[1])