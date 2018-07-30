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


$(document).ready(function() {
  $('.flexslider').flexslider({
    animation: "slide",
    smoothHeight: true,
    prevText: "",
    nextText: "",
    controlNav: false,
  });
});

$(".spoiler-trigger").click(function() {
    $(this).parent().next().collapse('toggle');
});

$('#review-form').bootstrapValidator({
//        live: 'disabled',
        message: 'This value is not valid',
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            Name: {
                validators: {
                    notEmpty: {
                        message: "Будь ласка вкажіть своє ім'я"
                    }
                }
            },

            Message: {
                validators: {
                    notEmpty: {
                        message: 'А як же відгук?'
                    }
                }
            }
        }
    });