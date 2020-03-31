$(document).ready(function(){
    $('.search-button').mouseenter(function(){
        $(this).css("color","#007bff");
    });
   
    $('.search-button').mouseleave(function(){
        $(this).css("color","black");
    });
    
    $('.search-button').click(function(){
        // AJAX
        var selection = $('#search-selection').val();
        var query = $('#query').val();
        console.log(selection);
        console.log(query);

        // CSRF FAILS WHILE POST METHOD

        // var csrfmiddlewaretoken = $('input[name="csrfmiddlewaretoken"]').val();
        // // var url = $('#user-forms').attr('action');
        // var xml = new XMLHttpRequest();
        // xml.onreadystatechange = function(){
        //     if(this.readyState==4&&this.status==200){   
        //         document.getElementById("render").innerHTML = this.responseText;
        //     }
        // }
        // xml.open("POST",'/drinkslist/',true);
        // xml.send('query',query);
        // xml.send('search-selection',selection);
        // xml.send('csrfmiddlewaretoken',csrfmiddlewaretoken);
        // xml.send();

        $.ajax({
            url: '/drinkslist/search/',
            type: 'POST',
            dataType: 'JSON',
            data: {'search-selection': selection, 'query': query, 'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()},
            success: function (data) {
                if($('#dialog').css("display")=="none"){
                    $('#dialog').show();
                }
                
                var raw;
                if (data.length>0){
                    // css still needed to be done
                    for(var i=0;i<data.length;i++){
                        var obj = data[i];
                        var title = data[i]['title'];
                        var link = data[i]['link'];
                        var summary = data[i]['summary'];
                        raw = $('#search-result').html();
                        raw = raw + '<li class="list-group-item"><a style="color:#007bff" class="list-group-item list-group-item-action" href='+ link+' >'+title+'</a>' +' <br />'+''+ summary + '</li><br/>'
                        $('#search-result').html(raw);
                        console.log(raw);
                    };
                    // sorting all the results
                    $('#search-result').html(raw);
                    console.log(data);
                }else{
                    // No results found
                    $('#search-result').html('<li class="list-group-item">'+'No results found, searching for '+'<strong style="color:#007bff">'+query+'</strong>'+" in Google?</li>");
                }
            },
            failure: function(data){
                alert('No Result Found' + data);
            }
        })
    });

    $('#exit_btn').click(function(){
        $('#dialog').hide();
        // clean the searching results, avoiding repertability
        var raw;
        $('#search-result').empty();
    });

});

// click other div will close the popup window, not done

// $(document).bind("click",function(){
//     if($('#dialog').css('display')!="none"){
//         $('#dialog').mousedown(function(){
//             $(this).hide();
//         });
//     }
// });
