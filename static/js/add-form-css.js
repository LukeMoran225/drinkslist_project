$(document).ready(function(){
// dynamicly adding css to the django form ,avoiding changing the template tags
    var input_sets =  $('#user_form').find("input");
    for (var i=0;i<input_sets.length;i++){
        var each = input_sets[i];
        var type = $(each).attr('type');
        var pa = $(each).parent();
        var la = $(each).prev();
        if(type=="file"){
            pa.attr("class","custom-file");
            la.attr("class","custom-file-label");
            each.className = "custom-file-input";
        }else if(type=="checkbox"){
            
        }else{
            each.className = "form-control";
        }
    };

    var helper = $('.helptext');
    var parent_form = $('#user_form');
    // if(parent_form.attr("class","form-control animated fadeIn")){
        // parent_form.attr("class","form-control");
    // }
    helper.hide();
    helper.css("color","#007bff");
    $('#id_username').on({
        "focus":function(){
            if($('.helptext').hide()){
                $('.helptext').show();
                parent_form.attr("class","form-control animated fadeIn");
            }
        }
    })

    // if($('.search-button')!= undefined){
    //     var check = $('#container').attr("class","jumbotron");
    //     $('.input-group-prepend').attr("class","input-group-prepend animated fadeIn");
    // }
    

});

// $(document).mousemove(function(){
//     var parent_form = $('#user_form');
//     var timeout=setTimeout(function () {
//         if(parent_form.attr("class","form-control animated fadeIn")){
//             parent_form.attr("class","form-control");
//         }
//     }, 1200);
// });