$(document).ready(function(){
    $('.search-button').mouseenter(function(){
        $(this).css("color","blue");
    });
   
    $('.search-button').mouseleave(function(){
        $(this).css("color","black");
    });
    
    $('.search-button').click(function(){
        // // AJAX
        var selection = $('#search-selection').val();
        var query = $('#query').val();
        console.log(selection);
        console.log(query);
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
                        raw = raw + '<a href='+ link+' >'+title+'</a>' +' <br />'+ summary + '<br/>'
                        $('#search-result').html(raw);
                        console.log(raw);
                    };

                    // sorting all the results
                    $('#search-result').html(raw);
                    console.log(data);
                }else{
                    // No results found
                    $('#search-result').html("No result found, try searching for "+'<strong style="color:#007bff">'+query+'</strong>'+" in Google");
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

