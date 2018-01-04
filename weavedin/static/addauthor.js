$('input').focus(function(){
  $(this).parents('.fgroup').addClass('focused');
});

$('input').blur(function(){
  var inputValue = $(this).val();
  if ( inputValue == "" ) {
    $(this).removeClass('filled');
    $(this).parents('.fgroup').removeClass('focused');  
  } else {
    $(this).addClass('filled');
  }
})  