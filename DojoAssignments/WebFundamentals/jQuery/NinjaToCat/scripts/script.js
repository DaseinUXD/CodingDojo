"use strict";

$(document).ready(function () {
    console.log($, "i'm ready")
    // CSS Way
    $('.puzzle').on('click', '#top1', function () {
        $('#top1').css('visibility', 'hidden');
        $('#bottom1').css('visibility', 'visible');
    });
    $('.puzzle').on('click', '#top2', function () {
        $('#top2').css('visibility', 'hidden');
        $('#bottom2').css('visibility', 'visible');
    });
    $('.puzzle').on('click', '#top3', function () {
        $('#top3').css('visibility', 'hidden');
        $('#bottom3').css('visibility', 'visible');
    });
    $('.puzzle').on('click', '#top4', function () {
        $('#top4').css('visibility', 'hidden');
        $('#bottom4').css('visibility', 'visible');
    });
    $('.puzzle').on('click', '#top5', function () {
        $('#top5').css('visibility', 'hidden');
        $('#bottom5').css('visibility', 'visible');
    });

});
