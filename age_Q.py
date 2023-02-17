driving = input('請問你有開過車嗎?')
if driving != '有' and '沒有':
    print('只能輸入有/沒有')
    raise SystemExit
age = input('請問你幾歲?')
age = int(age)
if driving == '有':
    if age >= 18:
        print('你通過測驗了')
    else:
        print('奇怪!你怎麼會開過車?')
elif driving == '沒有':
    if age >= 18:
        print('你可以考照了')
    else:
        print('你快要可以考了')
