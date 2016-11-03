# -*- coding: cp936 -*-
#deltaAICrc计算.py
#Dependency: Python 2.7.x
#Author: 纪永坤
#Email: jiyongkun@foxmail.com

#将脚本程序与R软件输出的结果文件放在同一文件夹
#需安装Python 2.7.x 运行环境

import csv
#输入R产生的CSV文件的文件名
file_in_name = raw_input('Please input the name of CSV file:\n')
file_in_csv = csv.reader(open(file_in_name,'rb'))
file_out_models = open(file_in_name + '_models.csv','wb')
file_out_dAICrc = open(file_in_name + '_deltaAICrc.csv','w')
file_out_dAICrc.write(file_in_name +'_dAICrc\n')
#将文件内容读入列表，形成二维数组
file_in = []
for row in file_in_csv:
    file_in.append(row)

#变量初始化
pureBirth = []
bd = []
DDX = []
DDL = []
yule2rate = []
yule3rate = []
dAICrc = []

#从第一棵树的结果开始遍历
line_num = 1 
while(line_num < len(file_in)):
    #将6个模型每个模型的AIC值存入列表
    AIC = []
    for i in range(0,6):
        AIC.append(float(file_in[line_num+i][12]))
    #计算这棵树的deltaAICrc = AICrc - AICrv
    dAICrc = min(AIC[0:2]) - min(AIC[2:])
    print dAICrc
    #将deltaAICrc值写入文件
    file_out_dAICrc.write(str(dAICrc) + '\n')
    #对每个模型的结果列进行汇总
    pureBirth.append(file_in[line_num])
    bd.append(file_in[line_num+1])
    DDX.append(file_in[line_num+2])
    DDL.append(file_in[line_num+3])
    yule2rate.append(file_in[line_num+4])
    yule3rate.append(file_in[line_num+5])
    #步进7行，进入下一棵树的结果
    line_num += 7

#将所有结果列按模型排序，写入文件
csv_out = csv.writer(file_out_models)
csv_out.writerow(file_in[0])
csv_out.writerows(pureBirth)
csv_out.writerows(bd)
csv_out.writerows(DDX)
csv_out.writerows(DDL)
csv_out.writerows(yule2rate)
csv_out.writerows(yule3rate)

file_out_dAICrc.close()
file_out_models.close()
print 'Finished!'
raw_input() 
