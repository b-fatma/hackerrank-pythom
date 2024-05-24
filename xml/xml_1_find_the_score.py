"""
https://www.hackerrank.com/challenges/xml-1-find-the-score/problem?isFullScreen=true
"""

import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # your code goes here
    score = len(node.attrib)
    for child_node in node:
        score += get_attr_number(child_node)
    return score
    
if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))