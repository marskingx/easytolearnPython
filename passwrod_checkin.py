x = 3  # 宣告密碼有3次機會
password = 'asdf'  # 宣告正確的密碼是asdf
while x > 0:  # 進入迴圈
    pwd = input('請輸入使用者密碼：')  # 請使用者輸入密碼
    x = x - 1  # 剩餘次數減少一次
    if pwd == password:  # 如果密碼是正確的asdf(password)
        print('登入成功')  # 顯示登入成功
        break  # 離開程式
    else:
        if x > 0:
            print('密碼錯誤，還有', x, '次輸入的機會')  # 就列印密碼錯誤的剩餘次數
        elif x == 0:
            print('3次密碼錯誤，請重置密碼')