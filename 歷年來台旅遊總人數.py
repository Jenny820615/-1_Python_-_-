# 載入 csv 模組
import csv
# 載入 pandas 模組
import pandas as pd
# 載入 matplotlib.pyplot 模組
import matplotlib.pyplot as plt
# 載入 字體管理員 模組
import matplotlib.font_manager as fm

# 設定中文字體
font_path='/System/Library/Fonts/STHeiti Medium.ttc'
font_prop=fm.FontProperties(fname=font_path)
font_prop.set_style('normal')
font_prop.set_size('12')

x = []
y = []

# 讀入 read.csv
with open('歷年來台旅客來台目的統計.csv', 'r', encoding='utf8') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    
    for row in plots:
        if row[2]in['總計 Grand Total']:
            x.append(row[0])
            value = row[3].replace(',', '')  # Remove commas from the string
            y.append(int(value)/10000)
        
# 圖表外觀設定
plt.figure(figsize=(10,6),facecolor='#FFFFDF')
plt.plot(x,y,'bo-')
plt.xlabel('西元年',fontproperties=font_prop,rotation=0,fontsize=12)
plt.ylabel('旅客人數',fontproperties=font_prop,rotation=0,fontsize=12,ha='right')
plt.ylim([-100,1500])
plt.title('歷年來台旅遊總人數',fontproperties=font_prop,rotation=0,fontsize=16)
plt.xticks(x)

# 在每個點的上方加入'合計'的文字標籤
# j+0.5讓點跟字分開一點，ha:水平對齊，va:垂直對齊
for i, j in zip(x,y):
    plt.text(i, j+20, f'{j:.2f}', ha='center', va='bottom', fontproperties=font_prop)

# 顯示格線
plt.grid()
# 設定圖例
plt.legend(['旅客人數 (單位：萬人)'],prop=fm.FontProperties(fname=font_path))
# 儲存圖表
plt.savefig('歷年來台旅遊總人數.png',dpi=300)
# 顯示圖表
plt.show()
plt.close()