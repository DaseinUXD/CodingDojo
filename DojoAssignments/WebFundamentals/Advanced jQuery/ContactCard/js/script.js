"use strict";

$(document).ready(function () {
    console.log('ready steady');

    $(document).on('click', '#addUser', function () {
        // console.log('add user button clicked');
        var first = $('#firstName').val();
        var last = $('#lastName').val();
        var desc = $('#description').val();
        // alert(first);
        // console.log(first);
        $('#cards').append(
            '                    <div class="card">\n' +
            '                        <div class="card-body">\n' +
            '                            <h3 class="card-title">' + first + ' ' + last + '</h3>\n' +
            '                            <button type="submit" class="btn btn-outline-info">Click for description</button>\n' +
            '                        </div>\n' +
            '                    </div>'
        );
        return false;
    });



});