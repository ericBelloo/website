
$('form').on('change keyup keydown paste cut', 'textarea', function () {
        $(this).height(0).height(this.scrollHeight);
}).find('textarea').change();

// Create new text area
$('#add_text').on('click', function(){
    $('form').append('<textarea class="new-content" placeholder="Content"></textarea>');
});

// Search for text areas, get their value and add them to a container
// result <p>Content</p>
$(document).on('click', '#btn_save', function(){
    let content = '';
    $( '.new-content' ).each(function( index ) {
        console.log($(this).type();
    });
    console.log(content);
});

//Send image
$('#id_file').on('change', function(){
    let file = this.files[0];
    let formData = new FormData();
    formData.append('image', file);
    formData.append('csrfmiddlewaretoken', $('input[name="csrfmiddlewaretoken"]').val());
    let request = $.ajax({
        url: $(this).data('url'),
        type: "POST",
		data: formData,
		processData: false,
		contentType: false,
    });
    request.done(function(data){
        $('form').append('<img src="' + data.url + '" class="new-content" alt ="' + data.name +' ">');
    });
    request.fail(function(data){
        console.log('fail');
    });
});