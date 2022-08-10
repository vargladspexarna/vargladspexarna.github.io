import utility.cleaner
import re, os, sys
import generateWebPage

path = os.path.join
wk_dir = os.path.dirname(os.path.realpath(__file__))+'/'

utility.cleaner.make_songtitle_bold(wk_dir=wk_dir)

utility.cleaner.remove_trailing_whitespace(wk_dir)

for i in range(2):
    utility.cleaner.add_trailing_whitespace(wk_dir)

utility.cleaner.spot_too_long_rows(wk_dir=wk_dir)
utility.cleaner.spot_lack_of_paragraphs(wk_dir=wk_dir)

utility.cleaner.add_melody_string_to_all(wk_dir=wk_dir)

generateWebPage.createFullWebPage(wk_dir=wk_dir, targetFile="index.html")

