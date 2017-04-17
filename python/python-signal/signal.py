#!/usr/bin/env python
# -*- coding: utf-8 -*-

import signal
import time

def handler(signalnum, frame):
    print "Receive signal.SIGINT"
    print "SIGINT number is {0}".format(signalnum)

# 当linux发出SIGINT信号是，执行handler函数
# linux中ctrl+c会发出SIGINT信号
signal.signal(signal.SIGINT, handler)

time.sleep(10)
