#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'extra-x86_64'
post_build = aur_post_build
depends = ['python-editor']

def pre_build():
  # aur_pre_build()
  pass

if __name__ == '__main__':
  single_main()

# vim:set ts=2 sw=2 et:
