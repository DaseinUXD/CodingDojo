"use strict";

$(document).ready(function () {
    console.log('ready steady');

    $(document).on('click', '#submitBtn', function () {
        var first = $('input[type=text][name=firstName]').val();
        // console.log(first);
        var last = $('input[type=text][name=lastName]').val();
        var email = $('input[type=email][name=email]').val();
        var phone = $('input[type=tel][name=phone]').val();
        if (first === '' || last === '' || email === '' || phone === '' )
        {
            alert('Please do not leave any spaces blank');
            return;
        }
        var newRow = '<tr><td>'+first+'</td><td>'+last+'</td><td><a href=mailto:'+email+'>'+email+'</a></td><td><a href=tel:'+phone+'>'+phone+'</a></td></tr>';
        // console.log(last, first, email, phone, newRow);
        $('table tbody').append(newRow);
        return false;
    })

});