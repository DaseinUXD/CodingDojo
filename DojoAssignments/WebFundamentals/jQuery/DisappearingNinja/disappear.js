"use strict";

$(document).ready(function(){

    console.log($);
    $('#1').click(function () {
        console.log('i was clicked');
        $('#1').fadeOut()
    });
    $('#2').click(function () {
        console.log('i was clicked');
        $('#2').fadeOut()
    });
    $('#3').click(function () {
        console.log('i was clicked');
        $('#3').fadeOut()
    });
    $('#4').click(function () {
        console.log('i was clicked');
        $('#4').fadeOut()
    });
    $('#5').click(function () {
        console.log('i was clicked');
        $('#5').fadeOut()
    });
    $('#6').click(function () {
        console.log('i was clicked');
        $('#6').fadeOut()
    });
    $('#7').click(function () {
        console.log('i was clicked');
        $('#7').fadeOut()
    });
    $('#8').click(function () {
        console.log('i was clicked');
        $('#8').fadeOut()
    });

    $('#restore').click(function () {
        $('img').fadeIn()
    })
});