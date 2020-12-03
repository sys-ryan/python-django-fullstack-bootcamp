$('h1').click(function(){
    $(this).text("I was changed")
})

$('li').click(function(){
    console.log('any li was clicked')
})


//Key Press
$('input').eq(0).keypress(function(){
    $('h3').toggleClass('turnBlue')
})

$('input').eq(0).keypress(function(event){
    console.log(event)
    if(event.which === 13){ //enter key
        $('h3').toggleClass('turnRed')

    }
})



//on() 
$('h1').on('mouseenter', function(){
    $(this).toggleClass('turnBlue')
})


//effects
$('input').eq(1).on('click', function(){
    //$('.container').fadeOut(3000)
    $('.container').slideUp(3000)
})
