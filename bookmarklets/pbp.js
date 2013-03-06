(function(){



var getScoringPlayer=function(row,team){
	var I;
	if(team=="awayTeam"){
	     I=1;
	}
	else{
		I=5;
	}
	playerID=row.cells[I].getElementsByTagName("a")[0].href.split("/").pop().split(".")[0];
	playerName=row.cells[I].getElementsByTagName("a")[0].innerHTML;
	return({id:playerID,name:playerName})
};

var getPointIncrease=function(row,team){
	var I;
	if(team=="awayTeam"){I=2;}
	else{I=4;}
	pts=parseInt(row.cells[I].innerHTML[1]);
	return(pts);
};


var playTable=$("table.stats_table.no_highlight").last();
var baseTime=-1*12*60;

var getTime=function(row){
	time=row.cells[0].innerHTML.split(":");
	mins=parseInt(time[0]);
	secs=parseFloat(time[1]);
	secs+=mins*60;
	secs=((12*60)-secs)+baseTime;
	return(secs);

};



playTable.find("tr").each(function(){

	if(this.id[0]=="q"){
		if(baseTime<47.9999*60){
		baseTime+=(12*60);
		}
		else{
		baseTime+=(5*60);
		}
	}
	if(this.cells.length==6){
		if(this.cells[2].innerHTML[0]=="+"){
		scoringTeam="awayTeam";
		playerObject=getScoringPlayer(this,scoringTeam);
		alert(playerObject.name);
		}
		else if(this.cells[4].innerHTML[0]=="+"){
		scoringTeam="homeTeam";
		playerObject=getScoringPlayer(this,scoringTeam);
		alert(playerObject.name);
		alert(getTime(this));
		alert(getPointIncrease(this,scoringTeam));
		
		}
	}
	

	

});


})();

