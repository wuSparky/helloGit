#!/bin/python
# coding: utf-8

import os
import re
import sys
import urllib2

###############################################################################
##  SUMMARY : 豆瓣最受关注的图书榜
##  AUTHOR  : JiangLu
##  TIME    : 2016-04-01
###############################################################################

def getHtml(url):
    try:
        html = urllib2.urlopen(url).read()
    except Exception:
        html = "None"
    return html

def getLink(html):
    link = []
    html = html.strip()
    patten = r'<a class="fleft" href="(.+?)">'
    find_re = re.compile(patten,re.DOTALL)

    for item in find_re.findall(html):
        result = item
        link.append(result)
    return link

def getBookInf(html):
    html = html.strip()

    title_pattern = r'<span property="v:itemreviewed">(.+?)</span>'
    author_patten = r'作者</span>:.+?>(.+?)</a>'
    price_patten = r'定价:</span>(.+?)<br/>'
    score_patten = r'property="v:average">(.+?)</strong>'
    content_patten1 = r'内容简介.+?class="all hidden".+?class="intro">(.+?)</p></div>'
    content_patten2 = r'内容简介.+?class="intro">(.+?)</p></div>'

    find_title = re.compile(title_pattern, re.DOTALL).findall(html)
    find_author = re.compile(author_patten,re.DOTALL).findall(html)
    find_price = re.compile(price_patten, re.DOTALL).findall(html)
    find_score = re.compile(score_patten, re.DOTALL).findall(html)
    find_content1 = re.compile(content_patten1, re.DOTALL).findall(html)
    find_content2 = re.compile(content_patten2, re.DOTALL).findall(html)

    result = dict()
    if len(find_title):
        result['title'] = find_title.pop().decode('utf-8')
    if len(find_author):
        result['author'] = find_author.pop().decode('utf-8')
    if len(find_price):
        result['price'] = find_price.pop().decode('utf-8')
    if len(find_score):
        result['score'] = find_score.pop().decode('utf-8')

    if len(find_content1):
        temp = find_content1.pop().decode('utf-8')
        temp = temp.replace('</p>', ' ')
        temp = temp.replace('<p>', ' ')
        result['content'] = temp
    elif len(find_content2):
        temp = find_content2.pop().decode('utf-8')
        temp = temp.replace('</p>', ' ')
        temp = temp.replace('<p>', ' ')
        result['content'] = temp
    return result

if __name__ == '__main__':
    #非虚构作品
    url_non_fiction = 'https://book.douban.com/chart?subcat=I'
    html_non_fiction = getHtml(url_non_fiction)
    link_non_fiction = getLink(html_non_fiction)
    book_non_fiction = []

    for index in range(len(link_non_fiction)):
        html_temp = getHtml(link_non_fiction[index])
        book_non_fiction.append(getBookInf(html_temp))
    print '------------------非虚构类作品-------------------------------------'
    for item in book_non_fiction:
        if item.get('title'):
            print '书名:' + '\t' + item['title'].encode('utf-8')
        if item.get('author'):
            print '作者:' + '\t' + item['author'].encode('utf-8')
        if item.get('price'):
            print '价格:' + '\t' + item['price'].encode('utf-8')
        if item.get('score'):
            print '豆瓣评分:' + '\t' + item['score'].encode('utf-8')
        if item.get('content'):
            print '内容简介:' + '\t' + item['content'].encode('utf-8')
        print '==============================================================='
    print '\n'

    #虚构作品
    url_fiction = 'https://book.douban.com/chart?subcat=F'
    html_fiction = getHtml(url_fiction)
    link_fiction = getLink(html_fiction)
    book_fiction = []

    for index in range(len(link_fiction)):
        html_temp = getHtml(link_fiction[index])
        book_fiction.append(getBookInf(html_temp))
    print '--------------------虚构类作品-------------------------------------'
    for item in book_fiction:
        if item.get('title'):
            print '书名:' + '\t' + item['title'].encode('utf-8')
        if item.get('author'):
            print '作者:' + '\t' + item['author'].encode('utf-8')
        if item.get('price'):
            print '价格:' + '\t' + item['price'].encode('utf-8')
        if item.get('score'):
            print '豆瓣评分:' + '\t' + item['score'].encode('utf-8')
        if item.get('content'):
            print '内容简介:' + '\t' + item['content'].encode('utf-8')
        print '==============================================================='

