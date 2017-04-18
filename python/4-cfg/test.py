#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import cfg


if cfg.has_option('DEFAULT', 'username'):
    print cfg.get('DEFAULT', 'username')
if cfg.has_option('PASSWORD', 'password'):
    print cfg.get('PASSWORD', 'password')
