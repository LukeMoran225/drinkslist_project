$(document).ready(function(){
    // several different events - sharing func
    function search(){
        // AJAX
        var selection = $('#search-selection').val();
        var query = $('#query').val();
        console.log(selection);
        console.log(query);
    
        // CSRF FAILS WHILE POST METHOD
    
        // var csrfmiddlewaretoken = $('input[name="csrfmiddlewaretoken"]').val();
        //         document.getElementById("render").innerHTML = this.responseText;
    
        $.ajax({
            url: '/drinkslist/search/',
            type: 'POST',
            dataType: 'JSON',
            data: {'search-selection': selection, 'query': query, 'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()},
            success: function (data) {
                $('#active_btn').click();
                var raw;
                if (data.length>0){
                    // css still needed to be done
                    for(var i=0;i<data.length;i++){
                        var obj = data[i];
                        var title = data[i]['title'];
                        var link = data[i]['link'];
                        var summary = data[i]['summary'];
                        raw = $('.modal-body').html();
                        raw = raw + '<li class="list-group-item"><a style="color:#007bff" class="list-group-item list-group-item-action" href='+ link+' >'+title+'</a>' +' <br />'+''+ summary + '</li><br/>'
                        $('.modal-body').html(raw);
                        console.log(raw);
                    };
                    // sorting all the results
                    $('.modal-title').html('Lightweight Searching Results');
                    $('.modal-body').html(raw);
                    console.log(data);
                }else{
                    // No results found
                    $('.modal-title').html('Lightweight Searching Results');
                    $('.modal-body').html('<li class="list-group-item">'+'No results found, searching for '+'<strong style="color:#007bff">'+query+'</strong>'+" in Google?</li>");
                    $('.gcse-search').show();
                }
            },
            failure: function(data){
                alert('No Result Found' + data);
            }
        })
    }

    // change the fixed placeholder
    var placeholder = $('#query').attr("placeholder");
    $('#query').on({
        click:function(){
            $(this).attr("placeholder"," ");
        },
        blur:function(){
            $(this).attr("placeholder",placeholder);
        },
        keypress:function(event){
            // check whether the text field is empty
            var keycode = (event.keyCode ? event.keyCode : event.which);
            if(keycode == '13'){
                $("#modal_title").text("Processing Ajax");
                $(".modal-body").text("");
                if($(this).val().length<1){
                    // alert("The text field is empty!");
                    // return false;
                    $('#active_btn').click();
                    $("#modal_title").text("Error");
                    $(".modal-body").text("The text field is empty!");
                }else{
                    search();
                }
            }
        }
    });
    
    $('.search-button').on({
        'mouseenter':function(){
            $(this).css("color","#007bff");
        },
        'mouseleave':function(){
            $(this).css("color","black");
        },
        click:function(event){
            $("#modal_title").text("Processing Ajax");
            $(".modal-body").text("");
            // check whether the text field is empty
            if($("#query").val().length<1){
                $('#active_btn').click();
                $("#modal_title").text("Error");
                $(".modal-body").text("The text field is empty!");
            }else{
                search();
            }
        },
    });
    

    $('#exit_btn').click(function(){
        $('#dialog').hide();
        // clean the searching results, avoiding repertability
        var raw;
        $('#search-result').empty();
    });

});

