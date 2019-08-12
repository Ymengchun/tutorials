
import time #导入time模块
print(time.localtime()) #本地时间

import time as t
print(t.localtime())  #为模块起别名

from time import localtime, time
print(localtime())
print(time())

from time import *
print(localtime())
