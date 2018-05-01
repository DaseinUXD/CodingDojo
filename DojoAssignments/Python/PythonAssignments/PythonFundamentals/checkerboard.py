def checkerboard():
    for i in range(8):

        row1 = ([ " "+"*"+" "+"*"+" "+"*"+ " "+"*"+" "])
        rowEven = '\n'.join(row1)
        print rowEven

        row2= ([ "*"+ " "+"*"+" "+"*"+" "+"*"+ " "+"*"])
        rowOdd = '\n'.join(row2)
        print rowOdd


checkerboard()
