#!/usr/bin/env python3

from lilaclib import *
update_on = [{'aur':'gnome-shell-extension-topicons-plus-git', 'use_last_modified':True}, {'github':'phocean/TopIcons'}]

build_prefix = 'extra-x86_64'
pre_build = aur_pre_build
post_build = aur_post_build

if __name__ == '__main__':
  single_main()
