//var newArray = numbersOnly([1, "apple", -3, "orange", 0.5]);
// newArray is [1, -3, 0.5]


function numbersOnly(arr) {
    //var arr = [];
    var newArray = [];
    for (i = 0; i < arr.length; i++){
        if(typeof arr[i] === "number" ) {
            newArray.push (arr[i]);
            console.log(newArray);

        }
    }
}
numbersOnly([3, "new", 4, "text", 5]);