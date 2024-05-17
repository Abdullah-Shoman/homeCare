function isNumber(evt) {
    evt = (evt) ? evt : window.event;
    var charCode = (evt.which) ? evt.which : evt.keyCode;
    if (charCode > 31 && (charCode < 48 || charCode > 57)) {
        return false;
    }
    return true;
}

$(document).ready(function(){
    // alert("hello project")
    $('form').submit(function(e){
        e.preventDefault()
        console.log('hi')
        $.ajax({
            url: '/registration_form',
            method: 'post',
            data: $('form').serialize(),
            success: function(data){
                if(data == 'error'){
                    $('h3').html(data)
                }else{
                    location.href = "/"
                }
            },
            error: function(data){
                // console.log('hi2')
                // alert(data.responseJSON);
            
            }
        })
        
    })
});

