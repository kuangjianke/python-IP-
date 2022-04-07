from agency_ip.ip_main import mains
import requests
import random
import re
import time
import requests
import re
url='https://www.jiamengfei.com/xm/301610'
headers='''
authority: www.jiamengfei.com
method: GET
path: /xm/301610
scheme: https
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9
cache-control: max-age=0
cookie: UM_distinctid=17be87af3ad70b-04c7d3445c420e-4343363-144000-17be87af3aeae5; CNZZDATA1256598819=895200779-1631684597-%7C1631695405; Hm_lvt_23fe168a1d83f488d040c8321779ac06=1631689723,1631690486,1631693972,1631700646; Hm_lpvt_23fe168a1d83f488d040c8321779ac06=1631701894
referer: https://www.jiamengfei.com/2?page=2
sec-ch-ua: "Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"
sec-ch-ua-mobile: ?0
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: same-origin
sec-fetch-user: ?1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36
'''
def dict_data(appd_data):  # 公开的头部格式化函数
    print_data = {}

    for i in appd_data.splitlines():
        if i or 'None' != 'None':  # 将空行去除
            html = re.findall('(.*?): (.*?$)', i)
            if html != []:
                print_data[html[0][0].replace(' ','')] = html[0][1]
            else:
                assert html, f'{i}头部信息格式错误'

    return print_data

headers=dict_data(headers)

data=mains('https://www.jiamengfei.com/2?',headers)
#
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
#     'cookie': 'user-key=c31bd399-d9a0-4cb1-bdca-5e509cf23a37; mt_xid=V2_52007VwMVU15ZUFwZSRFdBmQDFltcWVpeGUEYbFFlBBJVVFBaRk1LSl8ZYgYQB0FRVghKVUwLBDJXQVNdWQVZF3kaXQZmHxJTQVlUSx9NElkEbAYSYl9oUWocSB9UAGIzEVVdXg%3D%3D; areaId=18; __jdu=1255193314; PCSYCityID=CN_430000_430200_430202; shshshfpb=wBU63O0padoTM6%2FEXx%2FzeOw%3D%3D; shshshfpa=493c7be7-3595-3da2-157d-8dac055073ef-1591453850; pin=kjk1752; _tp=YOB7fXaeSAYMArWv%2Bs4waA%3D%3D; _pst=kjk1752; unick=kjk1752; ipLocation=%u6e56%u5357; cn=0; ipLoc-djd=18-1495-1496-30767.-1266905523; TrackID=1-oY18P3-FsDIZiyNs4jTtQzG0QfLLAMbl4oM2QWjuBWR0BznTCPaSsHUfH0ZPmaHJ-qS7hxXzT0z2rBJU-9VQvyJrYxLElzf1lJ-Rb2tAac; pdtk=RZ7%2B%2BPAQ5u4%2B08i6hyR%2F8OoEuC2PfZmHlfba39x8l0N9K494KGxvJegodpSHWFk6; unpl=V2_ZzNtbUAHS0BxXBVScxhbA2IGF18RUkdBd11PAXoRX1JlVxFfclRCFnQURlVnGVsUZwsZXkNcRhBFCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZHsaWAFnCxBfQlJzJXI4dmRzHl4GZAoiXHJWc1chVEBWfhtfAioDEVlGV0sXdwhDZHopXw%3d%3d; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_3a9d5eb790674443b45e3d8d092f3e23|1602847244778; shshshfp=fb52a64359e5a71ed6cf199f9ac9f8c8; __jda=122270672.1255193314.1602403743.1602842118.1602846263.26; __jdc=122270672; 3AB9D23F7A4B3C9B=USQAP45O2F5FSYBLCUPNAPAWH4NEMIRJCRKC7RP4RQJJ5LEQ7H4SIKYSZQBJLDAKURZYIYV4L26NVHHMDO5KMYB4H4; __jdb=122270672.23.1255193314|26.1602846263; shshshsID=e697c5dd0bc27ea5b895249483c5b1a5_23_1602849940243'
# }  # 加头部信息，和cookie
# for i in range(10000):
#     data=mains('https://www.tipdm.org/bdrace/jljingsai/20200903/1688.html?cName=ral_101',headers)

# lists = [i for i in range(1,200,2)]
# random.shuffle(lists)
# for c,i in enumerate(reversed(lists)):
#     if c % 5 == 0:
#         time.sleep(10)
#     try:
#         url=f'https://search.jd.com/Search?keyword=%E7%AC%94%E8%AE%B0%E6%9C%AC&wq=%E7%AC%94%E8%AE%B0%E6%9C%AC&page={i}&s=56&click=0'
#         html=requests.get(url,headers=headers,proxies=random.choice(data),timeout=3)
#         print(html)
#         id_list = re.findall('<li data-sku="(.*?)"', html.text)  # 正则匹配
#         asi=id_list or html.text
#         print(asi)
#         if 'window.location.href=' in asi:
#             assert False,''
#         random.shuffle(id_list)
#         for n,j in enumerate(reversed(id_list)):
#             try:
#                 urls = f'https://item.jd.com/{j}.html'
#                 htmls = requests.get(url,headers=headers, proxies=random.choice(data),timeout=3)
#                 url_data = f'https://p.3.cn/prices/mgets?callback=jQuery2173954&type=1&area=18_1488_29447_0&pdtk=&pduid=1598425172740890368605&pdpin=&pin=null&pdbp=0&skuIds=J_{j}&ext=11100000&source=item-pc'
#                 try:
#                     htmla = requests.get(url_data, headers=headers,proxies=random.choice(data), timeout=3)
#                     price = re.findall('"p":"(.*?)","op":', htmla.text)
#                     print(price or f'none ',f'爬取{c}页的第{n}个数据',)
#                 except:
#                     print('价格内容响应超时')
#             except:
#                 print('商品内容响应超时')
#     except:
#         print('ip响应超时')
