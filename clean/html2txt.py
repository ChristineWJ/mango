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
		"https://www.baidu.com", headers)
	html = crawler.get_html()

	cleaner = cleaner()
	text = cleaner.clean_html(html)
	print(text)
