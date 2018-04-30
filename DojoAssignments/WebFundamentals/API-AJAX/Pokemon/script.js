"use strict";


$(document).ready(function () {
    console.log('ready steady');
    WebFont.load({
        google: {
            families: ['Droid Sans', 'Droid Serif']
        }
    });
    for (var i=1; i < 152; i+=1) {
        var pokePic = i+".png";

        $.ajax({
            method: "GET",
            url: "https://pokeapi.co/api/v2/item/1/",
            dataType: "json",
            beforeSend: function( xhr ) {
                xhr.overrideMimeType( "text/plain; charset=x-user-defined" );
            }
        })
            .done(function( data ) {
                if ( console && console.log ) {
                    console.log( "Sample of data:", data.slice( 0, 100 ) );
                }
            });



    };
    var src = $('img').attr('src');
    console.log(src);



});