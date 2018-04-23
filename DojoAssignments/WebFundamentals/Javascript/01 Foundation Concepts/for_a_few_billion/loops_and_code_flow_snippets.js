//The following code will print the first two lines, but then will immediately exit the while loop.
var num = 1;
while (num < 5)
{
    if (num == 3)
    {
        break;
        // if you have additional code down here, it will never run!
    }
    console.log("I'm counting! The number is ", num);
    num = num + 1;          // if we break, we leave the WHILE loop so these lines won’t run
}

//The following code will count from 1 to 4, printing a statement about each number,
// but will completely forget to say anything about 3, because when num == 3,
// the continue forces it to skip the rest of that loop and continue from the top of the loop (after incrementing num).

for (var num = 1; num < 5; num += 1)
{
    if (num == 3)
    {
        continue;
        // if you have additional code down here, it will never run!
    }
    console.log("I'm counting! The number is ", num);
}
