#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def confirm(req, default='no', out=sys.stdout):
    valid = {"yes": True, "y": True,
             "no": False, "n": False}
    prompt = " [y/n] "

    while True:
        out.write(req + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]

print confirm("Do you like me?")
