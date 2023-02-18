import random
start = input('請輸入開始值')
end = input('請輸入結束值')
start = int(start)
end = int(end)
guess = random.randint(start, end)
count = 0
print(guess)
while guess > 0:
    count += 1
    asr = input('請你猜大小')
    asr = int(asr)
    if asr == guess:
        print('恭禧你在第', count, '次猜對，你可以再猜一次')
        guess = guess + random.randint(start,end)
        print(guess)
    elif asr < guess:
        print('你猜了第', count, '次，答案要再大一點')
    elif asr > guess:
        print('你猜了第', count, '次，答案要再小一點')
    else:
        print('答案在1-99之間')
