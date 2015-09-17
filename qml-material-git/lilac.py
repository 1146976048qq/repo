#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

build_prefix = 'extra-x86_64'
post_build = aur_post_build

def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        # edit PKGBUILD
        if line.strip().startswith("qmake"):
            words = line.split(" ")
            words[0] = ("qmake-qt5")
            line = " ".join(words)
        print(line)




if __name__ == '__main__':
    single_main(build_prefix)


