import os

from invoke import task
from ankiproject import delete_directories, create_directories, create_anki_package
from anki_packages import get_anki_packages

src_dir = os.path.abspath('./src')
tmp_dir = os.path.abspath('./tmp')
out_dir = os.path.abspath('./out')

anki_packages = get_anki_packages(src_dir = src_dir, out_dir = out_dir)


@task
def clean(c, output = False):
    directories = [tmp_dir]
    if output:
        directories.append(out_dir)
    delete_directories(*directories)


@task
def build(c):
    create_directories(out_dir, tmp_dir)
    for pkg in anki_packages:
        filename = create_anki_package(pkg)
        print(filename)