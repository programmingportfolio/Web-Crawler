# Web-Crawler

## Customer Requirements

The Wikipedia game:

Problem: 
	Given a starting page on Wikipedia, using connected pages, find a list of linked pages to a target page.

	For example, starting at the page: "Web Bot" and target page: "Tax Holiday". Web Bot has a link to the page "Barack Obama", which has a link to "Tax credit", which has a link to the page "Tax holiday", the end page. Therefore, the answer would be:

	Web Bot -> Barack Obama -> Tax credit -> Tax holiday

	I would run through this path way yourself to understand the problem:
	https://en.wikipedia.org/wiki/Web_Bot

Instructions:
	We're looking for a Python program called "wikipedia_game.py" that takes a source page and target page as command line arguments and you give me the list of connected links from start to end. Please zip up the wikipedia_game.py program along with a requirements.txt (if you used any pip packages) and any other resources used to solve the problem. Try to make sure that after unzipping and installing any pip requirements that the python program will run in it's current directory. If you have a more advanced solution, for example using a database, please provide instructions to set it up.

	Given this input for the python pogram:
	python wikipedia_game.py "Web Bot" "Tax Holiday"
	We should get this output:
	Web Bot -> Barack Obama -> Tax credit -> Tax holiday

Tips:
 - Any path can do but shorter will probably be easier
 - Run time can be long for unconnected pages
 - Feel free to use any python packages
 - Start with a closely connected pages
 - Normalizing page names and URL's is very helpful

Good luck!

## How it works

The program will start an initial search for a source website url, expressed in two word keywords, and a destination that is expressed in two word keywords.

The program will try to find relevancy first to the keywords where the source destination is. Otherwise, the program will begin to recursively unpack more links 

from its own links and the links within the links. How many times it will try to find relevancy can be specified. Relevant links will be added to a list which then will begin

the search. When relevancy is found, the program will begin to recursively go down "rabbit holes" until it can no longer find any more relevancy and then the program 

determines it is on a "wild goose chase". The program will then drop those links and keep repeatedly going down rabbit holes until it finds all the rabbits or it has dropped 

all of the links.