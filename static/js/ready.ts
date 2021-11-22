import $ from "jquery";

$(() => {
    if(window.location.href.includes('logout')){
        $("#logout_form").trigger("submit");
    }
    $("#app-loading").addClass("loaded");
});
