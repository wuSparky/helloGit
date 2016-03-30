#!/bin/python
# coding: utf-8

import os
import re
import sys
import urllib2

###############################################################################
##  SUMMARY : crawl movie from qq.com
##  AUTHOR  : JiangLu
##  TIME    : 2016-03-30
###############################################################################

MAXNUM = 5

def download(index):
    url = 'http://v.qq.com/x/movielist/?cate=10001&offset=%d&sort=4.html' % (index)
    try:
        html = urllib2.urlopen(url).read()
    except Exception:
        html = "None"
    return html

def parse(html):
    videos = []
    html = html.strip()
    pattern = r'alt="(.+?)"'
    find_re = re.compile(pattern, re.DOTALL)

    for item in find_re.findall(html):
        result = dict(
                title = item.decode('utf-8')
                # other items to add, year-director-actor-summary...
                )
        videos.append(result)
    return videos

if __name__ == '__main__':
    for i in range(MAXNUM):
        index = i * 20;
        html = download(index)
        videos = parse(html)
        for item in videos:
            print item['title'].encode('utf-8')

