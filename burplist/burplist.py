import xml.etree.ElementTree as ET
import urllib.parse
import base64
import re

#💥 💥 💥 A Simple code, But a Money Maker !!! 💥 💥 💥

tree = ET.parse("burp.xml")
root = tree.getroot()
wordlist = []

for i in root:
    wordlist += re.split('\/|\?|&|=',i[1].text)
    wordlist += re.split('\/|\?|&|=|_|-|\.|\+',i[1].text)

    wordlist += re.split('\/|\?|&|=|_|-|\.|\+|\:| |\n|\r|"|\'|<|>|{|}|\[|\]|`|~|\!|@|#|\$|;|,|\(|\)|\*|\|', urllib.parse.unquote(base64.b64decode(i[8].text.encode("utf-8")).decode('utf-8')))

    wordlist += re.split('\/|\?|&|=|\.|\+|\:| |\n|\r|"|\'|<|>|{|}|\[|\]|`|~|\!|@|#|\$|;|,|\(|\)|\*|\|', urllib.parse.unquote(base64.b64decode(i[8].text.encode("utf-8")).decode('utf-8')))

    if i[12].text is not None:
        wordlist += re.split('\/|\?|&|=|_|-|\.|\+|\:| |\n|\r|\t|"|\'|<|>|{|}|\[|\]|`|~|\!|@|#|\$|;|,|\(|\)|\*|\^|\\\\|\|', urllib.parse.unquote(base64.b64decode(i[12].text.encode("utf-8")).decode('utf-8')))

        wordlist += re.split('\/|\?|&|=|\.|\+|\:| |\n|\r|\t|"|\'|<|>|{|}|\[|\]|`|~|\!|@|#|\$|;|,|\(|\)|\*|\^|\\\\|\|', urllib.parse.unquote(base64.b64decode(i[12].text.encode("utf-8")).decode('utf-8')))

auxiliaryList = list(set(wordlist))

with open('wordlist.txt', 'w') as f:
    for item in auxiliaryList:
        f.write("%s\n" % item)

print ("wordlist saved to wordlist.txt")
