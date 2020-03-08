
// open the selected homework
$('.btn-about').on('click', function(){
    $('.about').removeClass('dn');
});

$('.btn-close').on('click', function(){
    $('.about').addClass('dn');
});

$('#id_search_document').on('keyup', function(){

    var value = $(this).val() == '' ? 'none' : $(this).val();

    let request = $.ajax({
        url: '/get_document_list/' + value + '/',
        type: 'GET',
        data: {},
    });
    request.done(function(data){
        $('#id_content_document').empty();
        object_list = data.list
        if (object_list.length == 0){
            $('#id_content_document').html('<span class="notification">The document with that name does not exist</span>');
        }else{
            object_list.forEach(element => $('#id_content_document').append('<a href="/homework/'+ element.id +'"><span class="content_element">'+ element.title +'</span></a><div class="line"></div>'));
        }
    });
    request.fail(function(jqXHR, textStatus){
        console.log(textStatus);
    });

});