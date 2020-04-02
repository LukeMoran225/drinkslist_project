/* 

call the XHR object to profile view - POST

*/

$(document).ready(function(){

    function popUp(title,body){
        $('#check-b').attr("class","jumbotron");
        $('#active_btn').click();
        $("#modal_title").text(title);
        $(".modal-body").text(body);
    };

    function send(username,url,is_pro,pic){
        $.ajax({
            url: url,
            type: 'POST',
            async: false,
            data: {'username': username,'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),'is_professional':is_pro,'picture':pic},
            success: function(data){
                alert(data);
                window.location.replace(url);
                // document.documentElement.innerHTML = data;
            },
            failure: function(data){
                alert('Invalid Access' + data);
            }
        });
    }

    var is_pro;

    $("#up-btn").click(function(){
        // Double check
        var username = $("#up-btn").val();
        var url = $("#up-btn").attr("data");
        // var is_pro = $("#id_is_professional").val();
        var pic = $("#id_picture").attr("src");
        
        // send(id,url);
        console.log(username,url,is_pro,pic);
        send(username,url,is_pro,pic);
    });


    $("input[type='checkbox']").click(function(){
        if ($(this).is(":checked"))
        {
            is_pro = true; 
        }else{
            is_pro = false; 
        };
    });


    
});