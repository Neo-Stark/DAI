$( document ).ready(function() {
  $( "button#day-night" ).click(function( event ) {
    event.preventDefault();
    $( "*" ).toggleClass( "night" )
    $("nav").toggleClass("navbar-light")
    $("nav").toggleClass("bg-light")
    $("nav").toggleClass("navbar-dark")
    $("nav").toggleClass("bg-dark")
  });
  $("button#navbar").click(function(event ) {
    $(this).empty()
    if ($("nav").css("display") == "none"){
      $(this).append("<i class='far fa-eye-slash'></i>Ocultar Navbar")
      $("nav").show("slow")
    }else{
      $(this).append("<i class='far fa-eye'></i>Mostrar Navbar")
      $("nav").hide("slow")
    }
  });
});