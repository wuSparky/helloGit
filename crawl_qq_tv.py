#!/bin/python
# coding: utf-8

import os
import re
import sys
import urllib2

###############################################################################
##  SUMMARY : crawl tv from qq.com
##  AUTHOR  : wuSpark
##  TIME    : 2016-03-29
###############################################################################

MAXNUM = 10

def download(index):
    '''
        download html according to index
        index : url index
    '''
    url = 'http://v.qq.com/list/2_-1_-1_-1_1_0_%d_20_-1_-1_0_-1.html' % (index)
    try:
        html = urllib2.urlopen(url).read()
    except Exception:
        html = "None"
    return html

def parse(html):
    '''
        parse html and get video title
        html : the original html
    '''
    videos = []
    html = html.strip()
    pattern = r'_hot="tv.title.link.1.">(.+?)</a>'
    find_re = re.compile(pattern, re.DOTALL)
    for item in find_re.findall(html):
        result = dict(
                title = item.decode('utf-8')
                # other items to add, year-director-actor-summary...
        )
        videos.append(result)
    return videos

# MAIN FUNCTION
if __name__ == '__main__':
    for i in range(MAXNUM):
        html = download(i)
        videos = parse(html)
        for item in videos:
            print item['title'].encode('utf-8')
