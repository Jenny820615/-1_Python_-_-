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
year2019 = []
business2019 = [] #業務+會議
education2019 = [] #求學+展覽
visit2019=[] #探親
tour2019=[] #觀光
medical2019=[] #醫療
others2019=[] #其他
xlabels=['業務會議','學術展覽','探親','觀光','醫療','其他']
# 讀入 read.csv
with open('歷年來台旅客來台目的統計.csv', 'r', encoding='utf8') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    
    for row in plots:
        if row[0]=='2019' and row[2]in['總計 Grand Total']:
            year2019.append(row[0])
            business2019.append(int(row[4].replace(',', ''))/10000 + int(row[7].replace(',', ''))/10000)
            education2019.append(int(row[8].replace(',', ''))/10000 + int(row[9].replace(',', ''))/10000)
            visit2019.append(int(row[6].replace(',', ''))/10000)
            tour2019.append(int(row[5].replace(',', ''))/10000)
            medical2019.append(int(row[10].replace(',', ''))/10000)
            others2019.append(int(row[11].replace(',', ''))/10000)
allvalues2019 = business2019+education2019+visit2019+tour2019+medical2019+others2019
           
# 讀入2020資料
year2020 = []
business2020 = [] #業務+會議
education2020 = [] #求學+展覽
visit2020=[] #探親
tour2020=[] #觀光
medical2020=[] #醫療
others2020=[] #其他
xlabels=['業務會議','學術展覽','探親','觀光','醫療','其他']
# 讀入 read.csv
with open('歷年來台旅客來台目的統計.csv', 'r', encoding='utf8') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    
    for row in plots:
        if row[0]=='2020' and row[2]in['總計 Grand Total']:
            year2020.append(row[0])
            business2020.append(int(row[4].replace(',', ''))/10000 + int(row[7].replace(',', ''))/10000)
            education2020.append(int(row[8].replace(',', ''))/10000 + int(row[9].replace(',', ''))/10000)
            visit2020.append(int(row[6].replace(',', ''))/10000)
            tour2020.append(int(row[5].replace(',', ''))/10000)
            medical2020.append(int(row[10].replace(',', ''))/10000)
            others2020.append(int(row[11].replace(',', ''))/10000)
allvalues2020 = business2020+education2020+visit2020+tour2020+medical2020+others2020

# 讀入2021資料
year2021 = []
business2021 = [] #業務+會議
education2021 = [] #求學+展覽
visit2021=[] #探親
tour2021=[] #觀光
medical2021=[] #醫療
others2021=[] #其他
xlabels=['業務會議','學術展覽','探親','觀光','醫療','其他']
# 讀入 read.csv
with open('歷年來台旅客來台目的統計.csv', 'r', encoding='utf8') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    
    for row in plots:
        if row[0]=='2021' and row[2]in['總計 Grand Total']:
            year2021.append(row[0])
            business2021.append(int(row[4].replace(',', ''))/10000 + int(row[7].replace(',', ''))/10000)
            education2021.append(int(row[8].replace(',', ''))/10000 + int(row[9].replace(',', ''))/10000)
            visit2021.append(int(row[6].replace(',', ''))/10000)
            tour2021.append(int(row[5].replace(',', ''))/10000)
            medical2021.append(int(row[10].replace(',', ''))/10000)
            others2021.append(int(row[11].replace(',', ''))/10000)
allvalues2021 = business2021+education2021+visit2021+tour2021+medical2021+others2021

# 讀入2022資料
year2022 = []
business2022 = [] #業務+會議
education2022 = [] #求學+展覽
visit2022=[] #探親
tour2022=[] #觀光
medical2022=[] #醫療
others2022=[] #其他
xlabels=['業務會議','學術展覽','探親','觀光','醫療','其他']
# 讀入 read.csv
with open('歷年來台旅客來台目的統計.csv', 'r', encoding='utf8') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    
    for row in plots:
        if row[0]=='2022' and row[2]in['總計 Grand Total']:
            year2022.append(row[0])
            business2022.append(int(row[4].replace(',', ''))/10000 + int(row[7].replace(',', ''))/10000)
            education2022.append(int(row[8].replace(',', ''))/10000 + int(row[9].replace(',', ''))/10000)
            visit2022.append(int(row[6].replace(',', ''))/10000)
            tour2022.append(int(row[5].replace(',', ''))/10000)
            medical2022.append(int(row[10].replace(',', ''))/10000)
            others2022.append(int(row[11].replace(',', ''))/10000)
allvalues2022 = business2022+education2022+visit2022+tour2022+medical2022+others2022

# 設定畫布大小
plt.figure(figsize=(12,6))
# 設定圖表內容
bar_width=0.2
labels2019 = xlabels
sizes2019 = allvalues2019
labels2020 = xlabels
sizes2020 = allvalues2020
labels2021 = xlabels
sizes2021 = allvalues2021
labels2022 = xlabels
sizes2022 = allvalues2022

index = np.arange(len(xlabels))

# 繪製2019年的長條圖
plt.bar(index,sizes2019,width=bar_width,tick_label=xlabels,color='#ACD6FF',label='2019年')
# 繪製2020年的長條圖
plt.bar(index+bar_width,sizes2020,width=bar_width,tick_label=xlabels,color='#F1E1FF',label='2020年')
# 繪製2021年的長條圖
plt.bar(index+bar_width*2,sizes2021,width=bar_width,tick_label=xlabels,color='#C1FFE4',label='2021年')
# 繪製2022年的長條圖
plt.bar(index+bar_width*3,sizes2022,width=bar_width,tick_label=xlabels,color='#FFC78E',label='2022年')

plt.title('2019~2022年各地區來台目的比較圖',fontproperties=font_prop,rotation=0,fontsize=18)
# 設定 x 軸刻度標籤及對應的文字
plt.xticks(index+bar_width*1.5, labels=xlabels, fontproperties=font_prop)
plt.legend(prop=font_prop)  # 設定標籤使用中文字體
plt.xlabel('來台目的/性質',fontproperties=font_prop,rotation=0,fontsize=12)
plt.ylabel('旅客人數\n(萬人)',fontproperties=font_prop,rotation=0,fontsize=12,ha='right')

# 在每個點的上方加入'合計'的文字標籤
# j+10讓點跟字分開一點，ha:水平對齊，va:垂直對齊
for i, j in enumerate(sizes2019):
    plt.text(i, j+3, f'{j:.2f}', ha='center', va='bottom', fontproperties=font_prop)
for i, j in enumerate(sizes2020):
    plt.text(i+bar_width, j+3, f'{j:.2f}', ha='center', va='bottom', fontproperties=font_prop)
for i, j in enumerate(sizes2021):
    plt.text(i+bar_width*2, j+3, f'{j:.2f}', ha='center', va='bottom', fontproperties=font_prop)
for i, j in enumerate(sizes2022):
    plt.text(i+bar_width*3, j+3, f'{j:.2f}', ha='center', va='bottom', fontproperties=font_prop)

# 儲存圖表
plt.savefig('2019~2022年各地區來台目的比較長條圖',dpi=300)
# 顯示圖表
plt.show()
plt.close()