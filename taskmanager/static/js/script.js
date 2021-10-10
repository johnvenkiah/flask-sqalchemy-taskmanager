$(document).ready(function(){
    // sidenav initialization
    $('.sidenav').sidenav();

    // datepicker initialization
    $('.datepicker').datepicker({
        format: "dd, mmmm, yyyy",
        i18n: {done: "Select"}
    });

    let selects = document.querySelectorAll("select");
    M.FormSelect.init(selects);

    $('.collapsible').collapsible();
});