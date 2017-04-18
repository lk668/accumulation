#!/usr/bin/env python
# -*- coding: utf-8 -*-

from prettytable import PrettyTable


def pretty_formatter(resources, attrs, col_names):
    """
     Optional col_names can be used to change column names in
     output.

     Args:
        resources (list): list of resources to format.
        attrs (list): List of attributes to retrieve from each resource.
        col_names (Optional[list]): List of columns alternative names.

    Returns:
        str: String with resources formatted in pretty table.
    """
    # 初始化表格，col_names是表头的名字
    tableout = PrettyTable(col_names)
    # 表格外边框举例
    tableout.padding_width = 1
    # 靠左居中
    tableout.align = "l"
    for resource in resources:
        # 表格的每一行
        row = []
        for attr in attrs:
            row.append(resource.get(attr,None))
        tableout.add_row(row)
    return tableout.get_string()

# 表格内容
resources = [{
    'a':'test-1',
    'b':'test-2',
    'c':'test-3',
    'd':'test-4'
}]

# 表格内容的key值
attrs = ['a','b','c','d']

# 表格的表头
col_names = ['1st','2nd','3rd','4th']

print pretty_formatter(resources, attrs, col_names)
