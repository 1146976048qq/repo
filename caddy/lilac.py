#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

build_prefix = 'extra-x86_64'

def pre_build():
    for line in edit_file('PKGBUILD'):
        if line.startswith('prepare() {'):
            line += "\n    export CGO_ENABLED=0"
        print(line)
    git_add_files('PKGBUILD')
    git_commit()

post_build = aur_post_build

if __name__ == '__main__':
  single_main()
