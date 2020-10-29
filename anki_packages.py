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
    yield AnkiPackage (
        filename = os.path.join(out_dir, 'language', 'egyptian-arabic.apkg'),
        deck = AnkiDeck(
                id = 1851605761,
                name = 'Language::Egyptian Arabic',
                notes = [
                    AnkiNote(
                        model = os.path.join(src_dir, 'anki', 'lang', 'arz', 'vocabulary-basic', 'model.json'),
                        template = os.path.join(src_dir, 'template', 'lang', 'arz', 'vocabulary-basic', 'config.json'),
                        data = [
                            os.path.join(src_dir, 'data', 'lang', 'arz', 'kallimni-arabi-bishweesh', 'vocabulary')
                        ]
                    )#,
                    # AnkiNote(
                    #     model = os.path.join(src_dir, 'anki', 'lang', 'arz', 'cloze', 'model.json'),
                    #     template = os.path.join(src_dir, 'template', 'lang', 'arz', 'models-cloze', 'config.json'),
                    #     data = [
                    #         os.path.join(src_dir, 'data', 'lang', 'arz', 'models')
                    #     ]
                    # )
                ]
            )
        )

    # BUL
    yield AnkiPackage (
        filename = os.path.join(out_dir, 'language', 'bulgarian.apkg'),
        deck = AnkiDeck(
                id = 1440911993,
                name = 'Language::Bulgarian',
                notes = [
                    AnkiNote(
                        model = os.path.join(src_dir, 'anki', 'lang', 'bul', 'vocabulary', 'model.json'),
                        template = os.path.join(src_dir, 'template', 'lang', 'bul', 'vocabulary', 'config.json'),
                        data = [
                            os.path.join(src_dir, 'data', 'lang', 'bul', 'glivinskaya-platonova-2004'),
                            os.path.join(src_dir, 'data', 'lang', 'bul', 'ivanova-shanova-dimitrova-2011')
                        ]
                    )
                ]
            )
        )

    # CES
    yield AnkiPackage (
        filename = os.path.join(out_dir, 'language', 'czech.apkg'),
        deck = AnkiDeck(
                id = 1083078907,
                name = 'Language::Czech',
                notes = [
                    AnkiNote(
                        model = os.path.join(src_dir, 'anki', 'lang', 'ces', 'vocabulary', 'model.json'),
                        template = os.path.join(src_dir, 'template', 'lang', 'ces', 'vocabulary', 'config.json'),
                        data = [
                            os.path.join(src_dir, 'data', 'lang', 'ces', 'martynenko-2019')
                        ]
                    )
                ]
            )
        )

    # CMN
    yield AnkiPackage (
        filename = os.path.join(out_dir, 'language', 'mandarin-chinese-simplified.apkg'),
        deck = AnkiDeck(
                id = 1973408674,
                name = 'Language::Mandarin Chinese (Simplified)',
                notes = [
                    AnkiNote(
                       model = os.path.join(src_dir, 'anki', 'lang', 'cmn', 'vocabulary-hans', 'model.json'),
                       template = os.path.join(src_dir, 'template', 'lang', 'cmn', 'vocabulary', 'config.json'),
                       data = [
                           os.path.join(src_dir, 'data', 'lang', 'cmn', 'short-term-spoken', 'vocabulary'),
                           os.path.join(src_dir, 'data', 'lang', 'cmn', 'kan-qian')
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

    yield AnkiPackage (
        filename = os.path.join(out_dir, 'language', 'mandarin-chinese-traditional.apkg'),
        deck = AnkiDeck(
                id = 2021001651,
                name = 'Language::Mandarin Chinese (Traditional)',
                notes = [
                    AnkiNote(
                       model = os.path.join(src_dir, 'anki', 'lang', 'cmn', 'vocabulary-hant', 'model.json'),
                       template = os.path.join(src_dir, 'template', 'lang', 'cmn', 'vocabulary', 'config.json'),
                       data = [
                           os.path.join(src_dir, 'data', 'lang', 'cmn', 'lingshailo-1955'),
                           os.path.join(src_dir, 'data', 'lang', 'cmn', 'isaenko-korotkov-sovetov')
                       ]
                    )
                ]
            )
        )

    # DAN
    yield AnkiPackage (
        filename = os.path.join(out_dir, 'language', 'danish.apkg'),
        deck = AnkiDeck(
                id = 1651997480,
                name = 'Language::Danish',
                notes = [
                    AnkiNote(
                        model = os.path.join(src_dir, 'anki', 'lang', 'dan', 'vocabulary', 'model.json'),
                        template = os.path.join(src_dir, 'template', 'lang', 'dan', 'vocabulary', 'config.json'),
                        data = [
                            os.path.join(src_dir, 'data', 'lang', 'dan', '___', 'vocabulary')
                        ]
                    )
                ]
            )
        )

    # DEU
    yield AnkiPackage (
        filename = os.path.join(out_dir, 'language', 'german.apkg'),
        deck = AnkiDeck(
                id = 1463683857,
                name = 'Language::German',
                notes = [
                    AnkiNote(
                        model = os.path.join(src_dir, 'anki', 'lang', 'deu', 'vocabulary', 'model.json'),
                        template = os.path.join(src_dir, 'template', 'lang', 'deu', 'vocabulary', 'config.json'),
                        data = [
                            os.path.join(src_dir, 'data', 'lang', 'deu', 'tematyczny-9000')
                        ]
                    )
                ]
            )
        )

    # ELL
    yield AnkiPackage (
        filename = os.path.join(out_dir, 'language', 'modern-greek.apkg'),
        deck = AnkiDeck(
                id = 1900654315,
                name = 'Language::Modern Greek',
                notes = [
                    AnkiNote(
                        model = os.path.join(src_dir, 'anki', 'lang', 'ell', 'vocabulary', 'model.json'),
                        template = os.path.join(src_dir, 'template', 'lang', 'ell', 'vocabulary', 'config.json'),
                        data = [
                            os.path.join(src_dir, 'data', 'lang', 'ell', '___', 'vocabulary')
                        ]
                    )
                ]
            )
        )

    # FAS
    yield AnkiPackage (
        filename = os.path.join(out_dir, 'language', 'farsi.apkg'),
        deck = AnkiDeck(
                id = 1599607598,
                name = 'Language::Farsi',
                notes = [
                    AnkiNote(
                        model = os.path.join(src_dir, 'anki', 'lang', 'fas', 'vocabulary', 'model.json'),
                        template = os.path.join(src_dir, 'template', 'lang', 'fas', 'vocabulary', 'config.json'),
                        data = [
                            os.path.join(src_dir, 'data', 'lang', 'fas', 'alavi-lorenz', 'vocabulary'),
                            os.path.join(src_dir, 'data', 'lang', 'fas', 'colloquial-2011', 'vocabulary')
                        ]
                    )
                ]
            )
        )

    # FRA
    yield AnkiPackage (
        filename = os.path.join(out_dir, 'language', 'french.apkg'),
        deck = AnkiDeck(
                id = 1490255054,
                name = 'Language::French',
                notes = [
                    AnkiNote(
                        model = os.path.join(src_dir, 'anki', 'lang', 'fra', 'vocabulary', 'model.json'),
                        template = os.path.join(src_dir, 'template', 'lang', 'fra', 'vocabulary', 'config.json'),
                        data = [
                            os.path.join(src_dir, 'data', 'lang', 'fra', 'tematyczny-9000')
                        ]
                    )
                ]
            )
        )

    # GRC
    yield AnkiPackage (
        filename = os.path.join(out_dir, 'language', 'ancient-greek.apkg'),
        deck = AnkiDeck(
                id = 2089318160,
                name = 'Language::Ancient Greek',
                notes = [
                    AnkiNote(
                        model = os.path.join(src_dir, 'anki', 'lang', 'grc', 'vocabulary', 'model.json'),
                        template = os.path.join(src_dir, 'template', 'lang', 'grc', 'vocabulary', 'config.json'),
                        data = [
                            os.path.join(src_dir, 'data', 'lang', 'grc', '___', 'vocabulary')
                        ]
                    )
                ]
            )
        )

    # HEB
    yield AnkiPackage (
        filename = os.path.join(out_dir, 'language', 'hebrew.apkg'),
        deck = AnkiDeck(
                id = 1977982198,
                name = 'Language::Hebrew',
                notes = [
                    AnkiNote(
                        model = os.path.join(src_dir, 'anki', 'lang', 'heb', 'vocabulary', 'model.json'),
                        template = os.path.join(src_dir, 'template', 'lang', 'heb', 'vocabulary', 'config.json'),
                        data = [
                            os.path.join(src_dir, 'data', 'lang', 'heb', 'tematyczny-9000')
                        ]
                    )
                ]
            )
        )

    # HIN
    yield AnkiPackage (
        filename = os.path.join(out_dir, 'language', 'hindi.apkg'),
        deck = AnkiDeck(
                id = 1675774097,
                name = 'Language::Hindi',
                notes = [
                    AnkiNote(
                        model = os.path.join(src_dir, 'anki', 'lang', 'hin', 'vocabulary', 'model.json'),
                        template = os.path.join(src_dir, 'template', 'lang', 'hin', 'vocabulary', 'config.json'),
                        data = [
                            os.path.join(src_dir, 'data', 'lang', 'hin', 'kostina-2016'),
                            os.path.join(src_dir, 'data', 'lang', 'hin', 'teach-yourself')
                        ]
                    )
                ]
            )
        )

    # HYE
    yield AnkiPackage (
        filename = os.path.join(out_dir, 'language', 'armenian.apkg'),
        deck = AnkiDeck(
                id = 1081329769,
                name = 'Language::Armenian',
                notes = [
                    AnkiNote(
                        model = os.path.join(src_dir, 'anki', 'lang', 'hye', 'vocabulary', 'model.json'),
                        template = os.path.join(src_dir, 'template', 'lang', 'hye', 'vocabulary', 'config.json'),
                        data = [
                            os.path.join(src_dir, 'data', 'lang', 'hye', 'sakayan-2007')
                        ]
                    )
                ]
            )
        )

    # HUN
    yield AnkiPackage (
        filename = os.path.join(out_dir, 'language', 'hungarian.apkg'),
        deck = AnkiDeck(
                id = 1885354038,
                name = 'Language::Hungarian',
                notes = [
                    AnkiNote(
                        model = os.path.join(src_dir, 'anki', 'lang', 'hun', 'vocabulary', 'model.json'),
                        template = os.path.join(src_dir, 'template', 'lang', 'hun', 'vocabulary', 'config.json'),
                        data = [
                            os.path.join(src_dir, 'data', 'lang', 'hun', '___', 'vocabulary')
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
                            os.path.join(src_dir, 'data', 'lang', 'ind', 'soravia-2002'),
                            os.path.join(src_dir, 'data', 'lang', 'ind', 'colloquial-1994'),
                            os.path.join(src_dir, 'data', 'lang', 'ind', 'demidiuk-sujai-hajartno'),
                            os.path.join(src_dir, 'data', 'lang', 'ind', 'indonesian-way', 'vocabulary'),
                            os.path.join(src_dir, 'data', 'lang', 'ind', 'italki')
                        ]
                    )
                ]
            )
        )

    # ITA
    yield AnkiPackage (
        filename = os.path.join(out_dir, 'language', 'italian.apkg'),
        deck = AnkiDeck(
                id = 1500977626,
                name = 'Language::Italian',
                notes = [
                    AnkiNote(
                        model = os.path.join(src_dir, 'anki', 'lang', 'ita', 'vocabulary', 'model.json'),
                        template = os.path.join(src_dir, 'template', 'lang', 'ita', 'vocabulary', 'config.json'),
                        data = [
                            os.path.join(src_dir, 'data', 'lang', 'ita', '___', 'vocabulary')
                        ]
                    )
                ]
            )
        )

    # KAZ
    yield AnkiPackage (
        filename = os.path.join(out_dir, 'language', 'kazakh.apkg'),
        deck = AnkiDeck(
                id = 1972920187,
                name = 'Language::Kazakh',
                notes = [
                    AnkiNote(
                        model = os.path.join(src_dir, 'anki', 'lang', 'kaz', 'vocabulary', 'model.json'),
                        template = os.path.join(src_dir, 'template', 'lang', 'kaz', 'vocabulary', 'config.json'),
                        data = [
                            os.path.join(src_dir, 'data', 'lang', 'kaz', 'razgovornyj-legko')
                        ]
                    )
                ]
            )
        )

    # LAT
    yield AnkiPackage (
        filename = os.path.join(out_dir, 'language', 'latin.apkg'),
        deck = AnkiDeck(
                id = 1228695891,
                name = 'Language::Latin',
                notes = [
                    AnkiNote(
                        model = os.path.join(src_dir, 'anki', 'lang', 'lat', 'vocabulary', 'model.json'),
                        template = os.path.join(src_dir, 'template', 'lang', 'lat', 'vocabulary', 'config.json'),
                        data = [
                            os.path.join(src_dir, 'data', 'lang', 'lat', '___', 'vocabulary')
                        ]
                    )
                ]
            )
        )

    # LIT
    yield AnkiPackage (
        filename = os.path.join(out_dir, 'language', 'lithuanian.apkg'),
        deck = AnkiDeck(
                id = 1808985328,
                name = 'Language::Lithuanian',
                notes = [
                    AnkiNote(
                        model = os.path.join(src_dir, 'anki', 'lang', 'lit', 'vocabulary', 'model.json'),
                        template = os.path.join(src_dir, 'template', 'lang', 'lit', 'vocabulary', 'config.json'),
                        data = [
                            os.path.join(src_dir, 'data', 'lang', 'lit', '___', 'vocabulary')
                        ]
                    )
                ]
            )
        )

    # NLD
    yield AnkiPackage (
        filename = os.path.join(out_dir, 'language', 'dutch.apkg'),
        deck = AnkiDeck(
                id = 1338690685,
                name = 'Language::Dutch',
                notes = [
                    AnkiNote(
                        model = os.path.join(src_dir, 'anki', 'lang', 'nld', 'vocabulary', 'model.json'),
                        template = os.path.join(src_dir, 'template', 'lang', 'nld', 'vocabulary', 'config.json'),
                        data = [
                            os.path.join(src_dir, 'data', 'lang', 'nld', '___', 'vocabulary')
                        ]
                    )
                ]
            )
        )

    # RON
    yield AnkiPackage (
        filename = os.path.join(out_dir, 'language', 'romanian.apkg'),
        deck = AnkiDeck(
                id = 1188298127,
                name = 'Language::Romanian',
                notes = [
                    AnkiNote(
                        model = os.path.join(src_dir, 'anki', 'lang', 'ron', 'vocabulary', 'model.json'),
                        template = os.path.join(src_dir, 'template', 'lang', 'ron', 'vocabulary', 'config.json'),
                        data = [
                            os.path.join(src_dir, 'data', 'lang', 'ron', '___', 'vocabulary')
                        ]
                    )
                ]
            )
        )

    # RUS
    yield AnkiPackage (
        filename = os.path.join(out_dir, 'language', 'russian.apkg'),
        deck = AnkiDeck(
                id = 2116971379,
                name = 'Language::Russian',
                notes = [
                    AnkiNote(
                        model = os.path.join(src_dir, 'anki', 'lang', 'rus', 'vocabulary', 'model.json'),
                        template = os.path.join(src_dir, 'template', 'lang', 'rus', 'vocabulary', 'config.json'),
                        data = [
                            os.path.join(src_dir, 'data', 'lang', 'rus', 'tematyczny-9000')
                        ]
                    )
                ]
            )
        )

    # SPA
    yield AnkiPackage (
        filename = os.path.join(out_dir, 'language', 'spanish.apkg'),
        deck = AnkiDeck(
                id = 1659435005,
                name = 'Language::Spanish',
                notes = [
                    AnkiNote(
                        model = os.path.join(src_dir, 'anki', 'lang', 'spa', 'vocabulary', 'model.json'),
                        template = os.path.join(src_dir, 'template', 'lang', 'spa', 'vocabulary', 'config.json'),
                        data = [
                            os.path.join(src_dir, 'data', 'lang', 'spa', 'aula'),
                            os.path.join(src_dir, 'data', 'lang', 'spa', 'frequency-2006')# ,
                            # os.path.join(src_dir, 'data', 'lang', 'spa', 'tematyczny-9000')
                        ]
                    )
                ]
            )
        )

    # SRP
    yield AnkiPackage (
        filename = os.path.join(out_dir, 'language', 'serbian.apkg'),
        deck = AnkiDeck(
                id = 1756731000,
                name = 'Language::Serbian',
                notes = [
                    AnkiNote(
                        model = os.path.join(src_dir, 'anki', 'lang', 'srp', 'vocabulary', 'model.json'),
                        template = os.path.join(src_dir, 'template', 'lang', 'srp', 'vocabulary', 'config.json'),
                        data = [
                            os.path.join(src_dir, 'data', 'lang', 'srp', '___', 'vocabulary')
                        ]
                    )
                ]
            )
        )

    # TGK
    yield AnkiPackage (
        filename = os.path.join(out_dir, 'language', 'tajiki.apkg'),
        deck = AnkiDeck(
                id = 1690278087,
                name = 'Language::Tajiki',
                notes = [
                    AnkiNote(
                        model = os.path.join(src_dir, 'anki', 'lang', 'tgk', 'vocabulary', 'model.json'),
                        template = os.path.join(src_dir, 'template', 'lang', 'tgk', 'vocabulary', 'config.json'),
                        data = [
                            os.path.join(src_dir, 'data', 'lang', 'tgk', 'arzumanov-2019', 'vocabulary')
                        ]
                    )
                ]
            )
        )

    # TUR
    yield AnkiPackage (
        filename = os.path.join(out_dir, 'language', 'turkish.apkg'),
        deck = AnkiDeck(
                id = 1547350583,
                name = 'Language::Turkish',
                notes = [
                    AnkiNote(
                        model = os.path.join(src_dir, 'anki', 'lang', 'tur', 'vocabulary', 'model.json'),
                        template = os.path.join(src_dir, 'template', 'lang', 'tur', 'vocabulary', 'config.json'),
                        data = [
                            os.path.join(src_dir, 'data', 'lang', 'tur', 'guzev-2006'),
                            os.path.join(src_dir, 'data', 'lang', 'tur', 'tematyczny-9000')
                        ]
                    )
                ]
            )
        )

    # UIG
    yield AnkiPackage (
        filename = os.path.join(out_dir, 'language', 'uighur-cyrillic.apkg'),
        deck = AnkiDeck(
                id = 1102964059,
                name = 'Language::Uighur (Cyrillic)',
                notes = [
                    AnkiNote(
                        model = os.path.join(src_dir, 'anki', 'lang', 'uig', 'vocabulary-cyrl', 'model.json'),
                        template = os.path.join(src_dir, 'template', 'lang', 'uig', 'vocabulary', 'config.json'),
                        data = [
                            os.path.join(src_dir, 'data', 'lang', 'uig', 'kasymova-2005')
                        ]
                    )
                ]
            )
        )

    # UKR
    yield AnkiPackage (
        filename = os.path.join(out_dir, 'language', 'ukrainian.apkg'),
        deck = AnkiDeck(
                id = 1783697648,
                name = 'Language::Ukrainian',
                notes = [
                    AnkiNote(
                        model = os.path.join(src_dir, 'anki', 'lang', 'ukr', 'vocabulary', 'model.json'),
                        template = os.path.join(src_dir, 'template', 'lang', 'ukr', 'vocabulary', 'config.json'),
                        data = [
                            os.path.join(src_dir, 'data', 'lang', 'ukr', '___', 'vocabulary')
                        ]
                    )
                ]
            )
        )

    # UZB
    yield AnkiPackage (
        filename = os.path.join(out_dir, 'language', 'uzbek.apkg'),
        deck = AnkiDeck(
                id = 1257256040,
                name = 'Language::Uzbek',
                notes = [
                    AnkiNote(
                        model = os.path.join(src_dir, 'anki', 'lang', 'uzb', 'vocabulary', 'model.json'),
                        template = os.path.join(src_dir, 'template', 'lang', 'uzb', 'vocabulary', 'config.json'),
                        data = [
                            os.path.join(src_dir, 'data', 'lang', 'uzb', 'dla-sng')
                        ]
                    )
                ]
            )
        )

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
                            os.path.join(src_dir, 'data', 'lang', 'vie', 'colloquial-2012')
                        ]
                    )
                ]
            )
        )

    # # # # #  S C R I P T  # # # # #

    # BOPO
    yield AnkiPackage (
        filename = os.path.join(out_dir, 'script', 'cmn-bopo.apkg'),
        deck = AnkiDeck(
                id = 1806089108,
                name = 'Script::Bopomofo (Mandarin Chinese)',
                notes = [
                    AnkiNote(
                        model = os.path.join(src_dir, 'anki', 'script', 'bopo', 'model.json'),
                        template = os.path.join(src_dir, 'template', 'script', 'bopo', 'cmn', 'config.json'),
                        data = [
                            os.path.join(src_dir, 'data', 'script', 'bopo', 'zhuyin')
                        ]
                    )
                ]
            )
        )

    # DEVA
    yield AnkiPackage (
        filename = os.path.join(out_dir, 'script', 'hin-deva.apkg'),
        deck = AnkiDeck(
                id = 1315098045,
                name = 'Script::Devanagari (Hindi)',
                notes = [
                    AnkiNote(
                        model = os.path.join(src_dir, 'anki', 'script', 'deva', 'model.json'),
                        template = os.path.join(src_dir, 'template', 'script', 'deva', 'hin', 'config.json'),
                        data = [
                            os.path.join(src_dir, 'data', 'script', 'deva')
                        ]
                    )
                ]
            )
        )

    # JPAN
    yield AnkiPackage (
        filename = os.path.join(out_dir, 'script', 'jpn-hira.apkg'),
        deck = AnkiDeck(
                id = 2026188063,
                name = 'Script::Hiragana (Japanese)',
                notes = [
                    AnkiNote(
                        model = os.path.join(src_dir, 'anki', 'script', 'hrkt', 'model.json'),
                        template = os.path.join(src_dir, 'template', 'script', 'hrkt', 'config.json'),
                        data = [
                            os.path.join(src_dir, 'data', 'script', 'jpan', 'hiragana')
                        ]
                    )
                ]
            )
        )

    # THAI
    yield AnkiPackage (
        filename = os.path.join(out_dir, 'script', 'tha-thai.apkg'),
        deck = AnkiDeck(
                id = 1583324758,
                name = 'Script::Thai',
                notes = [
                    AnkiNote(
                        model = os.path.join(src_dir, 'anki', 'script', 'thai', 'model.json'),
                        template = os.path.join(src_dir, 'template', 'script', 'thai', 'tha', 'config.json'),
                        data = [
                            os.path.join(src_dir, 'data', 'script', 'thai')
                        ]
                    )
                ]
            )
        )