# coding: UTF-8

from lxml import etree
import urllib2
import sys


# Obtain keyword from shell command
def obtain_keyword():
    try:
        return sys.argv[1]
    except:
        print 'ERROR: yd(youdao) takes one parameter.'
        sys.exit()
    return None


# Obtain option from shell command
def obtain_option():
    try:
        option = sys.argv[2]
        if option != '-s':
            print 'ERROR: option should be used as "yd keyword -s"'
            sys.exit()
        return option
    except:
        pass
    return None


# Crawl youdao dic page and return a bs4.BeautifulSoup object
def crawl_page(keyword):
    url = 'http://dict.youdao.com/search?le=eng&q=%s&keyfrom=dict.index' % keyword
    parser = etree.HTMLParser()
    # use try to check network connection
    try:
        tree = etree.parse(url, parser)
    except:
        print 'ERROR: network connection failed.'
        sys.exit()
    root = tree.getroot()
    return root


# Find the basic definition
def basic_definition(root):
    try:
        ul = root.xpath('//*[@id="phrsListTab"]/div/ul')[0]
        basic_def = [li.text for li in ul]
    except IndexError:
        basic_def = None
    return basic_def


# find definition of the 21st century big english-chinese dictionary
def century_21_definition(root):
    lis = root.xpath('//*[@id="authDictTrans"]/ul/li[@class="wordGroup"]')
    century_21 = []
    for l in lis:
        part_of_speech_list = l.xpath('./span')
        if part_of_speech_list:
            part_of_speech = part_of_speech_list[0].text
        defs = l.xpath('./ul/li[@class="wordGroup"]/span')
        defs = [d.text for d in defs]
        century_21.append((part_of_speech, defs))
    return century_21


# print basic definition
def print_basic_definition(basic_def):
    print '*****************************************************************'
    for b in basic_def:
        print b
    print '*****************************************************************'
    return None


# print definition of the 21st century big english-chinese dictionary
def print_century_21_definition(century_21):
    for c in century_21:
        i = 0
        print c[0]
        for q in c[1]:
            i += 1
            print i,
            print q
    print '*****************************************************************'
    return None


def main():
    keyword = obtain_keyword()
    root = crawl_page(keyword)
    basic_def = basic_definition(root)
    if not basic_def:
        print "No such word, please try again!"
        return None
    print_basic_definition(basic_def)
    specific = obtain_option()
    if specific:
        century_21 = century_21_definition(root)
        print_century_21_definition(century_21)
    return None


if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')
