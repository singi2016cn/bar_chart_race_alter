import bar_chart_race as bcr
import pandas as pd
import os.path


inputFile = 'input/a.csv'

inputFileArr = os.path.splitext(os.path.basename(inputFile))
inputFileName = inputFileArr[0]
inputFileExt = inputFileArr[1]

outputFile = 'output/' + inputFileName +'.mp4'
index_col = 'date'
parse_dates = [index_col]

if inputFileExt == '.csv':
    df = pd.read_csv(inputFile, index_col=index_col, parse_dates=parse_dates)
elif inputFileExt in ['.xls', '.xlsx']:
    df = pd.read_excel(inputFile, index_col=index_col, parse_dates=parse_dates)
else:
    print('not support input file format')
    quit()

bcr.bar_chart_race(df=df,filename=outputFile)