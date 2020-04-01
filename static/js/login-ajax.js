$(document).ready(function(){
    
    // initialise
    $("#modal_title").text("Processing Ajax");
    $(".modal-body").text("");

    function popUp(title,body){
        $('#check').attr("class","jumbotron");
        $('#active_btn').click();
        $("#modal_title").text(title);
        $(".modal-body").text(body);
    }

    function check(){
        var name = $("#id_username").val();
        var pass = $("#id_password").val();
        var url = $("#login_btn").val();
        console.log(name,pass);
        // request check_login routing, sending the user input
        $.ajax({
            url: url,
            type: 'POST',
            data: {'username': name, 'password': pass, 'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()},
            success: function (data) {
                console.log(data);
                // alert(data);
                if(data==="Invalid login details supplied" || data==="Your Drinkslist account is disabled."){
                    var title = "Error";
                    console.log(title)
                    popUp(title,data);
                }else{
                    var title = "Result";
                    var body = "Login successfully! Automatically redirect to the Homepage after 2s."
                    popUp(title,body);
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

    $("#login_btn").click(function(){
        check();
    });



});