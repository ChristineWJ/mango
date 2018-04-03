#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:config
   Author:admin
   date:2018/4/3
-------------------------------------------------
   Change Activity:2018/4/3:
-------------------------------------------------
"""
import logging


def log():
	LOGGING_FORMAT = '[%(levelname)s %(asctime)s %(module)s:%(lineno)d]: %(message)s'
	DATE_FORMAT = '%y%m%d %H:%M:%S'
	formatter = logging.Formatter(LOGGING_FORMAT, DATE_FORMAT)
	logging.basicConfig(
		level=logging.INFO,
		format=LOGGING_FORMAT,
		datefmt=DATE_FORMAT
	)
	return logging


if __name__ == '__main__':
	logger = log()
	logger.info("info")
	logger.debug("debug")
	logger.error("error")
