# Trimmed lilac.py
#!/usr/bin/env python3

from lilaclib import *

def post_build():
    git_add_files('PKGBUILD')
    git_commit()
