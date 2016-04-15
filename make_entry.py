#!/usr/bin/env python

# A script for creating blog entries in Pelican with the name format
#   YYYY-MM-DD-title-phrase-here.md
#
# Taken from
#   http://nafiulis.me/making-a-static-blog-with-pelican.html
# and modified only slightly (mainly for Markdown rather than reST)

import sys
from datetime import datetime

TEMPLATE = """
{title}
{hashes}

Date: {year}-{month}-{day} {hour}:{minute:02d}
Tags:
Category:
Slug: {slug}
Summary:
Status: draft


"""


def make_entry(title):
    today = datetime.today()
    slug = title.lower().strip().replace(' ', '-')
    f_create = "content/{}-{:0>2}-{:0>2}-{}.md".format(
        today.year, today.month, today.day, slug)
    t = TEMPLATE.strip().format(title=title,
                                hashes='#' * len(title),
                                year=today.year,
                                month=today.month,
                                day=today.day,
                                hour=today.hour,
                                minute=today.minute,
                                slug=slug)
    with open(f_create, 'w') as w:
        w.write(t)
    print("File created -> " + f_create)


if __name__ == '__main__':

    if len(sys.argv) > 1:
        make_entry(sys.argv[1])
    else:
        print "No title given"
