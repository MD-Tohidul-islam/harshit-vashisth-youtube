from csv import writer
with open('file3.csv','w',newline='') as f:
    csv_writer=  writer(f)
    # methods = writerrow , writerows
    csv_writer.writerow(['name','country'])
    csv_writer.writerow(['tohidul','bagladesh'])
    csv_writer.writerow(['rahul','india'])

    csv_writer.writerows([['name','country'],['nitin','india'],['mohit','london']])

