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


# 讀入亞洲地區資料
x1 = []
y1 = []
# 讀入 read.csv
with open('歷年來台旅客來台目的統計.csv', 'r', encoding='utf8') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    
    for row in plots:
        if row[0].isdigit() and int(row[0]) > 2018 and row[1]=='亞洲地區' and row[2]in['亞洲合計 Total', '非洲合計 Total','美洲合計 Total','大洋洲合計 Total','歐洲合計 Total']:
            x1.append(row[0])
            value = row[3].replace(',', '')  # Remove commas from the string
            y1.append(int(value)/10000)

# 讀入非洲地區資料
x2 = []
y2 = []
# 讀入 read.csv
with open('歷年來台旅客來台目的統計.csv', 'r', encoding='utf8') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    
    for row in plots:
        if row[0].isdigit() and int(row[0]) > 2018 and row[1]=='非洲地區' and row[2]in['亞洲合計 Total', '非洲合計 Total','美洲合計 Total','大洋洲合計 Total','歐洲合計 Total']:
            x2.append(row[0])
            value = row[3].replace(',', '')  # Remove commas from the string
            y2.append(int(value)/10000)

# 讀入美洲地區資料
x3 = []
y3 = []
# 讀入 read.csv
with open('歷年來台旅客來台目的統計.csv', 'r', encoding='utf8') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    
    for row in plots:
        if row[0].isdigit() and int(row[0]) > 2018 and row[1]=='美洲地區' and row[2]in['亞洲合計 Total', '非洲合計 Total','美洲合計 Total','大洋洲合計 Total','歐洲合計 Total']:
            x3.append(row[0])
            value = row[3].replace(',', '')  # Remove commas from the string
            y3.append(int(value)/10000)

# 讀入大洋洲地區資料
x4 = []
y4 = []
# 讀入 read.csv
with open('歷年來台旅客來台目的統計.csv', 'r', encoding='utf8') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    
    for row in plots:
        if row[0].isdigit() and int(row[0]) > 2018 and row[1]=='大洋洲地區' and row[2]in['亞洲合計 Total', '非洲合計 Total','美洲合計 Total','大洋洲合計 Total','歐洲合計 Total']:
            x4.append(row[0])
            value = row[3].replace(',', '')  # Remove commas from the string
            y4.append(int(value)/10000)

# 讀入歐洲地區資料
x5 = []
y5 = []
# 讀入 read.csv
with open('歷年來台旅客來台目的統計.csv', 'r', encoding='utf8') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    
    for row in plots:
        if row[0].isdigit() and int(row[0]) > 2018 and row[1]=='歐洲地區' and row[2]in['亞洲合計 Total', '非洲合計 Total','美洲合計 Total','大洋洲合計 Total','歐洲合計 Total']:
            x5.append(row[0])
            value = row[3].replace(',', '')  # Remove commas from the string
            y5.append(int(value)/10000)

# 圖表外觀設定
plt.figure(figsize=(12,8),facecolor='#ECFFFF')
# 繪製亞洲地區年折線
plt.plot(x1,y1, color='#4F81bd', linestyle='-', marker='o', label='亞洲地區(單位：萬人)')
# 繪製非洲地區年折線
plt.plot(x2,y2, color='#C0504D', linestyle='-', marker='o', label='非洲地區(單位：萬人)')
# 繪製美洲地區年折線
plt.plot(x3,y3, color='#9BBB59', linestyle='-', marker='o', label='美洲地區(單位：萬人)')
# 繪製大洋洲地區年折線
plt.plot(x4,y4, color='#8064A2', linestyle='-', marker='o', label='大洋洲地區(單位：萬人)')
# 繪製歐洲地區年折線
plt.plot(x5,y5, color='#4BACC6', linestyle='-', marker='o', label='歐洲地區(單位：萬人)')

plt.xlabel('西元年',fontproperties=font_prop,rotation=0,fontsize=12)
plt.ylabel('旅客人數',fontproperties=font_prop,rotation=0,fontsize=12,ha='right')
#plt.ylim([-1,12])
plt.title('歷年來台旅遊總人數',fontproperties=font_prop,rotation=0,fontsize=16)
plt.xticks(x2,fontproperties=font_prop)

# 在每個點的上方加入'合計'的文字標籤
# j+0.5讓點跟字分開一點，ha:水平對齊，va:垂直對齊
for i, j in enumerate(y1):
    plt.text(i, j+0.5, f'{j:.2f}', ha='center', va='bottom', color='#4F81bd', fontproperties=font_prop)
for i, j in enumerate(y2):
    plt.text(i, j-0.5, f'{j:.2f}', ha='center', va='bottom', color='#C0504D', fontproperties=font_prop, fontsize=10)
for i, j in enumerate(y3):
    plt.text(i, j+0.5, f'{j:.2f}', ha='center', va='bottom', color='#9BBB59', fontproperties=font_prop, fontsize=10)
for i, j in enumerate(y4):
    plt.text(i, j+0.5, f'{j:.2f}', ha='center', va='bottom', color='#8064A2', fontproperties=font_prop, fontsize=10)
for i, j in enumerate(y5):
    plt.text(i, j-0.5, f'{j:.2f}', ha='center', va='bottom', color='#4BACC6', fontproperties=font_prop, fontsize=10)

# 顯示格線
plt.grid()
# 設定圖例
plt.legend(prop=fm.FontProperties(fname=font_path))
# 儲存圖表
plt.savefig('2019~2022各地來台人數折線圖-X軸年份.png',dpi=300)
# 顯示圖表
plt.show()
plt.close()
