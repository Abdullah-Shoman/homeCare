function isNumber(evt) {
    evt = (evt) ? evt : window.event;
    var charCode = (evt.which) ? evt.which : evt.keyCode;
    if (charCode > 31 && (charCode < 48 || charCode > 57)) {
        return false;
    }
    return true;
}

// $(document).ready(function(){
//     $('form').submit(function(e){
//         e.preventDefault()
//         console.log('hi')
//         $.ajax({
//             url: '/reg',
//             method: 'post',
//             data: $('#form').serialize(),
//             success: function(data){
//                 $('.error').html("data");
                
//             },
//             error: function(data){
//                 // console.log('hi2')
//                 // alert(data.responseJSON);
            
//             }
//         })
        
//     })
// });

