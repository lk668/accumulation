#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import logging
import os
import sys
import signal

import constants
from commands import Cliexample


LOG = logging.getLogger(__name__)


def _require_sudo():
    if os.getuid() != 0:
        sys.stderr.write('Please use root!')
        sys.exit(1)


def _enable_log():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %('
                               'message)s',
                        filename=constants.LOG_PATH,
                        filemode='a')


def main():
    _require_sudo()
    _enable_log()
    cli = [Cliexample()]
    parser = argparse.ArgumentParser(description='Test CLI')
    subparsers = parser.add_subparsers(help='sub-command help',
                                       dest='sub_command')

    map(lambda x: x.add_arguments(subparsers), cli)

    args = parser.parse_args()
    LOG.debug("Start cmd of %s" % (' '.join(sys.argv)))
    args.func(args, args.verbose)


if __name__ == '__main__':
    sys.exit(main())
