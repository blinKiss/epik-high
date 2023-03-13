# test5.py
# https://www.data.go.kr/ 에서 한국교통안전공단_자동차제작결함신고정보 데이터를 이용하여
# 현대 기아 쌍용 르노 지엠 5개 회사의 총 결함수를 구하고 파이그래프로 출력하시오

import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import numpy as np
import pandas as pd

font_path = 'C:/Windows/Fonts/gulim.ttc'
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

df = pd.read_csv('./EyEDi/data/한국교통안전공단_자동차제작결함신고정보_20211231.csv')
df_slice = df['제작사'].value_counts()
# print(df_slice)

h, k, s, r, g = 0, 0, 0, 0, 0

company = ['현대', '기아', '쌍용', '르노', '지엠']
count = []

for i in company:
    count.append(df2[df2['제작사'].str.contains(i)].shape[0])

cc = dict(sorted(zip(company, count), key=lambda x: x[1], reverse=True))

plt.title('제조사별 자동차 결함 신고 수', loc='left')
explode = (0.1, 0, 0, 0, 0)
plt.pie(cc.values(),explode=explode, labels=cc.keys(), autopct='%.1f%%', startangle=90, counterclock=False)
plt.show()

# print(count)