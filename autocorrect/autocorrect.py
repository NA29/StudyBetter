from spellchecker import SpellChecker
spell = SpellChecker()


def autocorrect(userinput):
    userinput = userinput.lower()
    # find those words that may be misspelled
    toCheckString = userinput
    toCheckList = userinput.split()
    misspelled = spell.unknown(toCheckList)

    unknownindex = []
    correctedlist = []
    for word in misspelled:
        # Get the one `most likely` answer
        unknownindex.append(toCheckList.index(word))
        correctedlist.append(spell.correction(word))
        if None in correctedlist:
            correctedlist[correctedlist.index(None)] = word

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


    # print(unknownindex)
    # print(correctedlist)
    # print(output)
    # print('-----------------------------------------')
    # print('Before autocorrect: ' + toCheckString)
    # print('After autocorrect: ' + outputString)

    return outputString

#print(autocorrect('ES AND MONG ERYON I I JUST WANTED TO REMIND YOU GUYS THAT WE ARE CHAINE OUR BOGLE FLUTTER WORKSHOP IN THE DOWNSTAIRS GOOD LEK AND HAVE FUN SEE YOU GUYS AFER'))