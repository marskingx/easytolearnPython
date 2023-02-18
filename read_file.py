# 讀取檔案
data = []
with open('reviews.txt', 'r') as f:  # 打開一個檔案，並且把這個檔案當做"f"
    for line in f:  # 用for迴圈來讀取這個檔案
        data.append(line.strip())
print(len(data))

print(data[0])
print('---')
print(data[1])
