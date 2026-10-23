#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 10/23/2026 https://github.com/su8/0verbs
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.
#
# The program is python2 and python3 compatibile
import os
import re
import sys
from subprocess import check_output
try:
    from urllib.request import urlopen
except ImportError:
    from urllib import urlopen

class PackageFinder(object):

    def __init__(self):
        the_list = os.path.join(os.getenv('HOME'), '.package_list')

        if not os.path.isfile(the_list):
            ftp_url = 'ftp://ftp.openbsd.org/pub/OpenBSD/{release}/packages/{arch}/SHA256'\
            .format(release=self.spawN('uname', '-r'), arch=self.spawN('machine', '-a'))

            print('Creating a small local database from all {0} packages'\
            .format(ftp_url))

            all_packages = urlopen(ftp_url).read().decode('utf-8').split('\n')

            package_as_txt = str()
            for current_package in all_packages:
                package_as_txt += current_package + '\n'
            with open(the_list, 'wt') as z:
                z.write(package_as_txt)
            print('You are ready to perform local package search,'
                ' database saved in {0}'.format(the_list))
        else:
            if len(sys.argv) < 2:
                sys.exit('ERROR: Please supply some package!')
            query = sys.argv[1]
            with open(the_list, 'rt') as read_packs:
                for x in read_packs.readlines():
                    current_line = ''.join(re.findall(r'\([^()]*\)', x))\
                    .replace('(', '').replace(')', '')
                    if query in current_line:
                        found_match, _ = os.path.splitext(current_line)
                        print(found_match)

    def spawN(self, *arg):
        return check_output([arg[0], arg[1]]).decode('utf-8').replace('\n', '')

if __name__ == '__main__':
    PackageFinder()