import os
from bs4 import BeautifulSoup
from urllib.request import urlopen
from conversions import listtostring, datatourl, convertkeywords, cleanwikiurls, parseandprint
from tests import conversiontests
#begin search until something is relevant, and then continue searching until is no longer relevant

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print('Directory Path', dir_path)
    i = 0




    origininput = input('\n Type something like Web Bot here \n$ ')
    parenturl = datatourl(origininput)

    destinput = input('\n Type something like Tax Holiday here \n$ ')
    destination = datatourl(destinput)

    keywords = convertkeywords(destination)

    tobeparsedlinks = []

    tobeparsedlinks += beginsearch(parenturl, destination, keywords)

    parseandprint(destination, tobeparsedlinks)

    print('Links to be parsed', tobeparsedlinks)


def beginsearch(parenturl, destination, keywords):
    i = 0
    relevancy = False
    relevantlinkcount = 0

    relevantlinks = []

    previouslinks = []

    rabbitholes = []

#degrees of how far the beginsearch will look for relevancy
    while(i < 1):
        if (i == 0):
            irrelevantlinks = simplelinks(parenturl)
            print('links', irrelevantlinks)
        else:
            irrelevantlinks = []
            print('previous links', previouslinks)
            print('much larger iteration')

            for link in previouslinks:
                print('getting links')
                irrelevantlinks += simplelinks(str(link))

            print('complete')
            print(irrelevantlinks)
        for irrelevantlink in irrelevantlinks:
            print('irrelevantlink', irrelevantlink)
            try:
                irrelevantlinkhtml = urlopen(irrelevantlink).read()
                irrelevantsoup = BeautifulSoup(irrelevantlinkhtml, 'html.parser')
                # pass in entire text of documents
                irrelevant1 = str(irrelevantsoup.get_text()).count(keywords[0])
                irrelevant2 = str(irrelevantsoup.get_text()).count(keywords[1])
                print('counts', irrelevant1, irrelevant2)

                if (irrelevant1 > 4 or irrelevant2 > 4):
                    print('relevancy met')
                    relevantlinks[relevantlinkcount] = irrelevantlink
                    relevantlinkcount += 1
                    relevancy = True
                else:
                    pass
            except:
                print('failed to open url')
                pass
        print("Complete iteration")


        if(relevancy):
            print('relevantlinks', relevantlinks)
            for relevantlink in relevantlinks:
                if(relevantlink == destination):
                    return rabbitholes.append(parenturl, relevantlink)
                print('relevant link', relevantlink)
                rabbitholes.append(parenturl)
                rabbitholes += searchagain(relevantlink, destination, keywords)
        else:
            print('i addition')
            previouslinks = irrelevantlinks

        i += 1

    print('Completed all iterations')

    return rabbitholes


def searchagain(parenturl, destination, keywords):

    finalword = str(keywords[0] + ' ' + keywords[1])
    wildgoosechase = True

    i = 0
    relevancy = False
    relevantlinks = []

    nothing = []


    rabbitholes = []


    while (wildgoosechase):
        irrelevantlinks = simplelinks(parenturl)
        print('links', irrelevantlinks)

        for irrelevantlink in irrelevantlinks:
            print('irrelevantlink', irrelevantlink)

            try:
                irrelevantlinkhtml = urlopen(irrelevantlink).read()
                irrelevantsoup = BeautifulSoup(irrelevantlinkhtml, 'html.parser')
                # pass in entire text of documents
                irrelevant1 = str(irrelevantsoup.get_text()).count(keywords[0])
                irrelevant2 = str(irrelevantsoup.get_text()).count(keywords[1])
                irrelevant3 = str(irrelevantsoup.get_text()).count(finalword)

                print('counts', irrelevant1, irrelevant2)

                if (irrelevant1 > 20 or irrelevant2 > 20 or irrelevant3 > 20):
                    if(irrelevantlink == destination):
                        return rabbitholes.append(parenturl, irrelevantlink, destination)
                    else:
                        print('relevancy met')
                        relevantlinks.append(irrelevantlink)
                        relevancy = True
                else:
                    print('Dropping wild goose chase.')
                    wildgoosechase = True
            except:
                print('failed to open url')
                pass
        print("Complete iteration")

        if (relevancy):
            print('relevantlinks', relevantlinks)
            for relevantlink in relevantlinks:
                print('relevant link', relevantlink)
                rabbitholes += searchagain(relevantlink, destination, keywords)
        elif(wildgoosechase):
            return nothing
        else:
            return nothing

        i += 1

    print('Completed all iterations in searchagain')


def simplelinks(url):
    try:
        html = urlopen(url).read()
    except:
        clear = []
        return clear
    soup = BeautifulSoup(html, 'html.parser')
    wiki = 'wiki'
    results = []
    for link in soup.find_all('a'):
        href = link.get('href')
        find = str(href).find(wiki)
        if (find == True):
            results.append(cleanwikiurls(href))
    return results



main()