import os, sys, re
from datetime import date
from itertools import cycle
import platform

today = date.today()

spexString ='''
<button class="sp" id="one">SPEX</button>
<div class="content">
SONGS
</div>
'''

spexString2 ='''
<button class="sp" id="two">SPEX</button>
<div class="content">
SONGS
</div>
'''

SS = cycle([spexString,spexString2])

oneSong = '''
  <button class="sb" id="one">SONGTITLE</button>
  <div class="song">
    SONGTEXT
  </div>
'''

oneSong2 = '''
  <button class="sb" id="two">SONGTITLE</button>
  <div class="song">
    SONGTEXT
  </div>

'''
OS = cycle([oneSong, oneSong2])

titleBox = '''<button class="sb" style="background-color:black;color:white;text-align:left;font-weight:bold;font-size:20;">YEAR</button>
<div class="song" id="three">
</div>'''

titleBox = ''

def genPage(showMelody=True, showYoutube=True):
    if platform.system() == 'Linux':
        wk_dir = os.path.dirname(os.path.realpath(__file__))+'/'
    elif platform.system() == 'Windows':
        wk_dir = os.path.dirname(os.path.realpath(__file__))+'/'
        wk_dir = re.sub(r'[\]', '/', wk_dir)

    # wk_dir = input('Gief work directory')
    print('Current wkdir is {}'.format(wk_dir))

    if 'songTXT' in os.listdir(wk_dir):
        print('\n This folder contain songTXT. Good job!')
    else:
        print('\n This folder does not contain songTXT :(')

    urlToSongs = wk_dir + '/songTXT/'
    monsterString = ''

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
    def replaceaao2(STRING):
        STRING = re.sub(r'ä', '%C3%A4', STRING)
        STRING = re.sub(r'å', '%C3%A5', STRING)
        STRING = re.sub(r'ö', '%C3%B6', STRING)
        STRING = re.sub(r'Ä', '%C3%84', STRING)
        STRING = re.sub(r'Å', '%C3%85', STRING)
        STRING = re.sub(r'Ö', '%C3%96', STRING)
        STRING = re.sub(r'–', '&ndash', STRING)
        STRING = re.sub(r'é', '&eacute', STRING)
        return STRING

    # sort those fuckers by year.
    spexPlural = os.listdir(urlToSongs)
    test = [[j1, j2] for j1, j2 in zip(spexPlural, [re.search(r'\d\d\d\d', i).group(0) for i in spexPlural])]

    test.sort(key=lambda t: t[1])

    spexCounter = 0
    spexDict = {}
    bigSongCounter = 0
    bigSpexCounter = 0
    sommarSpexCounter = 0
    karnevalsSpexCounter = 0

    for spex, year in test:
        spexName = re.split(r'[(]', spex)[0]
        bigSpexCounter += 1
        if spexName not in spexDict.keys():
            spexCounter += 1
            spexDict[spexName] = {'num': spexCounter, 'spex': spexName, 'urls': []}
            if spexName == 'Trollet_Återvander_':
                spexCounter += -1
                spexDict[spexName] = {'num': '1337', 'spex': spexName, 'urls': []}

        spexDict[spexName]['urls'].append(urlToSongs + spex + '/')

    for button in spexDict.keys():
        spexCounter = spexDict[button]['num']

        currentSpexString = next(SS)
        title ='<b>'+ str(spexCounter)+'</b>'+ '&nbsp'*5 + re.sub(r'[_]', ' ', button) + '&nbsp'*5 + '['

        storeSongs = []
        songCounter = 0
        for song in spexDict[button]['urls']:

            list_of_songs = os.listdir(song)
            list_of_songs = [i.split('.', maxsplit=1) for i in list_of_songs]
            list_of_songs.sort(key=lambda x:int(x[0]))
            list_of_songs = ['.'.join(i) for i in list_of_songs]

            y = re.findall(r'\d\d', song)[-1]
            storeSongs.append(re.sub('YEAR', re.findall(r'\d\d\d\d', song)[-1], titleBox))
            sem = re.split('_', song)[-2][1:]

            if sem == 'Karnevalen':
                sem = 'K'
                karnevalsSpexCounter +=1
            elif sem == 'Kivik':
                sommarSpexCounter += 1
                sem = 'S'
            elif len(sem) != 2:
                sem = 'E'

            title += sem + y + ', '

            for song2 in list_of_songs:
                songCounter += 1

                f = open(song + song2, 'r')
                try:
                    sname = re.sub(r'\d+[.]\s', '', f.readlines(1)[0])

                    songName = '<b>' + str(spexCounter) +  '.' + str(songCounter)  + '&nbsp'*5+ sname + '</b>'
                    songText = f.read()
                except:
                    pass
                f.close()

                songText = re.sub(r'\n', '<br>', songText)
                m = re.split(r'<br>',songText)

                if showMelody == True:
                    if showYoutube == True:
                        search = re.split(' ', m[0])
                        if search[0] == 'Melodi:' or search[0]=='melodi:':
                            search.pop(0)
                        s1 = 'https://www.youtube.com/results?search_query='
                        s1 = s1 + '+'.join(search)
                        s1 = replaceaao2(s1)
                        search = '<a href="' + s1+'" target="_blank">' + 'YouTube' + '</a>'
                    else:
                        search = ''
                    m[0] = '<i><b><small>' + m[0] + '</small></b></i><br>' + search
                else:
                    m[0] = '\n'

                songText = '<br>'.join(m)
                currentSong = re.sub(r'SONGTITLE', songName, next(OS))
                storeSongs.append(re.sub(r'SONGTEXT', songText, currentSong))

        currentSpexString = re.sub(r'SPEX', title[:-2]+']', currentSpexString)
        currentSpexString = re.sub(r'SONGS', ''.join(storeSongs), currentSpexString)

        monsterString += currentSpexString
        bigSongCounter += songCounter

    #read webpage TEMPLATE
    f = open(wk_dir + 'pageTemplate.html', 'r')
    webPageTemplate = f.read()
    f.close()
    print('Creating webpage template.')
    webPageString = re.sub(r'MONSTERSTRINGHERE',monsterString, webPageTemplate)

    # HTML är ju kul. Ersätter åäö med kompatiblare tecken.
    webPageString = replaceaao(webPageString)
    webPageString = re.sub(r'DATUM', 'Uppdaterad: {}'.format(today),webPageString)
    webPageString = re.sub(r'DATUM', '',webPageString)
    #write webpage FULL
    webpageURL = wk_dir +'index.html'
    print('Writing webpage to file {}')
    w = open(webpageURL, 'w')
    w.write(webPageString)
    w.close()
    if 'webPage{}.html'.format(str(showMelody)) in os.listdir(wk_dir):
        print('webPage{}.html'.format(str(showMelody))+'is in your working directory!')
        print('All is well, enjoy your new webpage!')


    for spex in os.listdir(urlToSongs):
        for song in os.listdir(urlToSongs + spex):
            f = open(urlToSongs + spex + '/' + song, 'r')
            digit = re.split('[.]', song)[0]
            m = f.readline()
            f.close()
            m = re.sub(r'[/\n\.]', '-', m)

            os.rename(urlToSongs + spex +'/' + song,
                      urlToSongs + spex +'/' + digit + '.' + m + '.txt')


genPage(showMelody=True, showYoutube=True)
