#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        if 'gnome-shell<3.$' not in line:
            print(line)
        else:
            print(line.replace('gnome-shell<3.$', 'gnome-shell<1:3.$'))

