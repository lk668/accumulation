#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def get_disk_space(mountpoint='/'):
    size_total = None
    size_available = None
    try:
        statvfs_result = os.statvfs(mountpoint)
        print statvfs_result
        size_total = statvfs_result.f_bsize * statvfs_result.f_blocks
        size_available = statvfs_result.f_bsize * (statvfs_result.f_bavail)
    except OSError:
        pass
    return size_total, size_available

print get_disk_space('/')
