
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
$(document).click()

