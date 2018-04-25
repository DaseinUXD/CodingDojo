"use strict";

$(document).ready(function () {
    console.log($, "i'm ready");

    // Attr way
    $('.puzzle').on('click', '#top1', function () {
        var srcNew = $('img#top1').attr('src-alt');
        console.log(srcNew);
        $(this).attr('src', srcNew);
    });
    $('.puzzle').on('click', '#top2', function () {
        var srcNew = $('img#top2').attr('src-alt');
        console.log(srcNew);
        $(this).attr('src', srcNew);
    });
    $('.puzzle').on('click', '#top3', function () {
        var srcNew = $('img#top3').attr('src-alt');
        console.log(srcNew);
        $(this).attr('src', srcNew);
    });
    $('.puzzle').on('click', '#top4', function () {
        var srcNew = $('img#top4').attr('src-alt');
        console.log(srcNew);
        $(this).attr('src', srcNew);
    });
    $('.puzzle').on('click', '#top5', function () {
        var srcNew = $('img#top5').attr('src-alt');
        console.log(srcNew);
        $(this).attr('src', srcNew);
    });


});
