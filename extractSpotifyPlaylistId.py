import sys, pyperclip


extractFrom = str(sys.argv)


extractionObj = extractFrom.split("https://open.spotify.com/playlist/")
extractionObj1 = extractionObj[1].split("?")

finalExtract = extractionObj1[0]


print(f'Your playlist id is: {finalExtract} \nIt has been copied to clipboard.')

pyperclip.copy(finalExtract)


