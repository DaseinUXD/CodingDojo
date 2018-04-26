"use strict";

$(document).ready(function(){
    console.log('ready steady');
    // $('#images').on('click', 'img', function () {
    //     var srcNew = $(this).attr('src-alt');
    //     console.log(srcNew);
    //     $(this).attr('src', srcNew);
    // })
    $('#images img').hover(function(){
        var srcNew = $(this).attr('src-alt');
        console.log('hovered in', srcNew);
        var srcOrig = $(this).attr('src');
        $(this).attr('src', srcNew);
        $(this).attr('src-alt', srcOrig)
    }, function(){
        var srcOld = $(this).attr('src-alt');
        console.log('hovered out', 'src-alt', srcOld)
        $(this).attr('src', srcOld);
    });

});