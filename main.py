import bar_chart_race as bcr
import pandas as pd
import os.path
import time


inputFile = 'input/a.csv' #输入数据路径
index_col = 'date' #显示的列
outputFile = 'output/' + str(time.time()) +'.mp4' #输出路径
barNumber = 10 # 显示的条形图数量

inputFileArr = os.path.splitext(os.path.basename(inputFile))
inputFileName = inputFileArr[0]
inputFileExt = inputFileArr[1]


parse_dates = [index_col]

if inputFileExt == '.csv':
    df = pd.read_csv(inputFile, index_col=index_col, parse_dates=parse_dates)
elif inputFileExt in ['.xls', '.xlsx']:
    df = pd.read_excel(inputFile, index_col=index_col, parse_dates=parse_dates)
else:
    print('not support input file format')
    quit()

bcr.bar_chart_race(df=df,filename=outputFile, title='三国演义之谁才是主角', n_bars=barNumber, shared_fontdict={'family': 'Microsoft Yahei'})