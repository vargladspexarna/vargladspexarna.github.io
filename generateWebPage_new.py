import os
import platform
import re
from datetime import date
from itertools import cycle

from importlib import reload
import misc

reload(misc)

def extractNum(entry):
    return int(re.findall(r"\d+", entry)[0])

replaceaao = misc.replaceaao
fix_youtube_url = misc.fix_youtube_url

today = date.today()

print("Today is:  {} \n".format(today))

bigSpexButtonIDs = cycle(["two","one"])
songCycle = cycle(["two","one"])

wk_dir = os.path.dirname(os.path.realpath(__file__))+'/'

def getSpexSets(spex):
    '''
    Extracts every set (1998 VT, 2002 VT...) for a given spex
    and returns a more readable format (VT98, VT02...)

    Will be used for the big spexbutton
    E.g., [   1. Karnevalssaga (VT98, VT02..)    ]
    '''

    sortedYear = os.listdir(os.path.join(wk_dir, "sparmen", spex))
    sortedYear.sort(key=extractNum)

    string_part_sets  = "("

    for year in sortedYear:
        temp = year.split("_")
        string_part_sets +=temp[1] + temp[0][2:]+", "

    string_part_sets = string_part_sets[:-2]
    string_part_sets += ")"

    string_part_sets = re.sub(r"Kivik", "S", string_part_sets)
    string_part_sets = re.sub(r"Karnevalen", "K", string_part_sets)

    title = re.sub(r"[_]", ". ", spex) + " " + string_part_sets

    return title

def createDivForMain():
    sortedSpex = os.listdir(os.path.join(wk_dir, "sparmen"))
    sortedSpex.sort(key=extractNum)

    stringDivMain = ""

    for spex in sortedSpex:
        stringDivMain += createBigSpexButton(spex)
        stringDivMain += createDivForSpex(spex)

    stringDivMain ='''
        {}
        '''.format(stringDivMain)

    return createDivMain(stringDivMain)



def createBigSpexButton(spex):
    spexTITLE = getSpexSets(spex)

    spexString = '''
    <button class="sp" id="{}">{}</button>
    '''.format(next(bigSpexButtonIDs), spexTITLE)
    return spexString

def createDivForSpex(spex):
    '''
    This function creates 
    '''
    sortedYears = os.listdir(os.path.join(wk_dir, "sparmen", spex)) 
    sortedYears.sort(key=extractNum)

    spexDIV = ""

    for year in sortedYears:

        yearString = createYearButton(spex, year)
        yearString += createDivForSongs(spex, year)
        
        spexDIV += yearString
    
    spexDIV += createBlocker()

    spexDIV = '''
        {}
        '''.format(spexDIV)

    spexDIV = '''
        <div class="content">
        {}
        </div>
        '''.format(spexDIV)

    return spexDIV

def createBlocker():
    blockerSTRING = '''<button class="sb"
    style="background-color:green;color:white;text-align:left;font-weight:bold;font-size:2;"></button>
    '''
    return blockerSTRING


def createYearButton(spex, year):
    yearTITLE = re.sub(r"_.+", " ", year)
    yearTITLE = re.sub(r"[-]*.txt", "", yearTITLE)

    titleBox = '''<button class="sb"
    style="background-color:#1a1a1a;color:white;text-align:left;font-weight:bold;font-size:20;border-left:2px-solid-red;">{}</button>
    '''.format(yearTITLE)
    return titleBox

def createSongButton(title):
    oneSong = '''
      <button class="sb" id="{}">{}</button>
    '''.format(next(songCycle), title)
    return oneSong

def createDivForSong(text):
    div =  '''
          <div class="song">
            {}
          </div> 
          '''
    try:
        div = div.format(text)
    except:
        print("createDivForSong failed for:\n {}   {}   {}".format(spex, year, song))
    return div

def createDivForSongs(spex, year):
    sortedSongs = os.listdir(os.path.join(wk_dir, "sparmen", spex, year)) 
    sortedSongs.sort(key=extractNum)

    songDIV = ""
    for song in sortedSongs:
        # print(spex, year, song)
        songURL = os.path.join(wk_dir, "sparmen", spex, year, song)
        songTITLE = re.sub(r"_", ". ", song)
        songTITLE = re.sub(r"[-]*.txt", "", songTITLE)

        f = open(songURL, "r+")
        songTXT = f.read()
        f.close()
        songTXT = re.sub(r'\n', '<br>', songTXT)
        
        # Create song button 
        songDIV += createSongButton(songTITLE)

        # Create song container
        songDIV += createDivForSong(songTXT)

    spexString = '''
        {}
        '''

    return spexString.format(songDIV)

def createDivMain(content):

    divString = '''
        <div class="main">
        {}
        </div>
    '''.format(content)

    return divString


f = open(wk_dir + 'pageTemplate.html', 'r')
webPageTemplate = f.read()
f.close()

webPageString = re.sub(r'MONSTERSTRINGHERE', createDivForMain() , webPageTemplate)
webPageString = replaceaao(webPageString)
webPageString = re.sub(r'DATUM', 'Uppdaterad: {}'.format(today),webPageString)

targetURL = os.path.join(wk_dir, "index_new.html")

print('Attempting to write {}. \n\t Full path: {}'.format("index_new.html",
    targetURL))

w = open(targetURL, 'w')
w.write(webPageString)
w.close()

exit()


