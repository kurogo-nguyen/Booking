$('.navTrigger').click(function () {
    $(this).toggleClass('active');
    console.log("Clicked menu");
    $("#mainListDiv").toggleClass("show_list");
    $("#mainListDiv").fadeIn();

});
$(window).scroll(function() {
    if ($(document).scrollTop() > 50) {
        $('.navbar').addClass('bg-dark');
        console.log("OK");
    } else {
        $('.navbar').removeClass('bg-dark');
    }
});