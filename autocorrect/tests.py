from spellchecker import SpellChecker
spell = SpellChecker()


def autocorrect(userinput):
    userinput = userinput.lower()
    # find those words that may be misspelled
    toCheckString = userinput
    toCheckList = 'autocorrect'.split()
    misspelled = spell.unknown(toCheckList)

    unknownindex = []
    correctedlist = []
    for word in misspelled:
        unknownindex.append(toCheckList.index(word))
        try:
            correctedlist.append(spell.correction(word))
        except:
            correctedlist.append(word)
        print(correctedlist)
        print('this is a' + word)

    output = []

    for i in range(len(toCheckList)):
        if i not in unknownindex:
            output.append(toCheckList[i])
        else:
            output.append(correctedlist[unknownindex.index(i)])


    outputString =  ''
    for word in output:
        if outputString == '':
            outputString += word
        else: 
            outputString = outputString + ' ' + word

    return outputString

print(autocorrect("autocorrect"))