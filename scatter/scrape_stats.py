# stats from http://stats.nba.com/stats/leaguedashteamstats?Conference=&DateFrom=&DateTo=&Division=&GameScope=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2016-17&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=

# who knows how long that ^^^ url will be valid, but we can use it for now

# this file will create a json file
import requests
import json

HEADERS = {
    'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) '
                   'AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/45.0.2454.101 Safari/537.36'),
}

url="http://stats.nba.com/stats/leaguedashteamstats?Conference=&DateFrom=&DateTo=&Division=&GameScope=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2016-17&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision="

response = requests.get(url, headers=HEADERS)

print response.status_code
if response.status_code == 200:
	print "success!"
	stats = json.loads(response.text)
	result_set = stats['resultSets'][0]
	stat_headers = result_set['headers']
	# print stat_headers
	atlanta_row = result_set['rowSet'][0]
	# print atlanta_row
	team_dicts = []
	for team_row in result_set['rowSet']:
		team_dict = {}
		for i in range(0,len(team_row)):
			team_dict[stat_headers[i]] = team_row[i]
		# print team_dict
		team_dicts.append(team_dict)

	print team_dicts[-1]

team_dicts_json = json.dumps(team_dicts)

outfile = open("team_stats.json","w")
outfile.write(team_dicts_json)
outfile.close()




