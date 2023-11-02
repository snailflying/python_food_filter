import csv
import sys
import os



args = sys.argv
current_dir, filename = os.path.split(os.path.abspath(sys.argv[0]))
inputFile = current_dir + os.sep + 'input.csv' if len(args) < 2 else args[1]
outFile = current_dir + os.sep + 'output.csv' if len(args) < 3 else args[2]
logPath = current_dir + os.sep + 'log'
userList = ['大强','小征','小杰','林江','庚顺','阿木','千御','球球']

with open(inputFile) as csvFile:
    # 创建一个 CSV Reader 对象
    reader = csv.reader(csvFile)
    logOutput = open(logPath, 'w')
    # 设置行数所以我们知道哪一行的标题
    with open(outFile, mode='w') as output:
        writer = csv.writer(output,
                            delimiter=',',
                            quotechar='"',
                            quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['姓名', '菜品'])
        line = 0
        foodDict = dict()
        for row in reader:
            userName = row[0]
            line += 1
            if not userName in userList:
                continue
            food = row[1]
            if food in foodDict.keys():
                foodDict[food] = foodDict[food]+1
            else:
                foodDict[food] = 1
            printLine = '第' + str(line) + '行:'
            print(printLine, userName, food)
            writer.writerow([userName, food])
        writer.writerow('')
        writer.writerow(['菜品', '数量'])
        for foodKey in foodDict.keys():
            writer.writerow([foodKey, foodDict[foodKey]])
    logOutput.close()
