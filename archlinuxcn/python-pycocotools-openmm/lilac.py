#!/usr/bin/env python3

from lilaclib import *

def pre_build():
  aur_pre_build(do_vcs_update=True)

def post_build():
  aur_post_build()
# vim:set ts=2 sw=2 et:

