// Load the Visualization API and the piechart package.
google.charts.load('current', {packages: ['corechart']});
// Set a callback to run when the Google Visualization API is loaded.;
google.charts.setOnLoadCallback(drawChart);



function reformatData(jsonData){
    var temp= jsonData.Dashboard;
    console.log("temp: " + JSON.stringify(temp));
    var result = [];
    var i;
    var row;
    for (i=0; i < temp.length; ++i){
        row= temp[i]
        dataElement = [];
        dataElement.push(row.id + '-' + row.name);
        dataElement.push(row.count);
        result.push(dataElement);
    }
    console.log("Data: " + JSON.stringify(result));
    return result;
}

function drawChart() {
    var jsonData = $.ajax({
        url: "http://localhost:5000/SocialMessagingApp/dashboard",
        dataType: "json",
        async: false
    }).responseText;

    console.log("jsonData: " + JSON.parse(jsonData));

    // Create our data table out of JSON data loaded from server.
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Trend User');
    data.addColumn('number', 'Message number');
    data.addColumn('string', 'Date')
    console.log((reformatData(JSON.parse(jsonData))))
    data.addRows(reformatData(JSON.parse(jsonData)));

    var options = {
        title: 'Stock Parts by Id/name',
        chartArea: {width: '50%'},
        hAxis: {
            title: 'Total Number',
            minValue: 0
        },
        vAxis: {
            title: 'Trend User'
        }
    };

    var chart = new google.visualization.BarChart(document.getElementById('chart_div'));

    chart.draw(data, options);

}

google.charts.load('current', {packages: ['corechart', 'bar']});
google.charts.setOnLoadCallback(drawChart);