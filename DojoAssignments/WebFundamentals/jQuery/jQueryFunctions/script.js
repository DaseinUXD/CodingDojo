"use strict";

$(document).ready(function () {
    console.log($);
    $('h1').click(function () {
        $('h1').hide()
    });
    $('h2').click(function () {
        $('h1').show()
    });
    $('h3').click(function () {
        $('h2').toggle()
    });
    $('#slideDown').click(function () {
        $('#slidingText').slideDown();
        $('#slideUp').show();
    });
    $('#slideUp').click(function () {
        $('#slidingText').slideUp();
    });
    $('#slideToggle').click(function () {
        $('#toggleText').slideToggle();
    });

    $('#fadeOut').click(function () {
        $('#fadingText').fadeOut();
    });

    $('#fadeIn').click(function () {
        $('#fadingText').fadeIn();
    });

    $('#addClass').click(function () {
        $('#addClassText').addClass('crazyText');
        $('#removeClass').show();
    });
    $('#removeClass').click(function () {
        $('#addClassText').removeClass('crazyText');
    });

    $('#beforeBtn').click(function () {
        $('#before').before('This is now before!');
    });
    $('#afterBtn').click(function () {
        $('#after').after('This is now after!');
    });
    $('#appendBtn').click(function () {
        $('#appendText').append('This is appended!');
    });

    $('#htmlBtn').click(function () {
        $('#htmlText').html('This is <b>new</b> and <i>formatted</i> text');
    });
    $('#attrBtn').click(function () {
        var attr = $('#attrText').attr('draggable', 'true');
        console.log(attr);
    });
    $( "input" )
        .keyup(function() {
            var value = $( this ).val();
            $( "#inputText" ).text( value );
        })
        .keyup();

    $('#textBtn').click(function () {
        $('#textText').text('This is new, albeit un-formatted text');
    });
    $( "h5" ).data( "test", { first: 16, last: "pizza!" } );
    $( "span:first" ).text( $( "h5" ).data( "test" ).first );
    $( "span:last" ).text( $( "h5" ).data( "test" ).last );

});