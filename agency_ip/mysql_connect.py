import datetime
import requests
import pymysql
import threading
import time

def pymysqls(sql, ager):  # 数据库操作
    db = pymysql.connect('localhost', 'root', '000000', 'ip_data')
    cusor = db.cursor()  # 通过获取到的数据库连接db下的cursor()方法来创建游标
    cusor.execute(sql, ager)#运行sql
    return cusor.fetchall(), cusor, db#返回数据，游标，数据库方法


class TEST(object):
    def __init__(self, i, ip_data, data_values,verify_list):  # 不同的http访问不同的网页
        self.verify_list=verify_list
        self.data_values = data_values#实例化数据
        self.ip_data = ip_data#实例化数据
        self.i = i#实例化数据
        if i[0] == 'HTTPS':#判断代理ip格式，来访问不同的连接
            url = 'https://myexternalip.com/raw'
            self.requestsc(url)
        elif i[0] == 'HTTP':
            url = 'http://api.ipify.org/'
            self.requestsc(url)

    def requestsc(self, url):  # ip地址测试，可以用则通过，不可用置信度-1
        try:#错误处理
            dict_data = {f'{str.lower(self.i[0])}': f'{self.i[1]}:{self.i[2]}'}#创建ip格式
            html = requests.get(url, proxies=dict_data, timeout=1)#获取ip响应，返回ip
            if html.text == self.i[1]:  # 判断ip是否响应和是否隐藏了自己的ip
                self.ip_data.append(dict_data)#添加可用数据
                self.data_values.release()#多线程的结束
            else:
                assert False ,''
        except:
            sql = "UPDATE ip_data SET 置信度=%s WHERE http=%s and ip=%s and 端口= %s;"#sql语句
            dd = pymysqls(sql, [int(self.i[4]) + 1, self.i[0], self.i[1], self.i[2]])#更新置信度
            dd[2].commit()#提交减低置信度的更新
            dd[1].close()  # 关闭数据库
            self.data_values.release()
        self.verify_list.append(self.i)


def databaestes():

    sql = 'DELETE FROM ip_data WHERE 置信度>%s;' # 更新数据库，删除无用ip和读取数据
    d1 = pymysqls(sql, [2])#判断置信度大于2，将删除ip使用
    d1[2].commit()#提交信息
    d1[1].close()  # 关闭数据库

    sql = f'SELECT http,ip,端口,序列,置信度 FROM ip_data;'
    db = pymysql.connect('localhost', 'root', '000000', 'ip_data')#数据库的连接账号，密码和数据库
    cusor = db.cursor()  # 通过获取到的数据库连接db下的cursor()方法来创建游标
    cusor.execute(sql)#运行sql语句
    data = list(cusor.fetchall())#返回数据库的数据，类型list
    db.close()  # 关闭数据库
    return data#返回数据库数据


#验证数据
#判断ip是否可以隐藏本机ip
#数据库验证模块
def Validate_database():  # 多线程，循环每一个ip进行测试
    ip_data = []#创建可使用爬虫ip
    verify_list=[]
    file_size=0
    data = databaestes()#数据库数据
    max_threading=50
    print(f'使用线程:[{max_threading}]')
    data_values = threading.BoundedSemaphore(max_threading)  # 线程个数
    for j, i in enumerate(reversed(data)):#反向循环数据库，因为数据最新的写入在最后面，先后差别不大
        file_size = len(list(data))#总数据有多少，用于进度条模块
        vlaue = j + 1#验证ip地址的进度条
        ratio = vlaue / file_size * 100  # 在总量的百分比
        print("\r{}{:.2f}%[{}>{}]请等待...".format(f"{file_size}/{vlaue}  ", ratio, int(ratio) * '█',
                                                (100 - int(ratio)) * "."), end='')#输出进度条
        data_values.acquire()  # 确认多线程启动
        threading.Thread(target=TEST, args=(i, ip_data, data_values,verify_list)).start()#多线程启动
    print()
    while...:
        time.sleep(0.5)
        len_list=len(verify_list)+9#---------------加了爬虫就加1
        if len_list==file_size:
            print(f'\r数据更新更新完以成 》》》[{len_list} == {file_size}]《《《',end='')
            break
        else:
            print(f'\r确认数据更新中... 》》》[{len_list} != {file_size}]《《《',end='')
    print('')#不在进度条后面输出
    return ip_data#返回可以使用


def out_datas(i):  # 爬虫ip的最最近更新的ip时间
    sql = f'select datetime FROM ip_data WHERE 序列={i} ORDER BY datetime desc LIMIT %s;'#查询不同序列最新时间的sql语句
    data = pymysqls(sql, [1])[0]#根据爬虫序列来确定最新时间
    a = data[0][0]
    if a.second==0:
        a = f"((datetime.datetime({a.year}, {a.month}, {a.day}, {a.hour}, {a.minute}, {1}),),)"
    else:
        a = f"((datetime.datetime({a.year}, {a.month}, {a.day}, {a.hour}, {a.minute}, {a.second}),),)"
    data = datetime.datetime.strptime(a, "((datetime.datetime(%Y, %m, %d, %H, %M, %S),),)")#格式时间参数，用来对比后面爬取的时间
    return data#返回数据


def input_data(data, max_time, j):  # 保存数据，判断数据时间是否更新
        for i in range(len(data[0])):#保存爬取下来的数据
            print(f'\r插入数据中.{data[0][i]}', end=' ')
            strftime = datetime.datetime.strptime(data[3][i], "%Y/%m/%d %H:%M:%S")#判断时间，用于对比数据库最新时间
            if strftime >= max_time:#爬取数据的时间和更新时间的对比
                sql = 'insert into ip_data values(%s,%s,%s,%s,%s,%s)'  # 插入数据
                try:
                    dbs = pymysqls(sql, [data[0][i], data[1][i], data[2][i], data[3][i], j, 0])#写入数据
                    dbs[2].commit()#提交保存数据
                except:
                    return False
            else:#如果小于数据库最新时间，将停止整个页面的爬取
                return False  # 不继续爬取数据

