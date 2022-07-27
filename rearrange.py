import shutil 
import pprint
import os
import re

is_spex = {}

wk_dir = os.path.dirname(os.path.realpath(__file__))+"/"
target = os.path.join(wk_dir, "target")

list_of_spex = os.listdir(os.path.join(wk_dir, "songTXT"))

for spex in list_of_spex:
    temp = re.split(r"\_\(", spex)
    spexname = re.sub(r"_", " ", temp[0])

    spex_folder = os.path.join(target, spexname)
    sem, year = re.split(r"_", re.findall(r"\w*_\d*",spex)[-1])

    spex_year_folder = os.path.join(spex_folder, year + " " + sem)

    try:
        os.mkdir(os.path.join(wk_dir, "target"))
    except:
        pass

    try:
        os.mkdir(spex_folder)
    except:
        pass
    
    try:
        os.mkdir(spex_year_folder)
    except:
        pass
    
    spex_folder_old = os.path.join(wk_dir, "songTXT", spex)

    for song in os.listdir(os.path.join(wk_dir, "songTXT", spex)):
        inp = open(os.path.join(spex_folder_old, song), "r+")
        songtext = inp.read()
        inp.close()

        outp = open(os.path.join(spex_folder, year + " "+ sem, song), "w+")
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
"Calamity Jane",
"2023 - Ett rymdäventyr",
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
    new = os.path.join(target, str(i) + "_" + spex)
    i+=1
    try: 
        os.rename(old, new)
    except:
        pass

getnum = lambda x: int(x.split("_")[0])


j = 1

entries = os.listdir(os.path.join(wk_dir, "target"))

for entry in entries:
    if re.match(r"\d{1,2}", entry):
        continue
    else:
        shutil.rmtree(os.path.join(wk_dir, "target", entry))

    if re.match("\d{4}", entry):
        print(entry)
    else:
        try:
            shutil.rmtree(os.path.join(wk_dir, "target", entry))
        except:
            pass

#Hardcoded removal of 2023
try:
    shutil.rmtree(os.path.join(wk_dir, "target", "2023 - Ett rymdäventyr"))
except:
    pass

spexSorted = os.listdir(os.path.join(wk_dir, "target"))
spexSorted.sort(key=getnum)

for spex in spexSorted:
    for year in os.listdir(os.path.join(wk_dir, "target", spex)):
        temp = year.split(" ")

        try:
            os.rename(os.path.join(wk_dir, "target", spex,
                year),os.path.join(wk_dir, "target", spex, temp[0]+"_" + temp[1]))
        except:
            pass

    for year in os.listdir(os.path.join(wk_dir, "target", spex)):
        for song in os.listdir(os.path.join(wk_dir, "target", spex, year)):
            old = os.path.join(wk_dir, "target", spex, year, song)
            new = os.path.join(wk_dir, "target", spex, year, re.sub("(\d+)\.[ ]*",
                r"\1_", song))
            os.rename(old, new)

for spex in spexSorted:
    sortedYear = os.listdir(os.path.join(wk_dir, "target", spex))
    sortedYear.sort(key=getnum)

    for year in sortedYear:
        sortedSongs =os.listdir(os.path.join(wk_dir, "target", spex, year)) 
        sortedSongs.sort(key=getnum)
    
    j = 0
    for year in sortedYear:
        sortedSongs =os.listdir(os.path.join(wk_dir, "target", spex, year)) 
        sortedSongs.sort(key=getnum)
        print("\n" , spex, year, "\n")
        for song in sortedSongs:
            j+=1

            old = song
            new = re.sub(r"\d+_", "{}_".format(j), song)
            os.rename(os.path.join(wk_dir, "target", spex, year, old),
                    os.path.join(wk_dir, "target", spex, year, new))



exit()
for list_folders in entries:
    for spex in list_folders:
        listlist = os.listdir(os.path.join(wk_dir, "target", spex))

        try:
            listlist.sort(key = lambda x: int(x.split("_")[0]))
        except:
            listlist.sort(key = lambda x: int(x.split(".")[0]))
        
        

        for item in listlist:

            old = os.path.join(test, spex, item)
            new = os.path.join(test, spex, re.sub(r"[0-9]{1,10}\.", str(j) + "_", item))
            new = re.sub("(\d+_)\s+", r"\1", new)
            os.rename(old, new)

            j+=1

exit()

