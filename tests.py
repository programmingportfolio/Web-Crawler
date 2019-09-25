from conversions import listtostring, datatourl, convertkeywords, cleanwikiurls

def conversiontests(main):

    testinput1 = 'Web_Bot'
    testinput2 = 'Web Bot'
    testinput3 = ['web', 'bot']
    testinput4 = ['web', ' ', 'bot']
    testinput5 = '/wiki/crazy/stuff/more_stuff'

    print('Testinput1 underscore: ', datatourl(testinput1))
    print('Testinput2 regular user data: ', datatourl(testinput2))
    print('Testinput3 list: ', datatourl(listtostring(testinput3)))
    print('Testinput4 list with space: ', datatourl(listtostring(testinput4)))
    print('Testinput5 crazy url: ', cleanwikiurls(testinput5))

    convertokeyword = convertkeywords(datatourl(testinput1))
    print('ConvertToKeyword: ', convertokeyword)