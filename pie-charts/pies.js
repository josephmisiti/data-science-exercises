var SOCIALQ = {}
SOCIALQ.models = {}

SOCIALQ.models.pieChart = function() {
	
	
	var innerRadius = 100;
	var outerRadius = 200;
	var color = d3.scale.category20();
    var donut = d3.layout.pie().value(function(d){ return d.value });
    var arc = d3.svg.arc().outerRadius(outerRadius);
	
	function chart(selection) {
    	selection.each(function(data) {
			
			//data = [ 10, 20, 30, 40 ]
			
			var container = d3.select(this);
			var pie_wrapper = container.selectAll('g.pie-wrapper')
							.data([data])
							.enter()
							.append('g')
							.attr('class','pie-wrapper');
							
			var legend_wrapper = container.selectAll('g.legend-wrapper')
							.data([data])
							.enter()
							.append('g')
							.attr('class','legend-wrapper');							
			

			var arcs = pie_wrapper.selectAll('g.arc')
								  .data(donut)
								  .enter().append('g')
								  .attr('class','arc')
								  .attr("transform", "translate(" + outerRadius + "," + outerRadius + ")");
								
								
			arcs.append("path")
			    .attr("fill", function(d, i) { return color(i); })
			    .attr("d", arc);


			
		});
	}
	
	return chart;
}
