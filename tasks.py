import os

from invoke import task
from ankiproject import \
    DataFlow, Record, \
    delete_directories, create_directories, \
    get_files, get_data, \
    apply_template

src_dir = os.path.abspath('./src')
tmp_dir = os.path.abspath('./tmp')
out_dir = os.path.abspath('./out')

dataflows = [
    DataFlow(
        meta = {
            'template_folder': os.path.join(src_dir, 'template', 'lang'),
            'template_name': 'spa/cloze.html'
            },
        data = [
            Record(
                meta = {'format':'filesystem/directory'},
                data = os.path.join(src_dir, 'data', 'language', 'indonesian', 'cloze')),
            Record(
                meta = {'format':'filesystem/directory'},
                data = os.path.join(src_dir, 'data', 'language', 'spanish', 'cloze'))],
        pipeline = [get_files, get_data, apply_template])
]

@task
def clean(c, output = False):
    directories = [tmp_dir]
    if output:
        directories.append(out_dir)
    delete_directories(*directories)


@task
def build(c):
    create_directories(out_dir, tmp_dir)
    for dataflow in dataflows:
        for item in dataflow.run():
            print(item)