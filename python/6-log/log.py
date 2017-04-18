#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

import constants


# 生成一个日志对象，（）内为日志对象的名字
LOG = logging.getLogger('Test')

logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %('
                               'message)s',
                        filename=constants.LOG_PATH,
                        filemode='a')
LOG.debug("test1")
LOG = logging.getLogger(__name__)
LOG.debug("test2")
