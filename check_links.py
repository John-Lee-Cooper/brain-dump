#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys, re
import urllib.request


def find_all_patters(string, patterns):
    result = []
    for pattern in patterns:
        result += re.findall(pattern, string)
    return result


def check_link(url):
    try:
        req = urllib.request.Request(
                url, method='HEAD', headers={'User-Agent' : 'link-checker'})
        resp = urllib.request.urlopen(req, timeout=3)

        if resp.code >= 400:
            return url + '\tHTTP response code {}'.format(resp.code)
    except Exception as e:
        return url + '\tException {}'.format(e)
    return None



def check_links(urls):

    errors = []
    for url in urls:
        if url.startswith('#'):
            # skip in-url reference
            continue

        if url.startswith('/') and not url.startswith('//'):
            print(url, 'xxxxxxxxxxxxxxxxxx')
            #url = base_url + url

        error = check_link(url)
        if error is not None:
            errors.append(error)

    return errors


'''
#def main(search_dir, base_url=None):
    for path, dirs, filenames in os.walk(search_dir):
        for filename in [i for i in filenames if i.endswith('.md')]:
            filename = os.path.join(path, filename)
'''

def main(filenames, base_url=''):
    def red(s):
        return '\033[91m' + s + '\033[0m'
    def green(s):
        return '\033[32m' + s + '\033[0m'

    url_patterns = [
        """\[[^\]]+\]\(([^\)^"^']+)\)""",
        '(?:href|src)\s*=\s*"\s*([^"]+)'
    ]

    for filename in filenames:
        with open(filename) as f:
            print(filename, end=' ')
            content = f.read()

            urls = find_all_patters(content, url_patterns)

            errors = check_links(urls)

            print(red('x') if errors else green('‎✔'))
            for error in errors:
                print(error)
            print()


if __name__ == '__main__':
    '''
    if len(sys.argv) < 2:
        print('Look for broken links in markdown files (*.md)\n')
        print('usage: {} root_path base_url\n'.format(sys.argv[0]))
        print('i.e. {} source https://localhost:4000'.format(sys.argv[0]))
        sys.exit(1)

    search_dir = sys.argv[1]
    #base_url = sys.argv[2]

    try:
        main(search_dir)
    except KeyboardInterrupt:
        pass
    '''

    main(sys.argv[1:])
