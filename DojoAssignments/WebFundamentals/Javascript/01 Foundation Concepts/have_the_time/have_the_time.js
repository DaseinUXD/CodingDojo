
function haveTime(hour, minute, period) {

    if (minute > 30) {
        start = "It's almost"
        if(period == "AM") {
            end = "in the morning"
            else {
                end = "in the evening"
            }
    else {
            start = "It's just after";

        }
    }

    }

    console.log("It's almost ", hour+1,  "in the morning")

}

