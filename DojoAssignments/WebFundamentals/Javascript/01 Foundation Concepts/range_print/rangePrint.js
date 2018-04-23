//Range Print
// Create a function that can take a start point, end point, and skip amount, to print all numbers in the range.

function rangePrint(x, y, z)
{
    while (x < y)
    {
        var sum = x + z;
        console.log(sum);
        x++;
    }

}
rangePrint(2, 5, 2);

