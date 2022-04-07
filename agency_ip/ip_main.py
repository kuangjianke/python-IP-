from agency_ip.mysql_connect import *
from agency_ip.reptile import *
#flask_dome  mysql
def mains(url,headers):
    db = pymysql.connect('localhost', 'root', '000000', 'ip_data')
    cusor = db.cursor()  # 通过获取到的数据库连接db下的cursor()方法来创建游标
    sql = 'select count(ip) FROM ip_data ;'
    cusor.execute(sql)  # 运行sql
    len_data=cusor.fetchall()[0][0]
    max_data=500
    if  len_data < max_data:
        print(f'数据库数据:[{len_data}] 小于规定 [{max_data}] 条,数据插入...')
        reptile_main()  # 爬取最新的数据并保存到数据
    else:
        print(f'数据库数据:[{len_data}] 大于规定 [{max_data}] 条,跳过数据插入')
    ip_list = []
    ip_list_data=Validate_database()
    print(f'可用ip{ip_list_data}')
    print('对url进行测试中...')
    for i in ip_list_data:
        try:
            html = requests.get(url, headers=headers, proxies=i, timeout=1)
            if html.status_code == 200 and len(html.text)>250:
                ip_list.append(i)
        except:
            ...
    print(f'测试后对url的可用ip{ip_list}')
    return ip_list