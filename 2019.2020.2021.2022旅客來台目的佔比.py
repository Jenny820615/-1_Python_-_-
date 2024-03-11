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
           
# 輸入2019標籤資料
sizes=allvalues2019
labels=xlabels
colors=['#FFE6FF','#FFBB77','#FFFFB9','#ACD6FF','#CECEFF','#DFFFDF']
explode=(0.05,0.05,0.05,0.05,0.05,0.05)
# 繪製2019圓餅圖
plt.pie(sizes,explode,labels=labels,colors=colors, autopct='%1.1f%%',textprops={'fontproperties': font_prop})
plt.axis('equal')  # 讓圓餅圖比例相等
plt.title('2019年旅客來台目的佔比', fontproperties=font_prop,fontsize=12)
# 儲存2019圖表
plt.savefig('2019年旅客來台目的佔比.png',dpi=300)
plt.close()

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
           
# 輸入2020標籤資料
sizes=allvalues2020
# 繪製2020圓餅圖
plt.pie(sizes,explode,labels=labels,colors=colors, autopct='%1.1f%%',textprops={'fontproperties': font_prop})
plt.axis('equal')  # 讓圓餅圖比例相等
plt.title('2020年旅客來台目的佔比', fontproperties=font_prop,fontsize=12)
# 儲存2020圖表
plt.savefig('2020年旅客來台目的佔比.png',dpi=300)
plt.close()

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
           
# 輸入2021標籤資料
sizes=allvalues2021
explode2021=(0.05,0.05,0.05,0.5,0.05,0.05)
# 繪製2021圓餅圖
plt.pie(sizes,explode=explode2021,labels=labels,colors=colors, autopct='%1.1f%%',textprops={'fontproperties': font_prop})
plt.axis('equal')  # 讓圓餅圖比例相等
plt.title('2021年旅客來台目的佔比', fontproperties=font_prop,fontsize=12)
# 儲存2021圖表
plt.savefig('2021年旅客來台目的佔比.png',dpi=300)
plt.close()

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
           
# 輸入2022標籤資料
sizes=allvalues2022
# 繪製2022圓餅圖
plt.pie(sizes,explode,labels=labels,colors=colors, autopct='%1.1f%%',textprops={'fontproperties': font_prop})
plt.axis('equal')  # 讓圓餅圖比例相等
plt.title('2022年旅客來台目的佔比', fontproperties=font_prop,fontsize=12)
# 儲存2022圖表
plt.savefig('2022年旅客來台目的佔比.png',dpi=300)
plt.close()