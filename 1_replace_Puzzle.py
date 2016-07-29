#Python challenge 2 - http://www.pythonchallenge.com/pc/def/map.html

oldinStr="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"
inStr=" http://www.pythonchallenge.com/pc/def/map.html"

inLis= list(inStr)
outLis= list(inStr)
keyStr="abcdefghijklmnopqrstuvwxyz"
keyLis=list(keyStr)
for r in range(len(inLis)):
    for i in range(26):
        if inLis[r] == keyLis[i]:
            #print(inLis[r])
            outLis[r] = keyLis[(i+2)%26]
print(inStr + "\n")
print(''.join(outLis))
Contact GitHub API Training Shop Blog About