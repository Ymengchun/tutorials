try:
    file = open('eeee', 'r+')   #r+：以可读可写的方式打开文件，若文件不存在则报错
except Exception as e:
    print('there is no file named as eeeee')
    response = input('do you want to create a new file')    #用户输入
    if response =='y':
        file = open('eeee','w') #以不可读的方式打开文件，若文件不存在则创建一个
    else:
        pass    #占位语句
else:
    file.write('ssss')
file.close()


