$(window).scroll(function() {
    if($(this).scrollTop() > 50)
    {
        $('.navbar-trans').addClass('afterscroll');
    } else
    {
        $('.navbar-trans').removeClass('afterscroll');
    }

});

$("a[href^='http']").attr("target", "_blank");

function deleteGalleryImage() {
    document.getElementById("demo").style.color = "red";
}