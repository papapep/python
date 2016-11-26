#!/usr/bin/python
# coding=UTF8

"""Extract the `value` element from the XML tree, if it exists."""
from __future__ import print_function
from xml.etree import ElementTree as ET

tree = ET.ElementTree(file='dades.xml')
root = tree.getroot()

for child_of_root in root:
    for child_of_root2 in child_of_root:
        print (child_of_root2.tag, '\t', child_of_root2.text,end="\t")
    
    print()