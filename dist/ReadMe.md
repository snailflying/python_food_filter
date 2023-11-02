普通使用：

1.将需要处理的Excel另存为input.xlsx，并替换掉原文件夹内的input.xlsx.

2.运行runXlsx (如果被安全机制拦截，请打开系统设置，给run添加权限)

​    方式一、直接双击runXlsx。

​    方式二、打开terminal，cd到run文件所在目录，并运行 ./run

3.用Excel打开output.csv即可。

高级用法：

1.配置人员名单：userList.json

2.指定输入输出文件名称：
./run xxx1.csv  xxx2.csv  userList.json

xxx1.csv：输入文件
xxx2.csv：输入文件