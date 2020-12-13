from collections import OrderedDict
from prettytable import PrettyTable
from re import sub



def convQZIJ(mod, txt):
    txt = txt.upper()
    if mod == "QZ":
        while True:
            if "Z" in txt:
                txt = txt.replace('Z','Q')
            else:
                break
    if mod == "IJ":
        while True:

            if "J" in txt:
                txt = txt.replace('J','I')
            else:
                break
    return txt


def pfbox(keyText, mod):
    stream = convQZIJ(mod, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    stream = ''.join(OrderedDict.fromkeys(stream))
    keyText = convQZIJ(mod, keyText)
    keyText = ''.join(OrderedDict.fromkeys(keyText))

    pbox = [['', '', '', '', ''],
            ['', '', '', '', ''],
            ['', '', '', '', ''],
            ['', '', '', '', ''],
            ['', '', '', '', '']
            ]

    for i in range(5):
        for j in range(5):
            if len(keyText) != 0:
                pbox[i][j] = keyText[0]
                stream = stream.replace(keyText[0],"")
                if len(keyText) == 1:
                    keyText = ""
                else:
                    keyText = keyText[1:]
            else:
                pbox[i][j] = stream[0]
                stream = stream[1:]
    t = PrettyTable()
    t.add_rows(pbox)
    print(t)
    return pbox


def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))

def makelist(targetText):
    prelist = []
    templist = []
    for i in range(len(targetText)//2):
        for j in range(1):
            templist.append(targetText[0])
            if targetText[0] == targetText[1]:
                templist.append("X")
                targetText = targetText[1:]
            else:
                templist.append(targetText[1])
                targetText = targetText[2:]

        prelist.append(templist)
        templist = []
    if targetText != "":
        prelist.append([targetText[0],'X'])
    return prelist

def encoding(list,box):
    prolist = []
    enctemp = []
    for i in range(len(list)):
        primeX, primeY = index_2d(box, list[i][0])
        seconX, seconY = index_2d(box, list[i][1])
        if primeX == seconX:
            reprm = box[primeX][(primeY+1)%5]
            rescd = box[seconX][(seconY+1)%5]
            enctemp = [reprm,rescd]
        elif primeY == seconY:
            reprm = box[(primeX+1)%5][primeY]
            rescd = box[(seconX+1)%5][seconY]
            enctemp = [reprm,rescd]
        else:
            reprm = box[seconX][primeY]
            rescd = box[primeX][seconY]
            enctemp = [reprm,rescd]
        prolist.append(enctemp)
    return prolist

def decoding(list, box):
    prolist = []
    enctemp = []
    for i in range(len(list)):
        primeX, primeY = index_2d(box, list[i][0])
        seconX, seconY = index_2d(box, list[i][1])
        if primeX == seconX:
            reprm = box[primeX][(primeY +4) % 5]
            rescd = box[seconX][(seconY +4) % 5]
            enctemp = [reprm, rescd]
        elif primeY == seconY:
            reprm = box[(primeX +4) % 5][primeY]
            rescd = box[(seconX +4) % 5][seconY]
            enctemp = [reprm, rescd]
        else:
            reprm = box[seconX][primeY]
            rescd = box[primeX][seconY]
            enctemp = [reprm, rescd]
        prolist.append(enctemp)
    return prolist


if __name__ == "__main__":
    while True:
        mode = input("Select Pbox mod: IJ/QZ")
        if mode != "QZ" and mode != "IJ":
            print("Invalid mode: %s"%mode)
        else:
            break

    while True:
        key = input("type Key: ")
        if key.isalpha() != True:
            print("Invalid key %s: Key must be alphabet only."%key)
            continue
        else:
            break
    print("\n")
    box = pfbox(key,mode)

    while True:
        text = input("Type String: ")
        text = text.upper()
        text = sub(r'[^A-Z]','',text)
        if text == "":
            print("Invalid input!")
            continue
        break

    list = makelist(text)
    #print(list)

    while True:
        enmode = input("encode/decode: ")
        if enmode == "encode":
            encodedTxt = encoding(list,box)
            #print(encodedTxt)
            result = ''
            for i in encodedTxt:
                tem = ''.join(i)
                result += tem
            print("encoded result: "+result)
            break
        elif enmode == "decode":
            decodedTxt = decoding(list,box)
            result = ''
            for i in decodedTxt:
                tem = ''.join(i)
                result += tem
            print("decoded result: "+result)
            break
        else:
            print("Invalid mode %s" %enmode)
