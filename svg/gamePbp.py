from bs4 import BeautifulSoup as bs
import urllib


def has4td(row):
	n=len(row.findAll("td"));
	return(n==4);
	
def getScoringString(row,team):
	b="";
	if(team=="ill"):
		b=row.findAll('td')[3].findAll('b');
		
	elif(team=="ind"):
		b=row.findAll('td')[1].findAll('b');
		
	return(b[0].text);

def getTimeString(row):
	return(row.findAll('td')[0].text);

def halfElapsed(timeString):
	splitto=timeString.split(":");
	minsLeft=int(splitto[0]);
	secsLeft=int(splitto[1]);
	secsLeft=secsLeft+(minsLeft*60);
	elapsed=(20*60)-secsLeft;
	return(elapsed);
	
def processTimes(teamList, team):
	#will return a list of scoring strings and seconds elapsed since beginning of game.
	processed=[];
	baseTime=0;
	prevTime=0;
	for row in teamList:
		stringo=getScoringString(row,team);
		elapsed=halfElapsed(getTimeString(row))+baseTime;
		if(elapsed<prevTime):
			baseTime+=(20*60);
			elapsed+=baseTime;
		prevTime=elapsed;
		processed.append({"play":stringo,"gameSeconds":elapsed});
	return(processed);
	
		
		
		
	
	
	

url="http://scores.espn.go.com/ncb/playbyplay?gameId=330380356";
page=urllib.urlopen(url);
data=page.read();
page.close();
#print data;
soup=bs(data);
pbp=soup.findAll("table",{"class":"mod-data mod-pbp"});
#print pbp;
rows=pbp[0].findAll("tr");
#for row in rows:
#	print has4td(row);
#	print "\n";
fours=[];
for i in range(0,len(rows)):
	if(has4td(rows[i])):
		fours.append(rows[i]);
#print fours;
illinoisScores=[];
indianaScores=[];
for row in fours:
	if(row.findAll("td")[1].findAll('b')):
		indianaScores.append(row);
	elif(row.findAll("td")[3].findAll('b')):
		illinoisScores.append(row);
#print illinoisScores;
pt={"ill":processTimes(illinoisScores,"ill"),"ind":processTimes(indianaScores,"ind")};

print pt['ind'];
#now we have a list of rows for each team.  Each row with 4 tds each. 
#td[0] is time.  if time ever drops from row to row, a new half has started! this will fail if a team goes 20 mins without scoring
#illinois's scoring description is in td[3], indiana's in td[1]
#assisters are shown after periods.  split the scoring description by periods and take the first half. 

		


