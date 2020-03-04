
$(document).ready(function(){
    console.log('here');
    let request = $.ajax({
        url: $('section').data('url'),
        type:'GET',
        data: {'id_document': $('section').attr('id') }
    });
    request.done(function(data){
        $('section').append(data.html);
    });
    request.fail(function(jqXHR, textStatus){
        console.log(textStatus);
    });
});
