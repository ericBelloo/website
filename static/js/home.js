
$(document).ready(function(){
    $('#about_me').hide();
});

$('#btn_about').click(function(){
    if ($('#about_me').is(':visible')) {
        $('#about_me').hide();
    } else {
        $('#about_me').show();
    }
});

/*
    Show the upload documents
*/
$(document).change(function(evt){
    let name_id = evt.target.id;
    files = evt.target.files;
    switch( name_id){
        case 'id_first_dep':
        AppendDocument('#id_first_documents', files);
        break;
        case 'id_second_dep':
            AppendDocument('#id_second_documents', files);
        break;
        case 'id_third_dep':
            AppendDocument('#id_third_documents', files);
        break;
        case 'id_final_project':
            AppendDocument('#id_final_project', files);
        break;
    }
});

function AppendDocument(container, files){

    for (let i = 0, f; f = files[i]; i++) {
        let reader = new FileReader();
        reader.onload = function() {
            $(container).append('<div class="document"><img src="static/img/word.svg"><span>' + files[i].name + '</span></div>');
        }
    reader.readAsDataURL(f);
    }
}

/*
    Send form
*/
$(document).click(function(evt){
    let element = evt.target.id;
    switch(element){
        case 'btn_first':
            console.log('first');
            SendForm($('#form_first'));
        break;
        case 'btn_second':
            console.log('second');
            SendForm($('#form_second'));
        break;
        case 'btn_third':
            console.log('third');
            SendForm($('#form_third'));
        break;
        case 'btn_project':
            console.log('project');
            SendForm($('#form_project'));
        break;
    }
});

function SendForm(form){
    request = $.ajax({
        url: form.attr('action'),
        type: form.attr('method'),
        data: new FormData($(form)[0]),
        dataType: 'json',
        contentType: false,
        processData: false,
    });
    request.done(function(data){
        console.log('success');
    });
    request.fail(function(jqXHR, textStatus){
        //$('#id_message').addClass('msg-error');
        //$('#id_message_text').html(message);
        console.log(textStatus)
    });
};
