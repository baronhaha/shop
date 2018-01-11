$(function(){
  $('#myAffix').width($('#right').width());
  $(window).resize(function(){
    $('#myAffix').width($('#right').width());
  });
});