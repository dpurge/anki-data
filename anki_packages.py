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
                            os.path.join(src_dir, 'data', 'lang', 'arb', 'bagauddin', 'vocabulary-basic'),
                            os.path.join(src_dir, 'data', 'lang', 'arb', 'eckehard-schulz', 'vocabulary-basic'),
                            os.path.join(src_dir, 'data', 'lang', 'arb', 'italki', 'vocabulary-basic'),
                            os.path.join(src_dir, 'data', 'lang', 'arb', 'kovalev-sharbatov', 'vocabulary-basic')
                        ]
                    ),
                    AnkiNote(
                        model = os.path.join(src_dir, 'anki', 'lang', 'arb', 'vocabulary-nouns', 'model.json'),
                        template = os.path.join(src_dir, 'template', 'lang', 'arb', 'vocabulary-nouns', 'config.json'),
                        data = [
                            os.path.join(src_dir, 'data', 'lang', 'arb', 'eckehard-schulz', 'vocabulary-nouns'),
                            os.path.join(src_dir, 'data', 'lang', 'arb', 'kovalev-sharbatov', 'vocabulary-nouns')
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
    yield AnkiPackage (
        filename = os.path.join(out_dir, 'language', 'indonesian.apkg'),
        deck = AnkiDeck(
                id = 1780195254,
                name = 'Language::Indonesian',
                notes = [
                    AnkiNote(
                        model = os.path.join(src_dir, 'anki', 'lang', 'ind', 'vocabulary', 'model.json'),
                        template = os.path.join(src_dir, 'template', 'lang', 'ind', 'vocabulary', 'config.json'),
                        data = [
                            os.path.join(src_dir, 'data', 'lang', 'ind', 'indonesian-way', 'vocabulary')
                        ]
                    )
                ]
            )
        )

    # LAT
    # yield AnkiPackage (
    #     filename = os.path.join(out_dir, 'language', 'latin.apkg'),
    #     deck = AnkiDeck (
    #             id = 1228695891,
    #             name = 'Language::Latin',
    #             notes = []
    #         )
    #     )

    # VIE
    yield AnkiPackage (
        filename = os.path.join(out_dir, 'language', 'vietnamese.apkg'),
        deck = AnkiDeck(
                id = 1879426651,
                name = 'Language::Vietnamese',
                notes = [
                    AnkiNote(
                        model = os.path.join(src_dir, 'anki', 'lang', 'vie', 'vocabulary', 'model.json'),
                        template = os.path.join(src_dir, 'template', 'lang', 'vie', 'vocabulary', 'config.json'),
                        data = [
                            os.path.join(src_dir, 'data', 'lang', 'vie', 'colloquial-2012', 'vocabulary')
                        ]
                    )
                ]
            )
        )