# 載入 csv 模組
import csv
# 載入 numpy 模組
import numpy as np
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
font_prop.set_size('8')

# 讀入2019資料
x2019 = []
y2019 = []
z2019 = []
# 讀入 read.csv
with open('歷年來台旅客來台目的統計.csv', 'r', encoding='utf8') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    
    for row in plots:
        if row[0]=='2019' and row[2]in['亞洲合計 Total', '非洲合計 Total','美洲合計 Total','大洋洲合計 Total','歐洲合計 Total']:
            x2019.append(row[0])
            value = row[3].replace(',', '')  # Remove commas from the string
            y2019.append(row[1])
            z2019.append(int(value)/10000)
            
# 讀入2020資料
x2020 = []
y2020 = []
z2020 = []
# 讀入 read.csv
with open('歷年來台旅客來台目的統計.csv', 'r', encoding='utf8') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    
    for row in plots:
        if row[0]=='2020' and row[2]in['亞洲合計 Total', '非洲合計 Total','美洲合計 Total','大洋洲合計 Total','歐洲合計 Total']:
            x2020.append(row[0])
            value = row[3].replace(',', '')  # Remove commas from the string
            y2020.append(row[1])
            z2020.append(int(value)/10000)

# 讀入2021資料
x2021 = []
y2021 = []
z2021 = []
# 讀入 read.csv
with open('歷年來台旅客來台目的統計.csv', 'r', encoding='utf8') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    
    for row in plots:
        if row[0]=='2021' and row[2]in['亞洲合計 Total', '非洲合計 Total','美洲合計 Total','大洋洲合計 Total','歐洲合計 Total']:
            x2021.append(row[0])
            value = row[3].replace(',', '')  # Remove commas from the string
            y2021.append(row[1])
            z2021.append(int(value)/10000)

# 讀入2022資料
x2022 = []
y2022 = []
z2022 = []
# 讀入 read.csv
with open('歷年來台旅客來台目的統計.csv', 'r', encoding='utf8') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    
    for row in plots:
        if row[0]=='2022' and row[2]in['亞洲合計 Total', '非洲合計 Total','美洲合計 Total','大洋洲合計 Total','歐洲合計 Total']:
            x2022.append(row[0])
            value = row[3].replace(',', '')  # Remove commas from the string
            y2022.append(row[1])
            z2022.append(int(value)/10000)


# 設定畫布大小
plt.figure(figsize=(12,6))
# 設定圖表內容
bar_width=0.2
labels2019 = y2019
sizes2019 = z2019
labels2020 = y2020
sizes2020 = z2020
labels2021 = y2021
sizes2021 = z2021
labels2022 = y2022
sizes2022 = z2022
index = np.arange(len(y2019))

# 繪製2019年的長條圖
plt.bar(index,sizes2019,width=bar_width,tick_label=y2019,color='#ACD6FF',label='2019年')
# 繪製2020年的長條圖
plt.bar(index+bar_width,sizes2020,width=bar_width,tick_label=y2020,color='#F1E1FF',label='2020年')
# 繪製2021年的長條圖
plt.bar(index+bar_width*2,sizes2021,width=bar_width,tick_label=y2021,color='#C1FFE4',label='2021年')
# 繪製2022年的長條圖
plt.bar(index+bar_width*3,sizes2022,width=bar_width,tick_label=y2022,color='#FFC78E',label='2022年')

plt.title('2019~2022年各地區來台人數比較圖',fontproperties=font_prop,rotation=0,fontsize=18)
# 設定 x 軸刻度標籤及對應的文字
plt.xticks(index+bar_width*1.5, labels=y2019, fontproperties=font_prop)
plt.legend(prop=font_prop)  # 設定標籤使用中文字體
plt.xlabel('地區',fontproperties=font_prop,rotation=0,fontsize=12)
plt.ylabel('旅客人數\n(萬人)',fontproperties=font_prop,rotation=0,fontsize=12,ha='right')

# 在每個點的上方加入'合計'的文字標籤
# j+10讓點跟字分開一點，ha:水平對齊，va:垂直對齊
for i, j in enumerate(z2019):
    plt.text(i, j+3, f'{j:.2f}', ha='center', va='bottom', fontproperties=font_prop)
for i, j in enumerate(z2020):
    plt.text(i+bar_width, j+3, f'{j:.2f}', ha='center', va='bottom', fontproperties=font_prop)
for i, j in enumerate(z2021):
    plt.text(i+bar_width*2, j+3, f'{j:.2f}', ha='center', va='bottom', fontproperties=font_prop)
for i, j in enumerate(z2022):
    plt.text(i+bar_width*3, j+3, f'{j:.2f}', ha='center', va='bottom', fontproperties=font_prop)

# 儲存圖表
plt.savefig('2019~2022年各地區來台人數比較長條圖',dpi=300)
# 顯示圖表
plt.show()
plt.close()