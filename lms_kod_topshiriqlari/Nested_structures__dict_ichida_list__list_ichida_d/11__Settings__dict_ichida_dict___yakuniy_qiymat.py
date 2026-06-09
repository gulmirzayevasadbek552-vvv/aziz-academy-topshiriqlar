th1, lang1, dbg1 = input().split()
th2, lang2, dbg2 = input().split()

settings = {
    'theme': th1,
    'lang': lang1,
    'debug': True if dbg1 == '1' else False,
    'override': {
        'theme': th2,
        'lang': lang2,
        'debug': None if dbg2 == '-' else (True if dbg2 == '1' else False)
    }
}

if settings['override']['theme'] !='-':
    theme = settings['override']['theme']
else:
    theme = settings['theme']
if settings['override']['lang'] !='-':
    lang = settings['override']['lang']
else:
    lang = settings['lang']
if settings['override']['debug'] is None:
    debug = settings['debug']
else:
    debug = settings['override']['debug']
print(theme, lang, int(debug))