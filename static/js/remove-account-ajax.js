/* 

call the XHR object to user_delete view

*/

$(document).ready(function(){

    function popUp(title,body){
        $('#check-b').attr("class","jumbotron");
        $('#active_btn').click();
        $("#modal_title").text(title);
        $(".modal-body").text(body);
    };

    function send(id,url){
        $.ajax({
            url: url,
            type: 'POST',
            data: {'id': id,'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()},
            success: function(data){
                console.log(data);
                if(data==="Access Fobbidden"){
                    alert("Error: Access Fobbidden");
                    console.log(title)
                    popUp(title,data);
                }else{
                    alert("Deleted Successfully! Automatically redirect to the Homepage");
                    setTimeout(function(){
                        window.location.replace("/drinkslist/");
                    },2000);
                }
            },
            failure: function(data){
                alert('Invalid Access' + data);
            }
        });
    }

    $("#rm-btn").click(function(){
        // Double check
        var id = $("#rm-btn").val();
        var url = $("#rm-btn").attr("data");
        // send(id,url);
        console.log(id,url);
        var title = "Danger"
        var body = "Are you sure to remove your account?"
        popUp(title,body);
        $("#yes").click(function(){
            send(id,url);
            console.log(id,url);
        });
        
    });



    
});