(function($){
  $(function(){

    $('.sidenav').sidenav();
    $('.parallax').parallax();

  });
})(jQuery);

  $(document).ready(function () {
    $('.dropdown-button').dropdown({
      constrainWidth: false,
      hover: true,
      belowOrigin: true,
      alignment: 'left'
    });

     $('.carousel').carousel({indicators: true});
  });

   $('.moveNextCarousel').click(function(e){
      e.preventDefault();
      e.stopPropagation();
      $('.carousel').carousel('next');
   });

   $('.movePrevCarousel').click(function(e){
      e.preventDefault();
      e.stopPropagation();
      $('.carousel').carousel('prev');
   });

   document.addEventListener('DOMContentLoaded', function() {
var elems = document.querySelectorAll('select');
var instances = M.FormSelect.init(elems, options);
});

$(document).ready(function(){
$('select').formSelect();
});

       document.addEventListener('DOMContentLoaded', function() {
         var elems = document.querySelectorAll('.datepicker');
         var instances = M.Datepicker.init(elems, options);
       });

       $(document).ready(function(){
         $('.datepicker').datepicker({
           showClearBtn: true
         });
       });

       document.addEventListener('DOMContentLoaded', function() {
         var elems = document.querySelectorAll('.modal');
         var instances = M.Modal.init(elems, options);
       });

       $(document).ready(function(){
         $('.modal').modal();
       });
           $(document).ready(function () {
             $('.dropdown-button').dropdown({
               constrainWidth: false,
               hover: true,
               belowOrigin: true,
               alignment: 'left'
             });

             $('.slider').slider({
               indicators: true,
               height: 400,
               transition: 500,
               interval: 6000
             });
           });

           document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.materialboxed');
    var instances = M.Materialbox.init(elems, options);
  });


  $(document).ready(function(){
    $('.materialboxed').materialbox();
  });

  $(document).ready(function() {
    $('input#input_text, textarea#textarea2').characterCounter();
  });
