$('button.pic-del').on('click', function() {
    var imgId = $(this).closest('.card-block').attr('id');
    $('#g-image-delete').append("<input hidden name='g_image_to_delete' value='" + imgId + "'>");
    this.closest('.g-image-card').remove();
})