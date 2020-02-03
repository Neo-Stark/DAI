function pie_chart(data, title){
  Highcharts.chart("grafico", {
    chart: {
      plotBackgroundColor: null,
      plotBorderWidth: null,
      plotShadow: false,
      type: "pie"
    },
    title: {
      text: title
    },
    tooltip: {
      pointFormat: "{series.name}: <b>{point.y}</b>"
    },
    plotOptions: {
      pie: {
        allowPointSelect: true,
        cursor: "pointer",
        dataLabels: {
          enabled: true,
          format: "<b>{point.name}</b>: {point.y} Músicos"
        }
      }
    },
    series: [
      {
        name: "Número",
        colorByPoint: true,
        data: data
      }
    ]
  });
}



function grupos_musicos() {
  $.ajax({
    type: "get",
    url: "/p6/get_grupos_musicos",
    dataType: "json",
    success: function(response) {
      var data = [];
      for (var grupo in response) {
        data.push({
          name: response[grupo]["grupo__nombre"],
          y: response[grupo]["grupo__count"]
        });
      }
      var title = "Número de músicos por grupo"
      pie_chart(data, title);
    }
  });
}
function year_musicos() {
  $.ajax({
    type: "get",
    url: "/p6/get_musicos_year",
    dataType: "json",
    success: function(response) {
      var data = [];
      for (var year in response) {
        data.push({
          name: response[year]["fecha_nacimiento__year"],
          y: response[year]["fecha_nacimiento__year__count"]
        });
      }
      var title = "Número de músicos por año"
      pie_chart(data, title);
    }
  });
}

document.addEventListener("DOMContentLoaded", () => {
  grupos_musicos();
  $("#grupos").click(function(e) {
    e.preventDefault();
    grupos_musicos();
  });
  $("#year").click(function (e) { 
    e.preventDefault();
    year_musicos();
  });
});
