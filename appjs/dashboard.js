//Load the Visualization API and the piechart package.
google.charts.load('current', {packages: ['corechart', 'bar']});
// Set a callback to run when the Google Visualization API is loaded.;
google.charts.setOnLoadCallback(drawChart);
google.charts.setOnLoadCallback(drawChart2);
google.charts.setOnLoadCallback(drawChart3);


dashCtrl = this;

function reformatData(jsonData){
    var temp= jsonData.Dashboard.TrendingHash;
    //console.log("temp: " + JSON.stringify(temp));
    var result = [];
    var i;
    var row;
    for (i=0; i < temp.length; ++i){
        row= temp[i]
        dataElement = [];
        dataElement.push(row.Name);
        dataElement.push(row.Count);
        result.push(dataElement);
    }
    //console.log("Data: " + JSON.stringify(result));
    return result;
}

function reformatData2(jsonData) {
    var temp = jsonData.Dashboard.TrendingUser;
    //console.log("temp: " + JSON.stringify(temp));
    var result = [];
    var i;
    var row;
    for (i = 0; i < temp.length; ++i) {
        row = temp[i]
        dataElement = [];
        dataElement.push(row.Name);
        dataElement.push(row.Count);
        result.push(dataElement);
    }
    //console.log("Data: " + JSON.stringify(result));
    return result;
}

function reformatData3(jsonData) {
    var temp = jsonData.Dashboard;
    console.log("temp: " + JSON.stringify(temp));
    var result = [];
    result.push(["Number O fMessages", temp.NumberOfMessages]);
    result.push(["Number Of Replies", temp.NumberOfReplies]);
    result.push(["Number Of Dislikes", temp.NumberOfDislikes]);
    result.push(["Number Of Likes", temp.NumberOfLikes]);

    console.log("Data: " + JSON.stringify(result));
    return result;
}


function drawChart() {

    var jsonData = $.ajax({
        url: "http://localhost:5000/SocialMessagingApp/dashboard",
        dataType: "json",
        async: false
    }).responseText;



    // Create our data table out of JSON data loaded from server.
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Trend Hashtag');
    data.addColumn('number', 'Message number');
    //data.addColumn('string', 'Date')
    data.addRows(reformatData(JSON.parse(jsonData)));

    var options = {
        title: 'Top 10 Trending Hashtags:',
        chartArea: {width: '50%'},
        hAxis: {
            title: 'Total Number',
            minValue: 0
        },
        vAxis: {
            title: 'Trend User'
        }
    };

    var chart = new google.visualization.PieChart(document.getElementById('chart_div'));
    chart.draw(data, options);
}



function drawChart2() {
    dashCtrl = this;

    var jsonData = $.ajax({
        url: "http://localhost:5000/SocialMessagingApp/dashboard",
        dataType: "json",
        async: false
    }).responseText;



    // Create our data table out of JSON data loaded from server.
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Trend User');
    data.addColumn('number', 'Message number');
    //data.addColumn('string', 'Date')
    data.addRows(reformatData2(JSON.parse(jsonData)));

    var options = {
        title: 'Top 10 Trending Users:',
        chartArea: {width: '50%'},
        hAxis: {
            title: 'Total Number',
            minValue: 0
        },
        vAxis: {
            title: 'Trend User'
        }
    };

    var chart = new google.visualization.PieChart(document.getElementById('chart_div2'));
    chart.draw(data, options);
}



function drawChart3() {
    dashCtrl = this;

    var jsonData = $.ajax({
        url: "http://localhost:5000/SocialMessagingApp/dashboard",
        dataType: "json",
        async: false
    }).responseText;

    console.log("jsonData: " + JSON.parse(jsonData));

    // Create our data table out of JSON data loaded from server.
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Action');
    data.addColumn('number', 'Number Of Actions');
    //data.addColumn('string', 'Date')
    data.addRows(reformatData3(JSON.parse(jsonData)));

    var options = {
        title: 'Actions Statistics:',
        chartArea: {width: '50%'},
        hAxis: {
            title: 'Number of Actions',
            minValue: 0
        },
        vAxis: {
            title: 'Actions'
        }
    };

    var chart = new google.visualization.BarChart(document.getElementById('chart_div3'));
    chart.draw(data, options);

}
