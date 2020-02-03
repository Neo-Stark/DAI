$(document).on("click", ".paginationGrupos a", function(e) {
  e.preventDefault();
  var pageGrupos = $(this)
    .attr("href")
    .split("pageGrupos=")[1];
  console.log(pageGrupos);
  var route = "http://localhost:8000/p6";
  $.ajax({
    type: "GET",
    url: route,
    data: { pageGrupos: pageGrupos },
    dataType: "json",
    success: function(response) {
      $(".Grupos").html(response);
    }
  });
});
