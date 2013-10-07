var csrftoken = $.cookie('csrftoken'); 

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    crossDomain: false, // obviates need for sameOrigin test
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type)) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$('button.followButton').live('click', function(e){
    e.preventDefault();
    $button = $(this);

    if($button.hasClass('following')){

        console.log('unfollowing');
        
        $.post("/follow/", {'projectId': projectId, 'followBool': false} );  
      
        $button.removeClass('following');
        $button.removeClass('unfollow');
        $button.text('Follow');
    } 

    else {
        
        $.post("/follow/", {'projectId': projectId, 'followBool': true} );  
    
        $button.addClass('following');
        $button.text('Following');
    }
});

$('button.followButton').hover(function(){
     $button = $(this);
    if($button.hasClass('following')){
        $button.addClass('unfollow');
        $button.text('Unfollow');
    }
}, function(){
    if($button.hasClass('following')){
        $button.removeClass('unfollow');
        $button.text('Following');
    }
});