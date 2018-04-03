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
from crawl import url2html
from bs4 import BeautifulSoup


class cleaner():
	def __init__(self):
		pass

	def clean_html(self, html):
		soup = BeautifulSoup(html, 'html.parser')
		body = soup.body
		# text = .replace(re_space, "")
		body_text = body.get_text()
		text = []
		for line in body_text.split("\n"):
			if len(line.strip()) != 0:
				text.append(str(line))
		return text


if __name__ == '__main__':
	headers = {
	}
	crawler = url2html.crawler(
		"https://baike.baidu.com/item/%E7%BA%AF%E6%96%87%E6%9C%AC%E6%B5%8F%E8%A7%88%E5%99%A8/8789704", headers)
	html = crawler.get_html()

	cleaner = cleaner()
	text = cleaner.clean_html(html)
	print(text)
