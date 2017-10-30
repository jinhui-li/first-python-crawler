# coding:utf-8

import codecs
import ConfigParser
import re
import time
import urllib2
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

content_file = "/home/lijinhui/content.ini"
company_name_file = "/home/lijinhui/company_name.txt"

config = ConfigParser.ConfigParser()
with open(content_file, 'r') as f:
    config.readfp(f)
    start_id = int(config.get('content_id', 'start_id'))
    step = int(config.get('content_id', 'step'))
    loop = int(config.get('content_id', 'loop'))

while True:
    company_list = []
    for i in xrange(step):
        try:
            content_id = str(start_id + i)
            url = 'http://b2b.huangye88.com/qiye%s/' % content_id
            request = urllib2.Request(url)
            request.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6')
            opener = urllib2.build_opener()
            page = opener.open(request)
            html = page.read().decode('utf-8')
#            print(html)
            if "province=北京;city=北京" in html:
                title = re.findall(r"<title>(.*)</title>", html)
                company_name = content_id + title[0]
                print(company_name)
                company_list.append(company_name)
        except:
            pass
    with codecs.open(company_name_file, 'w', 'utf-8') as cf:
        for company in company_list:
            cf.write(company + '\r\n')
    print("End")
    time.sleep(loop)
