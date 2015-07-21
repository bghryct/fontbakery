#!/usr/bin/env python
import argparse
import logging
import os
import tabulate

from bakery_cli.logger import logger
from fontTools import ttLib

args = argparse.ArgumentParser(
	description='Print out italicAngle of the fonts')
args.add_argument('font', nargs="+")
args.add_argument('--verbose', default=False, action='store_true')


if __name__ == '__main__':

	arg = args.parse_args()

	if not arg.verbose:
	    logger.setLevel(logging.INFO)
	
	headers = ['filename', 'italicAngle']
	rows = []
	for font in arg.font:
		ttfont = ttLib.TTFont(font)
		rows.append([os.path.basename(font), ttfont['post'].italicAngle])
	print(tabulate.tabulate(rows, headers))