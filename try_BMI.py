hight = input('請輸入你的身高:')
weight = input('請輸入你的體重：')
hight = int(hight)
weight = int(weight)
hight = hight / 100    # 轉換為公尺
bmi = int(weight / hight / hight)
if bmi < 18.5:
    print('你的bmi值為', bmi, '屬體重過輕')
elif 18.5 <= bmi < 24:
    print('你的bmi值為', bmi, '屬正常範圍')
elif 24 <= bmi < 27:
    print('你的bmi值為', bmi, '稍重')
elif 27 <= bmi < 30:
    print('你的bmi值為', bmi, '輕度肥胖')
elif 30 <= bmi < 35:
    print('你的bmi值為', bmi, '中度肥胖')
elif bmi >= 35:  # 寫else: 也可以
    print('你的bmi值為', bmi, '重度肥胖')