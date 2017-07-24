# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 14:06:18 2017

@author: Ja
"""

import urllib
import urllib.request
import re


def getUrlList(url,regx):
    html = urllib.request.urlopen(urllib.request.Request(url=url, headers=headers)).read()
    pattern = re.compile(regx)
    url_list = re.findall(pattern, repr(html))
#    print(url_list)
    return url_list
    
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}          #伪装浏览器
regx = r'data-original="(.*?)"'                                                                               #正则
weburl = 'http://www.budejie.com/pic/'                                                                        #不得姐的图片站网址
pages = 10                                                                                                    #前几页



if __name__=="__main__":
    for page in range(1,pages+1):
        print('Downloading page ',page,'!')
        urls = weburl +'%s' %page
        for url in getUrlList(urls, regx):
            urllib.request.urlretrieve(url,'pic/%s' %url.split('/')[-1])                                          #下载到'./pic/'文件夹
        

