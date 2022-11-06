import os 
import re

wk_dir = os.path.dirname(os.path.realpath(__file__))+'/'
spex = os.listdir(os.path.join(wk_dir, "sparmen"))



    # < (less than)
    # > (greater than)
    # : (colon)
    # “ (double quote)
    # / (forward slash)
    # \ (backslash)
    # | (vertical bar or pipe)
    # ? (question mark)
    # * (asterisk)

forbidden_characters_windows = '<>:"/\\|?*'

for spex in os.listdir(os.path.join(wk_dir, "sparmen")):
    for year in os.listdir(os.path.join(wk_dir, "sparmen", spex)):
        for song in os.listdir(os.path.join(wk_dir, "sparmen", spex, year)):
            full_path_old = os.path.join(wk_dir, "sparmen", spex, year, song)
            num = re.match("\d+", song)

            if num:
                print(num.group(0))

            full_path_new = os.path.join(wk_dir, "sparmen", spex, year,
                    num.group(0) + ".txt")
            
