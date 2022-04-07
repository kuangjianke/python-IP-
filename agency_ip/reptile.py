from agency_ip.mysql_connect import out_datas
from agency_ip.mysql_connect import input_data

import requests
from lxml import etree
import time
import random
import re

headers = {
    'UserAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}


def reptile(url, n, v):
    time.sleep(random.random() + 1)  # 爬虫缓存时间
    html = requests.get(url, headers=headers)  # 获取网页
    html = etree.HTML(html.text)  # xpath获取数据
    data1 = html.xpath('//*[@id="list"]/table/tbody/tr/td[1]/text()')  # xapth获取数据,ip
    data2 = html.xpath('//*[@id="list"]/table/tbody/tr/td[2]/text()')  # 端口
    data3 = html.xpath('//*[@id="list"]/table/tbody/tr/td[4]/text()')  ##类型
    data4 = html.xpath(f'//*[@id="list"]/table/tbody/tr/td[{n}]/text()')  # 时间
    print('\r插入数据中' + '.' , end=' ')  # 输出更新页数
    return data1, data2, data3, data4  # 返回获取到的ip数据


def html_data4(html, z):
    time.sleep(random.random() + 1)  # 爬虫缓存时间
    ip = html.xpath('//*[@class="layui-table"]/tbody/tr/td[1]/text()')  # xapth获取数据
    duanko = html.xpath('//*[@class="layui-table"]/tbody/tr/td[2]/text()')  # xapth获取数据
    date = html.xpath('//*[@class="layui-table"]/tbody/tr/td[5]/text()')  # xapth获取数据
    ip_list, duanko_list, date_list = [], [], []
    for i in range(len(ip)):
        ip_list.append(ip[i].replace('\n', '').replace('\t', ''))
        duanko_list.append(duanko[i].replace('\n', '').replace('\t', ''))
        date_list.append(date[i].replace('\n', '').replace('\t', ''))
    leixin_list = ['HTTPS'] * len(ip_list)
    print('\r插入数据中' + '.' , end=' ')  # 输出更新页数
    return ip_list, duanko_list, leixin_list, date_list  # 返回获取到的ip数据


def html_data5(html, i):
    time.sleep(random.random() + 1)  # 爬虫缓存时间
    ip = html.xpath('//*[@id="content"]/section/div[2]/table/tbody/tr/td[1]/text()')  # xapth获取数据
    duanko = html.xpath('//*[@id="content"]/section/div[2]/table/tbody/tr/td[2]/text()')  # xapth获取数据
    http = html.xpath('//*[@id="content"]/section/div[2]/table/tbody/tr/td[4]/text()')  # xapth获取数据
    date = html.xpath('//*[@id="content"]/section/div[2]/table/tbody/tr/td[7]/text()')  # xapth获取数据
    date = list(map(lambda x: str(x).replace('-', '/'), date))
    print('\r插入数据中' + '.' , end=' ')  # 输出更新页数
    return ip, duanko, http, date  # 返回获取到的ip数据


def html_data6(htmls, n):
    time.sleep(random.random() + 1)  # 爬虫缓存时间
    data = re.findall('<td>(.*?)</td>', htmls.text)
    list = [0, 1, 4]
    ip, duanko, date, dates = [], [], [], []
    for j in list:
        for i in range(j, len(data), 5):
            ip.append(data[i]) if j == 0 else ...
            duanko.append(data[i]) if j == 1 else ...
            date.append(data[i]) if j == 4 else ...
    for i in date[1:]:
        da = re.findall('\d+', str(i))
        dates.append(f'{da[0]}/{da[1]}/{da[2]} {da[3]}:00:00')
    print('\r插入数据中' + '.' , end=' ')  # 输出更新页数
    leixin_list = ['HTTPS'] * len(ip[1:])
    return ip[1:], duanko[1:], leixin_list, dates  # 返回获取到的ip数据


def html_data7(html):
    ip = html.xpath('/html/body/div/div[1]/div/table/tbody/tr/td[1]/text()')
    http = html.xpath('/html/body/div/div[1]/div/table/tbody/tr/td[2]/text()')
    ip_list, duanko_list = [], []
    for i in ip:
        da = i.split(':')
        ip_list.append(da[0])
        duanko_list.append(da[1])
    http = list(map(lambda x: x[:-2], http))
    date_list = ['2020/11/11 11:11:11'] * len(ip_list)
    print('\r插入数据中' + '.', end=' ')  # 输出更新页数
    return ip_list, duanko_list, http, date_list  # 返回获取到的ip数据


def html_data8(htmls):
    ip = htmls.xpath(f'//*[@class="panel-body"]/div[2]/text()')
    ips, duanko = [], []
    for i in range(1, len(str(ip).split('@HTTP'))):
        ipdata = str(htmls.xpath(f'//*[@class="panel-body"]/div[2]/text()[{i}]')).replace(' ', '')
        datas = re.findall("n(.*?):(.*?)@HTTP", ipdata)
        ips.append(datas[0][0])
        duanko.append(datas[0][1])
    date_list = ['2020/11/11 11:11:11'] * len(ips)
    leixin_list = ['HTTP'] * len(ips)
    print('\r插入数据中' + '.', end=' ')  # 输出更新页数
    return ips, duanko, leixin_list, date_list  # 返回获取到的ip数据


def html_data9(html, s):
    ip = re.findall('span>(.*?)<', html.text)
    duanko = re.findall('<td>(.*?)<', html.text)
    list = [1, 3, 6]
    http, duankos, dates, = [], [], []
    for j in list:
        for i in range(j, len(duanko), 7):
            duankos.append(duanko[i]) if j == 1 else ...
            http.append(duanko[i]) if j == 3 else ...
            dates.append(str(duanko[i]).replace('\\', '')) if j == 6 else ...
    print('\r插入数据中' + '.' , end=' ')  # 输出更新页数
    return ip, duankos, http, dates  # 返回获取到的ip数据


def url_data1(max_time):  # 网络获取ip代理
    for i in range(1, 11):  # 循环页数
        url = f'http://www.ip3366.net/?stype=1&page={i}'  # 访问的ip地址url
        data = reptile(url, 8, i)  # 取数据
        if input_data(data, max_time[0], 1) == False:  # 是否继续爬取数据
            break
    print('插入完成1/9')


def url_data2(max_time):  # ip_url
    for i in range(1, 8):  # 循环页数
        url = f'http://www.ip3366.net/free/?stype=1&page={i}'  # 访问的ip地址url
        data = reptile(url, 7, i)  # 取数据
        if input_data(data, max_time[1], 2) == False:  # 是否继续爬取数据
            break
    print('插入完成2/9')


def url_data3(max_time):  # 不同页面的数据归于一个爬虫
    for i in range(1, 8):  # 循环页数
        url = f'http://www.ip3366.net/free/?stype=2&page={i}'  # 访问的ip地址url
        data = reptile(url, 7, i)  # 取数据
        if input_data(data, max_time[2], 3) == False:  # 是否继续爬取数据
            break
    print('插入完成3/9')


def url_data4(max_time):  # ----------
    for z in range(1, 22):
        url = f'https://www.89ip.cn/index_{z}.html'
        html = requests.get(url, headers=headers)
        html = etree.HTML(html.text)  # xpath获取数据
        data = html_data4(html, z)
        if input_data(data, max_time[3], 4) == False:  # 是否继续爬取数据----------
            break
    print('插入完成4/9')


def url_data5(max_time):
    for i in range(1, 11):
        url = f'https://www.7yip.cn/free/?action=china&page={i}'
        html = requests.get(url, headers=headers)
        html = etree.HTML(html.text)  # xpath获取数据
        data = html_data5(html, i)
        if input_data(data, max_time[4], 5) == False:  # 是否继续爬取数据----------
            break
    print('插入完成5/9')


def url_data6(max_time):
    for n in range(1, 11):
        url = f'http://www.66ip.cn/{n}.html'
        htmls = requests.get(url, headers=headers, timeout=2)
        htmls.encoding = 'gb2312'
        data = html_data6(htmls, n)
        if input_data(data, max_time[5], 6) == False:  # 是否继续爬取数据----------,max_time对比最大时间的位置
            # 后面是写入的序列，根据序列更新时间ip，
            break
    print('插入完成6/9')


def url_data7(max_time):
    url = 'http://www.nimadaili.com/putong/1/'
    html = requests.get(url, headers=headers, timeout=2)
    html = etree.HTML(html.text)  # xpath获取数据
    data = html_data7(html)
    input_data(data, max_time[6], 7)  # 是否继续爬取数据----------,max_time对比最大时间的位置
    print('插入完成7/9')


def url_data8(max_time):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
        'cookie': 'user-key=c31bd399-d9a0-4cb1-bdca-5e509cf23a37; mt_xid=V2_52007VwMVU15ZUFwZSRFdBmQDFltcWVpeGUEYbFFlBBJVVFBaRk1LSl8ZYgYQB0FRVgh'
                  'KVUwLBDJXQVNdWQVZF3kaXQZmHxJTQVlUSx9NElkEbAYSYl9oUWocSB9UAGIzEVVdXg%3D%3D; areaId=18; __jdu=1255193314; PCSYCityID=CN_430000_430200_430202;'
                  ' shshshfpb=wBU63O0padoTM6%2FEXx%2FzeOw%3D%3D; shshshfpa=493c7be7-3595-3da2-157d-8dac055073ef-1591453850; pin=kjk1752; _tp=YOB7fXaeSAYMArWv%2Bs4waA%3D%3D;'
                  ' _pst=kjk1752; unick=kjk1752; ipLocation=%u6e56%u5357; cn=0; ipLoc-djd=18-1495-1496-30767.-1266905523; TrackID=1-oY18P3-FsDIZiyNs4jTtQzG0QfLLAMbl4oM2QWjuB'
                  'WR0BznTCPaSsHUfH0ZPmaHJ-qS7hxXzT0z2rBJU-9VQvyJrYxLElzf1lJ-Rb2tAac; pdtk=RZ7%2B%2BPAQ5u4%2B08i6hyR%2F8OoEuC2PfZmHlfba39x8l0N9K494KGxvJegodpSHWFk6; unpl=V2_ZzNtb'
                  'UAHS0BxXBVScxhbA2IGF18RUkdBd11PAXoRX1JlVxFfclRCFnQURlVnGVsUZwsZXkNcRhBFCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZHs'
                  'aWAFnCxBfQlJzJXI4dmRzHl4GZAoiXHJWc1chVEBWfhtfAioDEVlGV0sXdwhDZHopXw%3d%3d; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_3a'
                  '9d5eb790674443b45e3d8d092f3e23|1602847244778; shshshfp=fb52a64359e5a71ed6cf199f9ac9f8c8; __jda=122270672.1255193314.1602403743.1602842118.1602846263.26; __jdc=122270672; 3AB9D23'
                  'F7A4B3C9B=USQAP45O2F5FSYBLCUPNAPAWH4NEMIRJCRKC7RP4RQJJ5LEQ7H4SIKYSZQBJLDAKURZYIYV4L26NVHHMDO5KMYB4H4; __jdb=122270672.23.1255193314|26.1602846263; shshshsID=e697c5dd0bc27ea5b895249483c5b1a5_23_1602849940243'
    }  # 加头部信息，和cookie

    url = 'https://proxy.coderbusy.com/zh-hans/ops/daily.html'
    html = requests.get(url, headers=headers, timeout=2)
    data = re.findall('href="/zh-hans/ops/daily/topics/(.*?).html"', html.text)[0]
    url = f'https://proxy.coderbusy.com/zh-hans/ops/daily/topics/{data}.html'
    htmls = requests.get(url, headers=headers, timeout=2)
    htmls = etree.HTML(htmls.text)  # xpath获取数据
    data = html_data8(htmls)
    input_data(data, max_time[7], 8)  # 是否继续爬取数据----------,max_time对比最大时间的位置
    print('插入完成8/9')


def url_data9(max_time):
    for s in range(1, 189):
        datas = {'page': f'{s}'}
        url = 'http://wapi.http.cnapi.cc/index/index/get_free_ip'
        html = requests.post(url, headers=headers, data=datas, timeout=2)
        data = html_data9(html, s)
        if input_data(data, max_time[8], 9) == False:  # 是否继续爬取数据----------,max_time对比最大时间的位置
            # 后面是写入的序列，根据序列更新时间ip，
            break
    print('插入完成9/9')


def reptile_main():  # 由数据库验证模块启动
    max_time = []  # 获取更新的最新时间
    for i in range(1, 9 + 1):  # 爬虫有多少个就写多少序列-------------
        date = out_datas(i)  # 获取三个爬虫的最新ip更新时间
        max_time.append(date)  # 追加最新时间
    url_data1(max_time)  # 运行爬虫
    url_data2(max_time)  # 运行爬虫
    url_data3(max_time)  # 运行爬虫-
    url_data4(max_time)  # 爬虫4----------89代理
    url_data5(max_time)  # 齐云代理
    url_data6(max_time)  # 66代理
    url_data7(max_time)  # 免费代理,有小羊图标
    # url_data8(max_time)  # 代理盒子，每日代理  cookie过期
    url_data9(max_time)  # 芝麻http
# 检验最后的[1007 == 1007]，添加新爬虫就加一
# 更新时间序列，时间序列+1
# 为数据库添加时间
