import os

from invoke import task
from ankiproject import \
    delete_directories, create_directories, \
    AnkiPackage, AnkiDeck, AnkiNote, \
    create_anki_package

src_dir = os.path.abspath('./src')
tmp_dir = os.path.abspath('./tmp')
out_dir = os.path.abspath('./out')

anki_packages = [

    AnkiPackage(
        filename = os.path.join(out_dir, 'language', 'modern-standard-arabic.apkg'),
        deck = AnkiDeck(
                id = 1706626659,
                name = 'Language::Modern Standard Arabic',
                notes = [
                    AnkiNote(
                        model = os.path.join(src_dir, 'anki', 'lang', 'arb', 'basic', 'model.json'),
                        template = os.path.join(src_dir, 'template', 'lang', 'arb', 'vocabulary-basic', 'config.json'),
                        data = [
                            os.path.join(src_dir, 'data', 'lang', 'arb', 'vocabulary')
                        ]
                    ),
                    AnkiNote(
                        model = os.path.join(src_dir, 'anki', 'lang', 'arb', 'cloze', 'model.json'),
                        template = os.path.join(src_dir, 'template', 'lang', 'arb', 'models-cloze', 'config.json'),
                        data = [
                            os.path.join(src_dir, 'data', 'lang', 'arb', 'models')
                        ]
                    )
                ]
        )
    ),

    AnkiPackage(
        filename = os.path.join(out_dir, 'language', 'egyptian-arabic.apkg'),
        deck = AnkiDeck(
                id = 1851605761,
                name = 'Language::Egyptian Arabic',
                notes = [
                    AnkiNote(
                        model = os.path.join(src_dir, 'anki', 'lang', 'arz', 'basic', 'model.json'),
                        template = os.path.join(src_dir, 'template', 'lang', 'arz', 'vocabulary-basic', 'config.json'),
                        data = [
                            os.path.join(src_dir, 'data', 'lang', 'arz', 'vocabulary')
                        ]
                    ),
                    AnkiNote(
                        model = os.path.join(src_dir, 'anki', 'lang', 'arz', 'cloze', 'model.json'),
                        template = os.path.join(src_dir, 'template', 'lang', 'arz', 'models-cloze', 'config.json'),
                        data = [
                            os.path.join(src_dir, 'data', 'lang', 'arz', 'models')
                        ]
                    )
                ]
        )
    ),

    AnkiPackage(
        filename = os.path.join(out_dir, 'language', 'indonesian.apkg'),
        deck = AnkiDeck(
                id = 1780195254,
                name = 'Language::Indonesian',
                notes = [
                    AnkiNote(
                        model = os.path.join(src_dir, 'anki', 'lang', 'ind', 'basic', 'model.json'),
                        template = os.path.join(src_dir, 'template', 'lang', 'ind', 'vocabulary-basic', 'config.json'),
                        data = [
                            os.path.join(src_dir, 'data', 'lang', 'ind', 'vocabulary')
                        ]
                    ),
                    AnkiNote(
                        model = os.path.join(src_dir, 'anki', 'lang', 'ind', 'cloze', 'model.json'),
                        template = os.path.join(src_dir, 'template', 'lang', 'ind', 'models-cloze', 'config.json'),
                        data = [
                            os.path.join(src_dir, 'data', 'lang', 'ind', 'models')
                        ]
                    )
                ]
        )
    ),

    AnkiPackage(
        filename = os.path.join(out_dir, 'language', 'latin.apkg'),
        deck = AnkiDeck(
                id = 1228695891,
                name = 'Language::Latin',
                notes = []
        )
    )

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
    #for dataflow in dataflows:
    #    for item in dataflow.run():
    #        print(item)
    for pkg in anki_packages:
        filename = create_anki_package(pkg)
        print(filename)