import re, os, sys
import json
path = os.path.join

def remove_trailing_whitespace(wk_dir):
    i,j = 0,0
    for spex in os.listdir(path(wk_dir, "sparmen")):
        for year in os.listdir(path(wk_dir, "sparmen", spex)):
            for song in os.listdir(path(wk_dir, "sparmen", spex, year)):
                f=open(path(wk_dir, "sparmen", spex, year, song), "+r")
                songTXT_old = f.read()
                songTXT_new = re.sub(r"[\n]{3,100}", "", songTXT_old)

                if songTXT_old != songTXT_new:
                    i+=1
                else:
                    j+=1

                f.close()

                w=open(path(wk_dir, "sparmen", spex, year, song), "+w")
                w.write(songTXT_new)
                w.close()
        print("Cleaned up {} files in spex {}. {} were not cleaned.".format(i,
            spex,  j))

def add_trailing_whitespace(wk_dir, silent=True):
    for spex in os.listdir(path(wk_dir, "sparmen")):
        i, j  = 0, 0
        for year in os.listdir(path(wk_dir, "sparmen", spex)):
            for song in os.listdir(path(wk_dir, "sparmen", spex, year)):
                f=open(path(wk_dir, "sparmen", spex, year, song), "+r")
                songTXT_old = f.read()
                songTXT_new = songTXT_old + "\n"

                if songTXT_old != songTXT_new:
                    i+=1
                else:
                    j+=1

                f.close()

                w=open(path(wk_dir, "sparmen", spex, year, song), "+w")
                w.write(songTXT_new)
                w.close()
        if not silent:
            print("Added {} whitespaces in spex {}. {} songs were untouched.".format(i,
                spex,  j))

def is_bold(string):
    if re.search(r"<b>.*</b>", string):
        return True
    else:
        return False

def make_string_bold(string):
    return "<b>{}</b>\n".format(string[:-1])


def make_songtitle_bold(wk_dir, silent=True):
    for spex in os.listdir(path(wk_dir, "sparmen")):
        i, j  = 0, 0
        for year in os.listdir(path(wk_dir, "sparmen", spex)):
            for song in os.listdir(path(wk_dir, "sparmen", spex, year)):
                f=open(path(wk_dir, "sparmen", spex, year, song), "+r")
                songTXT_old = f.readlines()

                if is_bold(songTXT_old[0]):
                    pass
                else:
                    songTXT_old[0] = make_string_bold(songTXT_old[0])
                f.close()

                songTXT_new = "".join(songTXT_old)

                w=open(path(wk_dir, "sparmen", spex, year, song), "+w")
                w.write(songTXT_new)
                w.close()

def has_melody(string):
    if re.search(r"Melodi:", string):
        return True
    else:
        return False

def add_melody_string(string):
    return "Melodi: <i>{}</i>\n".format(string[:-1])

def is_melodi_italic(string):
    if re.search(r"<i>.*</i>", string):
        return True
    else:
        return False

def make_melodi_italic(string):

    return "<b>{}</b>\n".format(string[:-1])

def add_melody_string_to_all(wk_dir, silent=False):
    for spex in os.listdir(path(wk_dir, "sparmen")):
        i, j  = 0, 0
        for year in os.listdir(path(wk_dir, "sparmen", spex)):
            for song in os.listdir(path(wk_dir, "sparmen", spex, year)):
                f=open(path(wk_dir, "sparmen", spex, year, song), "+r")
                songTXT_old = f.readlines()

                if has_melody(songTXT_old[1]):
                    j += 1
                else:
                    i += 1
                    songTXT_old[1] = add_melody_string(songTXT_old[1])

                f.close()

                songTXT_new = "".join(songTXT_old)

                w=open(path(wk_dir, "sparmen", spex, year, song), "+w")
                w.write(songTXT_new)
                w.close()
        print('''Fixed {} songs by adding 'Melodi: <i></i>' in spex {}. {} remained untouched'''.format(i, spex, j))



def find_number_of_paragraphs(string):
    paragraphs = re.split(r"\n\n", string)

    return len(paragraphs)

def spot_lack_of_paragraphs(wk_dir, silent=False):
    DICT = {}

    for spex in os.listdir(path(wk_dir, "sparmen")):
        DICT[spex] = {}

        i, j  = 0, 0
        for year in os.listdir(path(wk_dir, "sparmen", spex)):
            DICT[spex][year] = []

            for song in os.listdir(path(wk_dir, "sparmen", spex, year)):
                f=open(path(wk_dir, "sparmen", spex, year, song), "+r")
                songTXT = f.read()
                f.close()

                M = find_number_of_paragraphs(songTXT)
                if M < 4:
                    DICT[spex][year].append(song)

    s = ""
    for spex in DICT.keys():
        s+="╔─────────────────────────────╗\n"
        s+=spex+"\n"
        for year in DICT[spex].keys():
            s+="+-"+year+"\n"
            for song in DICT[spex][year]:
                s+="+----" + song + "\n"
        s+='''╚─────────────────────────────╝'''+"\n"
        
    f=open("lacking_paragraphs.txt", "w+")
    f.write(s)
    f.close()

def spot_too_long_rows(wk_dir, silent=False):
    DICT = {}

    for spex in os.listdir(path(wk_dir, "sparmen")):
        DICT[spex] = {}

        i, j  = 0, 0
        for year in os.listdir(path(wk_dir, "sparmen", spex)):
            DICT[spex][year] = []

            for song in os.listdir(path(wk_dir, "sparmen", spex, year)):
                f=open(path(wk_dir, "sparmen", spex, year, song), "+r")
                songTXT = f.readlines()
                f.close()

                for row in songTXT[2:]: 
                    if len(row) > 60:
                        DICT[spex][year].append(song)
                        break

    s = ""
    for spex in DICT.keys():
        s+="╔─────────────────────────────╗\n"
        s+=spex+"\n"
        for year in DICT[spex].keys():
            s+="+-"+year+"\n"
            for song in DICT[spex][year]:
                s+="+----" + song + "\n"
        s+='''╚─────────────────────────────╝'''+"\n"
        
    f=open("too_long_rows.txt", "w+")
    f.write(s)
    f.close()
