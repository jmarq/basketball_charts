# this code is obsolete, because the page it scrapes has changed its structure
#  now the list of games is split up onto multiple pages by month

import urllib
from bs4 import BeautifulSoup as bs
import json

# this url only contains games from October now
url="http://www.basketball-reference.com/leagues/NBA_2013_games.html"
site=urllib.urlopen(url);
content=site.read();
site.close();
soup=bs(content);
gamesTable=soup.find(id="games");
gamesRows=gamesTable.findAll('tr');

results={};


#home team name is row[4] away is [2], points follow name
for i in range(1,len(gamesRows)):
	tds=gamesRows[i].findAll('td');
	if(tds[1].text !="Box Score"):
		break;
	awayName=tds[2].text;
	homeName=tds[4].text;
	if( int(tds[5].text) > int (tds[3].text) ):
	    winningName=homeName;
	    losingName=awayName;
	else:
	    winningName=awayName;
	    losingName=homeName;
	print winningName+" won and "+losingName+" lost\n";
	if(winningName in results.keys()):
	    prev=results[winningName][len(results[winningName])-1];
	    results[winningName].append(prev+1);
	else:
	    results[winningName]=[0,1];
	if(losingName in results.keys()):
	    prev=results[losingName][len(results[losingName])-1];
	    results[losingName].append(prev-1);
	else:
	    results[losingName]=[0,-1];

#print results;		
resultJSON=json.dumps(results);
fi=open("leagueResults.json",'w');
fi.write(resultJSON);
fi.close();
		
	
	
	