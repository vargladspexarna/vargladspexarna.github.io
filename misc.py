import re

def replaceaao(STRING):
    STRING = re.sub(r'ä', '&auml', STRING)
    STRING = re.sub(r'å', '&aring', STRING)
    STRING = re.sub(r'ö', '&ouml', STRING)
    STRING = re.sub(r'Ä', '&Auml', STRING)
    STRING = re.sub(r'Å', '&Aring', STRING)
    STRING = re.sub(r'Ö', '&Ouml', STRING)
    # Fuck you 2023
    STRING = re.sub(r'202\s3', '2023', STRING)
    STRING = re.sub(r'–', '-', STRING)
    STRING = re.sub(r'é', '&eacute', STRING)
    STRING = re.sub(r'’', '', STRING)
    STRING = re.sub(r'´', '', STRING)
    STRING = re.sub(r"æ", "&aelig;", STRING)
    STRING = re.sub(r"ø", "&oslash;", STRING)
    STRING = re.sub(r"å", "&aring;", STRING)
    STRING = re.sub(r"Æ", "&AElig;", STRING)
    STRING = re.sub(r"Ø", "&Oslash;", STRING)
    STRING = re.sub(r"Å", "&Aring;", STRING)
    STRING = re.sub(r'ß', '&szlig', STRING)
    STRING = re.sub(r'ü', '&uuml', STRING)
    STRING = re.sub(r'Ä', '&Auml', STRING)
    STRING = re.sub(r'Ö', '&Ouml', STRING)
    STRING = re.sub(r'Ü', '&Uuml', STRING)
    STRING = re.sub(r'10.16', '10.6.16', STRING)
    return STRING

def fix_youtube_url(STRING):
    STRING = re.sub(r'ä', '%C3%A4', STRING)
    STRING = re.sub(r'å', '%C3%A5', STRING)
    STRING = re.sub(r'ö', '%C3%B6', STRING)
    STRING = re.sub(r'Ä', '%C3%84', STRING)
    STRING = re.sub(r'Å', '%C3%85', STRING)
    STRING = re.sub(r'Ö', '%C3%96', STRING)
    STRING = re.sub(r'–', '&ndash', STRING)
    STRING = re.sub(r'é', '&eacute', STRING)
    return STRING
