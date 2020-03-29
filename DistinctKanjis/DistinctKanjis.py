#-*- coding:utf-8 -*-
import re

def isKanji(char):
    #Accepts: a single char
    #Returns: True if it is a Kanji, False if it is not a Kanji
    
    #Kanjis in unicode: https://zetawiki.com/wiki/%EC%9C%A0%EB%8B%88%EC%BD%94%EB%93%9C_%ED%95%9C%EC%9E%90
    #Only included ones within UTF-8 range.
    regex = re.compile(r"[\u4E00-\u9FBF]|[\u3400-\u4DBF]|[\u2E80-\u2EFF]|[\uF900-\uFAFF]")
    if regex.match(char) != None:
        return True
    else:
        return False
fName = input("input text> ")
f = open(fName,"r",encoding="utf8")
rawData = f.read()

lKanji = []
for char in rawData:
    if isKanji(char):
        lKanji.append(char)

lKanji = list(set(lKanji)) #remove overlapping ones
print(str(len(lKanji)) + " Kanjis are present.")

if input("Press y and Enter if you want to get list of characters present> ").lower().strip() == "y":
    for char in lKanji:
        print(char, end=" ")