#!python3

import io
import os
import shutil
import sys
import urllib.request
import zipfile

src, dst = sys.argv[1:]

if not os.path.isfile(os.path.join(dst, 'baseconv.decTest')):
    shutil.copytree(src, dst, copy_function=shutil.copyfile, dirs_exist_ok=True)

if not os.path.isfile(os.path.join(dst, 'add.decTest')):
    with urllib.request.urlopen('http://speleotrove.com/decimal/dectest.zip') as f:
        with zipfile.ZipFile(io.BytesIO(f.read())) as z:
            z.extractall(dst)
