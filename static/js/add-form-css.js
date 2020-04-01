$(document).ready(function(){

    // dynamicly adding css to the django form ,avoiding changing the template tags
    var input_sets =  $('#user_form').find("input");
    var error_helper = $('#user_form').find("ul");
    
    var helper = $('.helptext');
    helper.hide();
    var parent_form = $('#user_form');
    helper.css("color","#007bff");

    for (var i=0;i<error_helper.length;i++){
        $(error_helper).css("color","#007bff");
    }
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

    
    $('#check_btn').on({
        "click":function(){
            if($('.helptext').hide()){
                $('.helptext').show();
            }
            if($(error_helper).hide()){
                $(error_helper).show();
            }
        }
    })

    $('.custom-file-input').on('change',function(){ 
        let fileName = $(this).val().split('\\').pop(); 
        $('.custom-file-label').addClass("selected").html(fileName); 
    });
   

});


