#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup

def get_link(url,keyword):
    html = urllib.request.urlopen(url)
    ## ここの引数 'lxml' は環境依存？
    soup = BeautifulSoup(html,'lxml')


    result = []
    for link in soup.find_all('a',href=True):
        li = link['href']
        if keyword in li:
            #print(link)
            result.append(li)

    if len(result)>1:
        print('{} results'.format(len(result)))
        return result
    
    if len(result)==0:
        print('No result')
        return None

    else:
        your_url = url+result[0]
        return your_url

