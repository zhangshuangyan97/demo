import os
import urllib.request
# 构建请求对象
from lxml import etree
from selenium import webdriver
import time
from handless import share_browser

url = "https://www.ishsh.com/sexy"
# brower.execute_script("window.scrollBy(0,4800)")
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
    }
# request = urllib.request.Request(url=url,headers=headers)
# handdler = urllib.request.HTTPHandler()
# opener = urllib.request.build_opener(handdler)
# response = opener.open(request)
# content = response.read().decode("utf-8")
# # print(content)
browser = share_browser()
browser.get(url)
time.sleep(1)
browser.execute_script("document.documentElement.scrollTop=100000")
time.sleep(100)

content = browser.page_source
# 解析
img_xpath = '//div[@class="recent-article cl"]/ul/li/div[@class="post-thumbnail"]/a/img'
tree = etree.HTML(content)
img_list = tree.xpath(img_xpath)
for i in img_list:
    img = i.xpath('./@data-original')[0]
    name =i.xpath('./@alt')[0]
    file_name = name + "." + img.split(".")[-1]
    file_path = os.path.join("xx",file_name)
    urllib.request.urlretrieve(img,file_path)
    print("下载完成")
