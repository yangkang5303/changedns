import urllib.request
import json
from bs4 import BeautifulSoup
api_url = 'https://api.godaddy.com/v1/domains/fkce.me/records'

def get_ip():
    url = 'http://www.net.cn/static/customercare/yourip.asp'
    req = urllib.request.Request(url)
    rsp =urllib.request.urlopen(req)
    html =rsp.read().decode('utf-8' ,"ignore")
    html =BeautifulSoup(html ,'html.parser')
    iph2 =html.h2
    global ip
    ip =iph2.get_text()
    return ip

def update_NS(api_url, ip_addr):
    head = {}
    head['Accept'] = 'application/json'
    head['Content-Type'] = 'application/json'
    head['Authorization'] = 'sso-key $key:$secret'

    records_a = {
        "data": ip_addr,
        "name": "@",
        "ttl": 600,
        "type": 'A',
    }
    records_NS01 = {
        "data": "ns07.domaincontrol.com",
        "name": "@",
        "ttl": 3600,
        "type": "NS",
    }
    records_NS02 = {
        "data": "ns08.domaincontrol.com",
        "name": "@",
        "ttl": 3600,
        "type": "NS",
    }
    put_data = [records_a, records_NS01, records_NS02]

    try:
        req = urllib.request.Request(api_url, headers=head, data=json.dumps(put_data).encode(), method="PUT")
        rsp = urllib.request.urlopen(req)
        code = rsp.getcode()
        if code == 200:
            print('成功更改域名解析：' + ip_addr)
        else:
            print('更改失败！')
    except:
        print('错误！')
ACTIP = get_ip()
update_NS(api_url,ACTIP)