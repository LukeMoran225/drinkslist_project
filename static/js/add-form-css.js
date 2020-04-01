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

    $('.helptext').hide();
    $('.helptext').css("color","#007bff");
    $('#id_username').on({
        focus:function(){
            if($('.helptext').hide()){
                $('.helptext').show();
            }
        }
    })

});