$(window).scroll(function() {
    if($(this).scrollTop() > 50)
    {
        $('.navbar-trans').addClass('afterscroll');
    } else
    {
        $('.navbar-trans').removeClass('afterscroll');
    }

});

$('button.pic-del').on('click', function() {
    var imgId = $(this).closest('.card-block').attr('id');
    $('#g-image-delete').append("<input hidden name='g_image_to_delete' value='" + imgId + "'>");
    this.closest('.g-image-card').remove();
})
