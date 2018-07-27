#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

build_prefix = 'extra-x86_64'

#pre_build = aur_pre_build
def pre_build():
  aur_pre_build()
#  add_makedepends([
  add_depends([
    "alsa-lib",
    "pulseaudio",
    "libmpdclient",
    "libnl",
    "wireless_tools",
    "jsoncpp",
    "i3-wm",
    "curl"])

post_build = aur_post_build

if __name__ == '__main__':
  single_main()
