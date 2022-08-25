# draw_graph2.py
'''
첨부 데이터("Training_set.csv")를 사용하여 
남여를 구분하고 남여 각각 키의 분포를 하나의 히스토그램으로 나타내고, 
남여 각각 몸무게의 분포를 히스토그램으로 따로 표시하는 프로그램을 작성하여 제출하시오.

이 데이터는 개인별로 키, 몸무게, 성별을 조사한 것입니다.
히스토그램의 간격은 5단위로 한다. 
예를 들어 키는 120, 125, 130, 135, 140, ..., 200 등으로 한다. 
몸무게는 30, 35, 40, 45 ... 100 등으로 한다.
힌트 : groupby, get_group 등을 이용하여 데이터를 그룹핑하고 분리할 수 있음.
'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager as fm
from matplotlib import rc

import pandas as pd

#다음 3줄의 코드는 한글을 그래프에 출력하기 위함이다.
mpl.rcParams['axes.unicode_minus'] = False
font_name = fm.FontProperties(fname="c:/windows/fonts/malgun.ttf").get_name()
rc('font', family=font_name)

# 그래프 크기
plt.rcParams["figure.figsize"] = (8, 5)

data=pd.read_csv('Training_set.csv', header=0)
grouped=data['Weight'].groupby(data['Gender'])

boy=grouped.get_group('Male') # index를 가지는 series 형태이다.
girl=grouped.get_group('Female')



binsList=[i for i in range(30,101,5)]

plt.subplots_adjust(left=0.125, bottom=0.1,  right=0.9, top=0.9, wspace=0.3, hspace=0.35)

plt.subplot(1,2,1) # 1행, 2열, 1번째
plt.hist(boy, bins=binsList, label=['Boy'])

plt.xlim(30, 100)
plt.ylim(0, 350)
plt.xlabel('Weight')
plt.ylabel('Counts')
plt.title('Histogram of Weight(Boy)')
plt.grid(True, alpha=0.5, linestyle='--')
plt.legend(loc='upper left')

plt.subplot(1,2,2) # 1행, 2열, 1번째
plt.hist(girl, bins=binsList, label=['Girl'], color='r')

plt.xlim(30, 100)
plt.ylim(0, 350)
plt.xlabel('Weight')
plt.ylabel('Counts')
plt.title('Histogram of Weight(Girl)')
plt.grid(True, alpha=0.5, linestyle='--')
plt.legend(loc='upper left')
plt.show()
