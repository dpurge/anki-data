import os

from ankiproject import AnkiPackage, AnkiDeck, AnkiNote

def get_anki_packages(src_dir, out_dir):

    # ARB
    yield AnkiPackage (
        filename = os.path.join(out_dir, 'language', 'modern-standard-arabic.apkg'),
        deck = AnkiDeck(
                id = 1706626659,
                name = 'Language::Modern Standard Arabic',
                notes = [
                    AnkiNote(
                        model = os.path.join(src_dir, 'anki', 'lang', 'arb', 'vocabulary-basic', 'model.json'),
                        template = os.path.join(src_dir, 'template', 'lang', 'arb', 'vocabulary-basic', 'config.json'),
                        data = [
                            os.path.join(src_dir, 'data', 'lang', 'arb', 'Italki', 'vocabulary-basic')
                        ]
                    )
                ]
            )
        )

    # ARZ
    # yield AnkiPackage (
    #     filename = os.path.join(out_dir, 'language', 'egyptian-arabic.apkg'),
    #     deck = AnkiDeck(
    #             id = 1851605761,
    #             name = 'Language::Egyptian Arabic',
    #             notes = [
    #                 AnkiNote(
    #                     model = os.path.join(src_dir, 'anki', 'lang', 'arz', 'basic', 'model.json'),
    #                     template = os.path.join(src_dir, 'template', 'lang', 'arz', 'vocabulary-basic', 'config.json'),
    #                     data = [
    #                         os.path.join(src_dir, 'data', 'lang', 'arz', 'vocabulary')
    #                     ]
    #                 ),
    #                 AnkiNote(
    #                     model = os.path.join(src_dir, 'anki', 'lang', 'arz', 'cloze', 'model.json'),
    #                     template = os.path.join(src_dir, 'template', 'lang', 'arz', 'models-cloze', 'config.json'),
    #                     data = [
    #                         os.path.join(src_dir, 'data', 'lang', 'arz', 'models')
    #                     ]
    #                 )
    #             ]
    #         )
    #     )

    # CMN
    yield AnkiPackage (
        filename = os.path.join(out_dir, 'language', 'mandarin-chinese.apkg'),
        deck = AnkiDeck(
                id = 1973408674,
                name = 'Language::Mandarin Chinese',
                notes = [
                    AnkiNote(
                       model = os.path.join(src_dir, 'anki', 'lang', 'cmn', 'vocabulary', 'model.json'),
                       template = os.path.join(src_dir, 'template', 'lang', 'cmn', 'vocabulary', 'config.json'),
                       data = [
                           os.path.join(src_dir, 'data', 'lang', 'cmn', 'short-term-spoken', 'vocabulary')
                       ]
                    ),
                    AnkiNote(
                       model = os.path.join(src_dir, 'anki', 'lang', 'cmn', 'models', 'model.json'),
                       template = os.path.join(src_dir, 'template', 'lang', 'cmn', 'models', 'config.json'),
                       data = [
                           os.path.join(src_dir, 'data', 'lang', 'cmn', 'short-term-spoken', 'models')
                       ]
                    ),
                    AnkiNote(
                        model = os.path.join(src_dir, 'anki', 'lang', 'cmn', 'texts', 'model.json'),
                        template = os.path.join(src_dir, 'template', 'lang', 'cmn', 'texts', 'config.json'),
                        data = [
                            os.path.join(src_dir, 'data', 'lang', 'cmn', 'short-term-spoken', 'texts')
                        ]
                    )
                ]
            )
        )

    # IND
    # yield AnkiPackage (
    #     filename = os.path.join(out_dir, 'language', 'indonesian.apkg'),
    #     deck = AnkiDeck(
    #             id = 1780195254,
    #             name = 'Language::Indonesian',
    #             notes = [
    #                 AnkiNote(
    #                     model = os.path.join(src_dir, 'anki', 'lang', 'ind', 'basic', 'model.json'),
    #                     template = os.path.join(src_dir, 'template', 'lang', 'ind', 'vocabulary-basic', 'config.json'),
    #                     data = [
    #                         os.path.join(src_dir, 'data', 'lang', 'ind', 'vocabulary')
    #                     ]
    #                 ),
    #                 AnkiNote(
    #                     model = os.path.join(src_dir, 'anki', 'lang', 'ind', 'cloze', 'model.json'),
    #                     template = os.path.join(src_dir, 'template', 'lang', 'ind', 'models-cloze', 'config.json'),
    #                     data = [
    #                         os.path.join(src_dir, 'data', 'lang', 'ind', 'models')
    #                     ]
    #                 )
    #             ]
    #         )
    #     )

    # LAT
    # yield AnkiPackage (
    #     filename = os.path.join(out_dir, 'language', 'latin.apkg'),
    #     deck = AnkiDeck (
    #             id = 1228695891,
    #             name = 'Language::Latin',
    #             notes = []
    #         )
    #     )