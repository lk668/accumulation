#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import cfg


print cfg.get('DEFAULT', 'username')
print cfg.get('PASSWORD', 'password')
