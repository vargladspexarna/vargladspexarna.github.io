import os
import re
list_of_spex = os.listdir("songTXT")

is_spex = {}

target = "/home/mumrah/sparmen-master/target/"

for spex in list_of_spex:
    temp = re.split(r"\_\(", spex)
    spexname = re.sub(r"_", " ", temp[0])

    spex_folder = os.path.join(target, spexname)
    sem, year = re.split(r"_", re.findall(r"\w*_\d*",spex)[-1])

    spex_year_folder = os.path.join(spex_folder, year + " " + sem)


    try:
        os.mkdir(spex_folder)
    except:
        pass
    
    try:
        os.mkdir(spex_year_folder)
    except:
        pass
    
    spex_folder_old = os.path.join("/home/mumrah/sparmen-master/songTXT/", spex)

    for song in os.listdir(os.path.join("/home/mumrah/sparmen-master/songTXT/", spex)):
        inp = open(os.path.join(spex_folder_old, song), "r+")
        songtext = inp.read()
        inp.close()

        outp = open(os.path.join(spex_folder, year + " " + sem, song), "w+")
        outp.write(songtext)
        outp.close()


ordered_list = ["En Karnevalssaga",
"Odysseus Återkomst",
"Amasonernas Återkomst",
"Alexander Den Store Återkommer",
"Gaius-Caligula",
"Marco Polo",
"Tutankhanmun",
"Pizarro",
"Fantomen på AF",
"DIII",
"Sherlock Holmes",
"Tors Hammare",
"Frankenstein",
"Livet i Revy",
"Leonardo",
"Platon och Dualismen",
"Kiviks Musteri",
"Mata Hari",
"Ivanhoe",
"Möllan Rouge",
"Spartacus",
"Titanic",
"Äppelkungen och de sista snapphanarna",
"GIII",
"2023 - Ett rymdäventyr",
"Calamity Jane",
"Muren",
"Drottning Kristina",
"Fritiof Piraten",
"Falklandskriget",
"Kompani Kivik",
"Svärdet i Stenen",
"Tusen och en Natt",
"Kluedo",
"Heliga Valborg",]

i=1

for spex in ordered_list:
    old = os.path.join(target, spex)
    new = os.path.join(target, str(i) + ". " + spex)
    i+=1
    try: 
        os.rename(old, new)
    except:
        pass

getnum = lambda x: int(x.split(".")[0])

test = "/home/mumrah/sparmen-master/target/1. En Karnevalssaga/"
test = os.listdir(test)
test.sort(key =lambda x: int(x.split(" ")[0]))
list_folders = test


test = "/home/mumrah/sparmen-master/target/1. En Karnevalssaga/"

j = 1

for spex in list_folders:
    listlist = os.listdir(test +spex)
    listlist.sort(key = lambda x: int(x.split(".")[0]))
    
    

    for item in listlist:

        old = os.path.join(test, spex, item)
        new = os.path.join(test, spex, re.sub(r"[0-9]{1,10}\.", str(j) + ". ", item))
        os.rename(old, new)

        j+=1

exit()

