#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:html2txt
   Author:admin
   date:2018/4/3
-------------------------------------------------
   Change Activity:2018/4/3:
-------------------------------------------------
"""
import sys
import urllib.request
import chardet
from log import config
from crawl import url2html


class cleaner():
	def __init__(self):
		pass

	def clean_html(self, html):
		pass


if __name__ == '__main__':
	headers = {
	}
	crawler = url2html.crawler("http://www.baidu.com", headers)
	html = crawler.get_html()

	cleaner = cleaner()
	text = cleaner.clean_html(html)

	print(text)
