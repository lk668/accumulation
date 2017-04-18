#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse


class Cliexample():

    def add_arguments(self, subparsers):
        test_parser = subparsers.add_parser(
            'test',
            help='Help for test',
            parents=[self.parent_parser]
        )

        subcmd_parser = test_parser.add_subparsers(dest='test_cmd')

        start_parser = subcmd_parser.add_parser(
            'start',
            help='start test cmd',
            parents=[self.parent_parser]
            )

        start_parser.add_argument(
            '--tags',
            metavar='TAGS',
            type=str,
            nargs='?',
            dest='tags',
            default=None,
            help='run only tasks with following tags'
        )

        start_parser.set_defaults(func=self.start)

    def __init__(self):
        self.parent_parser = argparse.ArgumentParser(add_help=False)
        self.parent_parser.add_argument(
            '--verbose',
            action='store_true',
            default=False,
            dest='verbose',
            help='verbose mode'
        )
        self.verbose = False

    def start(self, args, verbose):
        if args.tags:
            print "CMD is cli test start --tag"
        else:
            print "CMD is cli test start"
