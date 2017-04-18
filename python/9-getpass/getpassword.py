#!/usr/bin/env python
# -*- coding: utf-8 -*-

import getpass


def get_password(prompt):
    return getpass.getpass(prompt=prompt)


password = get_password("Please input the xxx password:")
print "The password you input is {0}".format(password)
