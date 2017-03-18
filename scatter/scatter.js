


//calculate dimensions of svg
var margin = {top: 40, right: 140, bottom: 60, left: 40},
//width = 1860 - margin.left - margin.right,
//height = 800 - margin.top - margin.bottom;
width = 500;
height = 500;

chart_data = [];
keys = [];


// create x scale, it doesn't have its endpoints yet (the domain will come from the input data)
var x = d3.scale.linear()
    .range([0, width]);

var y = d3.scale.linear()
    .range([height, 0]);

//set up the axis functions, to be called on svg groups 
var xAxis = d3.svg.axis()
    .ticks(6)
    .scale(x)
    .tickSize(-height)
    .tickSize(4)
    .orient("botton");

var yAxis = d3.svg.axis()
    .ticks(6)
    .scale(y)
    //.ticks(6)
    .tickSize(-width)
    .tickSize(4)
    .orient("right")
    ;

x_var = document.querySelector("#x-axis-select").value;
y_var = document.querySelector("#y-axis-select").value;


//make the actual svg, sizing it, and then add a group, which will act as our main selection.  the group has been translated (moved) to the origin plus the margin
var svg = d3.select("body").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

//svg clip paths?  I need to look into this.  
// it seems like it can keep the chart from overflowing
//  into what should be the margins
svg.append("clipPath")
    .attr("id", "clip")
  .append("rect")
    .attr("width", width)
    .attr("height", height);



d3.json("team_stats.json", function(err, data) {
	if (err) throw err;
	chart_data = data;
	console.dir(chart_data[0]);
	console.log(Object.keys(chart_data[0]));

	x.domain([d3.min(chart_data, function(d) { return d[x_var]; }), d3.max(chart_data, function(d) { return d[x_var]; })]).nice();
	y.domain([d3.min(chart_data, function(d) { return d[y_var]; }), d3.max(chart_data, function(d) { return d[y_var]; })]).nice();

	//svg
	  //.datum(data)// TA DA!!! Here we bind the data to the main svg group (g)
	  //.on("click", click);

	function circleHover(d) {
		var mouse_coords = d3.mouse(this);
		console.log(mouse_coords)
		d3.select(this).style("stroke","red");
		var hoverInfo = document.querySelector(".hover-info")
		hoverInfo.innerHTML = d.TEAM_NAME;
		hoverInfo.style.top = mouse_coords[1]+margin.top+"px";
		hoverInfo.style.left = mouse_coords[0]+margin.left+"px";


	}
	function circleUnhover(d) {
		d3.select(this).style("stroke","#222");
	}


	circles = svg.selectAll("circle").data(chart_data);
	circles.enter().append("circle")
     .attr("cx",function(d,i){return(x(d[x_var]))})
     .attr("cy",function(d,i){return(y(d[y_var]))})
     .attr("r",function(d,i){return(10)})
     .style("fill","none").style("stroke",function(d,i){return("#222");}).style("stroke-width",2)
     .on("mouseover", circleHover)
     .on("mouseleave", circleUnhover);
    circles.exit().remove();



	// add the y axis
	svg.append("g")
	  .attr("class", "y axis")
	  .attr("transform", "translate(" + width + ",0)")
	  .call(yAxis)
	  .append("text")
	  .attr("class", "y-label")
	  .attr("x", height/2)
	  .attr("y", -50)
	  .style("text-anchor", "end")
	  .style("color", "white")
	  .style("transform","rotate(90deg)")
	  .text(y_var);


	//add the x axis
	svg.append("g")
	  .attr("class", "x axis")
	  .attr("transform", "translate(0," + height + ")")
	  .call(xAxis)
	  .append("text")
	  .attr("class", "x-label")
	  .attr("x", width/2)
	  .attr("y", 40 )
	  .style("text-anchor", "end")
	  .style("color", "white")
	  .text(x_var);
	  
/*
	svg.append("text")
	  .attr("class", "x-label")
	  .attr("x", width /2)
	  .attr("y", height+30 )
	  .style("text-anchor", "end")
	  .style("color", "white")
	  .text(x_var);

	svg.append("text")
	  .attr("class", "y-label")
	  .attr("x", width+60)
	  .attr("y", height/2 )
	  .style("text-anchor", "end")
	  .style("color", "white")
	  .text(y_var);
*/


	// On click, update the x-axis.
	// the transition selection call/attr usage is interesting here, after setting the scale domain
	function adjustChart() {
		x_var = document.querySelector("#x-axis-select").value;
		y_var = document.querySelector("#y-axis-select").value;

		x.domain([d3.min(chart_data, function(d) { return d[x_var]; }), d3.max(chart_data, function(d) { return d[x_var]; })]).nice();
		y.domain([d3.min(chart_data, function(d) { return d[y_var]; }), d3.max(chart_data, function(d) { return d[y_var]; })]).nice();

		svg.select(".y-label")
			.text(y_var);
		svg.select(".x-label")
			.text(x_var)

		svg.select(".y.axis")
		  .call(yAxis);

		svg.select(".x.axis")
		  .call(xAxis);


		var t = circles.transition().duration(750);
		t
		 .attr("cx",function(d,i){return(x(d[x_var]))})
		 .attr("cy",function(d,i){return(y(d[y_var]))})
		 .attr("r",function(d,i){return(10)})
		 .style("fill","none").style("stroke",function(d,i){return("#222");}).style("stroke-width",2)
	}

	adjustChart();

	document.querySelector("#x-axis-select").onchange=adjustChart;
	document.querySelector("#y-axis-select").onchange=adjustChart;


});





