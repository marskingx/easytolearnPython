#  range 範圍的使用
#  python 內建功能：請單產生器

import random

num = range(100)
for i in num:
    r = random.randint(1, 100)
    print('第', i+1, "次" , r)
