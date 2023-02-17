while True:  # 當x小於10的時候，進入迴圈
    mode = input('請選擇您需要的遊戲模式：')
    if mode == '1':
        print('啟動遊戲模式1')
    elif mode == '2':
        print('啟動遊戲模式2')
    elif mode == '0':
        print('離開遊戲模式')
        break
    else:
        print('請輸入1/2/0')

print('我出來了')