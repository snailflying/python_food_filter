import csv
import sys
import os
import openpyxl
import json

args = sys.argv
current_dir, filename = os.path.split(os.path.abspath(sys.argv[0]))
# 输入文件
inputFile = current_dir + os.sep + 'input.xlsx' if len(args) < 2 else args[1]
# 输出文件
outFile = current_dir + os.sep + 'output.csv' if len(args) < 3 else args[2]
# 人员名单Json
userFile = current_dir + os.sep + 'userList.json' if len(args) < 2 else args[3]


def readUserList():
    if not os.path.exists(userFile):
        return ["大强", "小征", "小杰", "林江", "庚顺", "蔡晶", "阿木", "千御", "球球"]
    with open(userFile, 'r') as userJsonFile:
        jsonOut = json.load(userJsonFile)
        return jsonOut


def openExcelSheet1Rows():
    wb = openpyxl.load_workbook(inputFile)
    sheetNames = wb.sheetnames
    table = wb[sheetNames[0]]
    reader = table.rows
    return reader


userList = readUserList()
excelRows = openExcelSheet1Rows()

with open(outFile, mode='w') as output:
    writer = csv.writer(output,
                        delimiter=',',
                        quotechar='"',
                        quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['姓名', '菜品'])
    lineNumber = 0
    foodDict = dict()
    for row in excelRows:
        line = [col.value for col in row]
        userName = line[1]
        lineNumber += 1
        if not userName in userList:
            continue
        food = line[4]
        if food in foodDict.keys():
            foodDict[food] = foodDict[food] + 1
        else:
            foodDict[food] = 1
        printLine = '第' + str(lineNumber) + '行:'
        print(printLine, userName, food)
        writer.writerow([userName, food])
    writer.writerow('')
    writer.writerow(['菜品', '数量'])
    for foodKey in foodDict.keys():
        writer.writerow([foodKey, foodDict[foodKey]])
