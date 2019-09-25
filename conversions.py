
def listtostring(list):
    build = ''
    for word in list:
        build += ' ' + word
    return build.strip()

def cleanwikiurls(wikiurl):
    wikiurl = wikiurl.split('/')
    wikiurl = str(wikiurl[len(wikiurl) - 1])
    wikiurl = datatourl(wikiurl)

    return wikiurl


def datatourl(userdata):
    begin = 'https://en.wikipedia.org/wiki/'
    try:
        userdata = userdata.strip('_')
    except:
        pass
    try:
        userdata = userdata.strip()
    except:
        pass
    try:
        userdata = userdata.split()
        capital1 = userdata[0][0:1].upper()
        trail1 = userdata[0][1:].lower()
        urlpart1 = capital1 + trail1
    except:
        print('Invalid data.')
        return ''

    try:
        trail2 = userdata[1][0:].lower()
        urlpart2 = urlpart1 + '_' + trail2
    except:
        urlpart2 = urlpart1


    return begin + urlpart2


def convertkeywords(url):
    keywords = []
    if(url.find('/')):
        url = url.split('/')
        url = str(url[len(url) - 1])

    if (url.find('_')):
        url = url.split('_')
    else:
        url = url.split()

    capital1 = url[0][0:1].upper()
    trail1 = url[0][1:].lower()
    urlpart1 = capital1 + trail1
    keywords.append(urlpart1)
    try:
        trail2 = url[1][0:].lower()
        keywords.append(trail2)
    except:
        pass
    return keywords

def parseandprint(destination, tobeparsedlinks):
    position = 0
    build = ''
    stringcount = 0;
    stringarray = []

    for link in tobeparsedlinks:

        if(link == destination):
            temp = tobeparsedlinks[0:position + 1]
            position = 0
            for link in temp:
                build += link + '->'
            stringarray[stringcount] = build
            stringcount += 1
        position += 1

    for linkbuild in stringarray:
        print('Link build: ', linkbuild)