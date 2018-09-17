$(function() {
    $(".expand-button").click(function() {
        info = $(this).closest(".spell-card").find(".extra-info")
        info.slideToggle(250);
    });
});
