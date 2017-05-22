#!/usr/bin/python
#encoding=utf8

from pyexcel.cookbook import merge_all_to_a_book
import glob

merge_all_to_a_book(glob.glob('*.xls'), 'out.xls')
