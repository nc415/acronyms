function make_chart(group, data) {
  var $div = $('<div class="event-statistic" />')
  if (data.length !== 0) {
    $div.highcharts({
      chart: {
        type: 'pie'
      },
      credits: { enabled: false },

      title: { text: "By " + group },
      series: [{ innerSize: '60%',
        name: 'Number of attendees',
      data: data}],
      exporting: {
        enabled: false
      },
      plotOptions: {
        pie: {
          dataLabels: {
            distance: 5,
          },
        }
      },
    });
    $('#attendance_statistics').append($div);
  }
}
