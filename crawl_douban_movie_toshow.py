#!/bin/python
# coding: utf-8

import os
import re
import sys
import urllib2

###############################################################################
##  SUMMARY : crawl to show movie from douban.com
##  AUTHOR  : JiangLu
##  TIME    : 2016-03-31
###############################################################################

def download():
    url = 'https://movie.douban.com/later/beijing/'
    try:
        html = urllib2.urlopen(url).read()
    except Exception:
        html = "None"
    return html

def parse(html):
    videos = []
    html = html.strip()
    pattern = r'<div class="intro">.*? class="">(.+?)</a>.*?<li class="dt">(.+?)</li>'
    find_re = re.compile(pattern, re.DOTALL)

    for item in find_re.findall(html):
        result = dict(
                title = item[0].decode('utf-8'),
                date = item[1].decode('utf-8')
                # other items to add, year-director-actor-summary...
                )
        videos.append(result)
    return videos

if __name__ == '__main__':
        html = download()
        videos = parse(html)
        print '电影名称' + '\t' + '上映日期'
        for item in videos:
            print item['title'].encode('utf-8') + '\t' + item['date'].encode('utf-8')

