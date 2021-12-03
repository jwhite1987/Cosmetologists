$(function() {
    "use strict";

     // chart 1

		  var ctx = document.getElementById('chart1').getContext('2d');
			d3.csv('data/north_carolina.csv').then(d => {
			    var city = d.map(a=>a['City']);
			    // var countries = d.map(a=>a['country', 'Average Points']);
			    // var points = d.map(a=>a['Average Points']);
			    // var price = d.map(a=>a['Average Price']);
			    // var trees = [continents, countries, price];
			    console.log(city)
					var count = {};
				  d.map(a => a.City).forEach(function(i) { count[i] = (count[i]||0) + 1;});
					console.log(count)
			var myChart = new Chart(ctx, {
				type: 'line',
				data: {
					labels: city,
					datasets: [{
						label: 'New Visitor',
						data: count,
						backgroundColor: '#fff',
						borderColor: "transparent",
						pointRadius :"0",
						borderWidth: 3
					}]
				},
			options: {
				maintainAspectRatio: false,
				legend: {
				  display: false,
				  labels: {
					fontColor: '#ddd',
					boxWidth:40
				  }
				},
				tooltips: {
				  displayColors:false
				},
			  scales: {
				  xAxes: [{
					ticks: {
						beginAtZero:true,
						fontColor: '#ddd'
					},
					gridLines: {
					  display: true ,
					  color: "rgba(221, 221, 221, 0.08)"
					},
				  }],
				   yAxes: [{
					ticks: {
						beginAtZero:true,
						fontColor: '#ddd'
					},
					gridLines: {
					  display: true ,
					  color: "rgba(221, 221, 221, 0.08)"
					},
				  }]
				 }

			 }
			})
		});
	})


    // chart 2
	 //
		// var ctx = document.getElementById("chart2").getContext('2d');
		// 	var myChart = new Chart(ctx, {
		// 		type: 'doughnut',
		// 		data: {
		// 			labels: ["Direct", "Affiliate", "E-mail", "Other"],
		// 			datasets: [{
		// 				backgroundColor: [
		// 					"#ffffff",
		// 					"rgba(255, 255, 255, 0.70)",
		// 					"rgba(255, 255, 255, 0.50)",
		// 					"rgba(255, 255, 255, 0.20)"
		// 				],
		// 				data: [5856, 2602, 1802, 1105],
		// 				borderWidth: [0, 0, 0, 0]
		// 			}]
		// 		},
		// 	options: {
		// 		maintainAspectRatio: false,
		// 	   legend: {
		// 		 position :"bottom",
		// 		 display: false,
		// 		    labels: {
		// 			  fontColor: '#ddd',
		// 			  boxWidth:15
		// 		   }
		// 		}
		// 		,
		// 		tooltips: {
		// 		  displayColors:false
		// 		}
		// 	   }
		// 	});
		// 	});
	 //
	 //
	 //
	 //
   // });
