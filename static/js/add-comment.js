// /* 

// call the XHR object to add_comment view - POST

// */

// $(document).ready(function(){

//     function popUp(title,body){
//         $('#check-b').attr("class","jumbotron");
//         $('#active_btn').click();
//         $("#modal_title").text(title);
//         $(".modal-body").text(body);
//     };

//     $("#cm-btn").click(function(){
//         var comment = $("#cm").val();
//         var for_recipe = $("#user_form").attr("recipe");
//         var url = $("#cm-btn").attr("data");
//         console.log(url);
//         $.ajax({
//             url: '.',
//             type: 'POST',
//             async: true,
//             data: {'for_recipe':for_recipe ,'comment':comment,'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()},
//             success: function(data){
//                 alert("Update Successfully!");
//             },
//             failure: function(data){
//                 alert('Invalid Access' + data);
//             }
//         });
//     });

    
// });