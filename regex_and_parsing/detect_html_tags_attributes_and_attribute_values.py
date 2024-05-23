"""
https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem?isFullScreen=true
"""

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        [print(f'-> {attr[0]} > {attr[1]}') for attr in attrs]
        
parser = MyHTMLParser()
for _  in range(int(input())):
    parser.feed(input())