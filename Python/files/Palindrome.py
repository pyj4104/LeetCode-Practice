def findPal(s):
    maxStr = lambda x, y: x if len(x) > len(y) else y
    retVal = s[0]
    for i in range(len(s)):
        candidate = checkPal(s, i)
        retVal = maxStr(retVal, checkPal(s, i))
    return retVal

def checkPal(s, index):
    eHRetVal = ''
    eLRetVal = ''
    oRetVal = ''
    # even length calc
    if index + 1 != len(s) and s[index] == s[index+1]:
        ehMid = (s[index] + s[index+1])
        eHRetVal = expandPal(s, '', index, index+1)
    if index > 0 and s[index] == s[index-1]:
        elMid = s[index] + s[index-1]
        eHRetVal = expandPal(s, '', index-1, index)

    eRetVal = eHRetVal if len(eHRetVal) > len(eLRetVal) else eLRetVal

    # odd length calc
    low = index
    high = index
    oRetVal = expandPal(s, s[index], index-1, index+1)

    return oRetVal if len(oRetVal) > len(eRetVal) else eRetVal

print(findPal("babad"))
print(findPal("cbbd"))
