#!/bin/python
# coding: utf-8

import os
import re
import sys
import urllib2

###############################################################################
##  SUMMARY : crawl now playing movie from douban.com
##  AUTHOR  : JiangLu
##  TIME    : 2016-03-31
###############################################################################

def download():
    url = 'https://movie.douban.com/nowplaying/beijing/'
    try:
        html = urllib2.urlopen(url).read()
    except Exception:
        html = "None"
    return html

def parse(html):
    videos = []
    html = html.strip()
    pattern1 = r'<h2>正在上映</h2>(.+?)<h2>即将上映'
    find_re1 = re.compile(pattern1, re.DOTALL)
    pattern2 = r'class="list-item.*?data-title="(.+?)".*?data-score="(.*?)"'
    find_re2 = re.compile(pattern2, re.DOTALL)

    extent = ('').join(find_re1.findall(html))
    for item in find_re2.findall(extent):
        result = dict(
                title = item[0].decode('utf-8'),
                score = item[1]
                # other items to add, year-director-actor-summary...
                )
        videos.append(result)
    return videos

if __name__ == '__main__':
        html = download()
        videos = parse(html)
        print '电影名称' + '\t' + '豆瓣评分'
        for item in videos:
            print item['title'].encode('utf-8') + '\t' + item['score']

