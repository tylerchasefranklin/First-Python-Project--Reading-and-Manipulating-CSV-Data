import csv

with open('csv_input.csv') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    next(data, None)
    datasort = sorted(data, key=lambda d: d[5]) #sorting by birth order
    for col in datasort:
        if col[4] == 'F':                       #changing f's to female and m's to male
            col[4] = 'Female'
        else:
            col[4] = 'Male'

    with open("csv_output.csv", 'w') as myfile:
        writer = csv.writer(myfile)
        columnnames = ['Last Name', 'First Name', 'Gender', 'Marital Status', 'Birth Order', 'Quote']
        mylist = datasort
        # print mylist
        writer = csv.writer(myfile)
        writer.writerow(columnnames)                    #putting headers back in
        for col in mylist:
            myorder = (col[1], col[0], col[4], col[3], col[5], col[2])  #setting the column order
            print myorder
            writer.writerow(myorder)    #writing to output file
            # print(x)
