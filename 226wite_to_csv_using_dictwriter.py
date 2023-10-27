from csv import DictWriter
with open('file4.csv','w',newline='') as f:
    csv_writer = DictWriter(f,fieldnames=['first name','last name','age'])
    csv_writer.writeheader()
    csv_writer.writerow({
        'first name': ' tohid',
        'last name': ' islam',
        'age': 25
    })
    csv_writer.writerow({
        'first name': ' rahul',
        'last name': ' roy',
        'age': 34
    })
    csv_writer.writerows([
        {'first name': ' tohid',
        'last name': ' islam',
        'age': 25},
        {'first name': ' rahul',
        'last name': ' roy',
        'age': 34},
        {'first name': ' nitin',
        'last name': ' rai',
        'age': 34}
    ])