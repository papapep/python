#!/usr/bin/python
# coding=UTF8

"""Extract the `value` element from the XML tree, if it exists."""
from __future__ import print_function
from xml.etree import ElementTree as ET


rs = ET.fromstring(file='dades.xml')
root = rs.findall('RS/R')

for item in root:
    print item.find('C1').text


