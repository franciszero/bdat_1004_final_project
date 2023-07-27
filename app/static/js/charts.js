google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {
    var data = google.visualization.arrayToDataTable([
        ['Date', 'Temperature'],
        {% for city_weather in city_weathers %}
        ['{{ city_weather.date }}', {{ city_weather.temperature }}],
        {% endfor %}
    ]);

    var options = {
        title: 'City Weather',
        curveType: 'function',
        legend: { position: 'bottom' }
    };

    var chart = new google.visualization.LineChart(document.getElementById('chart_div'));

    chart.draw(data, options);
}
