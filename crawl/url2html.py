#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:url2html
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


class crawler():

	def __init__(self, url, headers):
		self.url = url
		self.headers = headers

	def get_html(self):
		try:
			req = urllib.request.Request(self.url, headers=self.headers)
			resp = urllib.request.urlopen(req)
		except Exception as e:
			logger.error(e)
			sys.exit(1)
		if resp.status != 200:
			logger.error("http status：", resp.status)
			sys.exit(1)
		html = resp.read()
		det_charstes = chardet.detect(html)
		charset = det_charstes["encoding"]
		if chardet != None:
			html = html.decode(charset)
		else:
			html = html.decode("utf8")
		return html


if __name__ == '__main__':
	logger = config.log()

	headers = {
	}
	crawler = crawler("http://www.baidu.com", headers)
	print(crawler.get_html())
