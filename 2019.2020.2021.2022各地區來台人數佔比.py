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

# 輸入2019標籤資料
labels=y2019
sizes=z2019
colors=['#FFE6FF','#FFBB77','#FFFFB9','#DFFFDF','#CECEFF']
explode=(0.05,0.05,0.05,0.05,0.05)
# 繪製2019圓餅圖
plt.pie(sizes,explode,labels=labels,colors=colors, autopct='%1.1f%%',textprops={'fontproperties': font_prop})
plt.axis('equal')  # 讓圓餅圖比例相等
plt.title('2019年各地區來台人數佔比', fontproperties=font_prop,fontsize=12)
# 儲存2019圖表
plt.savefig('2019年各地區來台人數佔比.png',dpi=300)
plt.close()

# 讀入2020資料
x2020 = []
y2020 = []
z2020 = []
# 讀入 read.csv
with open('歷年來台旅客來台目的統計.csv', 'r', encoding='utf8') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    
    for row in plots:
        if row[0]=='2020' and row[2]in['亞洲合計 Total', '非洲合計 Total','美洲合計 Total','大洋洲合計 Total','歐洲合計 Total']:
            x2019.append(row[0])
            value = row[3].replace(',', '')  # Remove commas from the string
            y2020.append(row[1])
            z2020.append(int(value)/10000)

# 輸入2020標籤資料
labels2020=y2020
sizes2020=z2020
# 繪製2020圓餅圖
plt.pie(sizes2020,explode,labels=labels2020,colors=colors, autopct='%1.1f%%',textprops={'fontproperties': font_prop})
plt.axis('equal')  # 讓圓餅圖比例相等
plt.title('2020年各地區來台人數佔比', fontproperties=font_prop,fontsize=12)
# 儲存2020圖表
plt.savefig('2020年各地區來台人數佔比.png',dpi=300)
plt.close()

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

# 輸入2021標籤資料
labels2021=y2021
sizes2021=z2021
# 繪製2021圓餅圖
plt.pie(sizes2021,explode,labels=labels2021,colors=colors, autopct='%1.1f%%',textprops={'fontproperties': font_prop})
plt.axis('equal')  # 讓圓餅圖比例相等
plt.title('2021年各地區來台人數佔比', fontproperties=font_prop,fontsize=12)
# 儲存2021圖表
plt.savefig('2021年各地區來台人數佔比.png',dpi=300)
plt.close()

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

# 輸入2022標籤資料
labels2022=y2022
sizes2022=z2022
# 繪製2022圓餅圖
plt.pie(sizes2022,explode,labels=labels2022,colors=colors, autopct='%1.1f%%',textprops={'fontproperties': font_prop})
plt.axis('equal')  # 讓圓餅圖比例相等
plt.title('2022年各地區來台人數佔比', fontproperties=font_prop,fontsize=12)
# 儲存2022圖表
plt.savefig('2022年各地區來台人數佔比.png',dpi=300)
plt.close()