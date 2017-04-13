#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ConfigParser

CFG_PATH = './test.conf'

cfg = ConfigParser.ConfigParser(allow_no_value=True)
cfg.read(CFG_PATH)
